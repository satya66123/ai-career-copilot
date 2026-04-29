import streamlit as st
import time

from auth import login_user, register_user
from agents.orchestrator import run_all_agents
from database.queries import save_resume, update_result, get_user_history, get_user_stats
from utils.validators import clean_skills
from utils.helpers import validate_input
from services.ollama_service import generate_response

# NEW IMPORTS (ADDED)
from utils.pdf_generator import generate_pdf
from agents.keyword_agent import generate_keywords

st.set_page_config(page_title="AI Career Copilot", layout="wide")

# =========================
# DARK UI + CARDS
# =========================
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION INIT
# =========================
for key, default in {
    "user": None,
    "chat_history": [],
    "greeted": False,
    "login_time": 0,
    "last_request": 0,
    "last_resume": "",
    "model": "mistral:latest"
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# =========================
# SESSION TIMEOUT
# =========================
if st.session_state.user:
    if time.time() - st.session_state.login_time > 3600:
        st.session_state.user = None
        st.warning("Session expired")
        st.rerun()

# =========================
# AUTH
# =========================
if st.session_state.user is None:

    st.title("🔐 Login / Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(u, p):
                st.session_state.user = u
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        nu = st.text_input("New Username")
        np = st.text_input("New Password", type="password")

        if st.button("Register"):
            register_user(nu, np)
            st.success("Registered")

# =========================
# MAIN APP
# =========================
else:

    st.title("🚀 AI Career Copilot")

    # =========================
    # SIDEBAR
    # =========================
    st.sidebar.title("⚙️ Controls")

    st.session_state.model = st.sidebar.selectbox(
        "Model",
        ["mistral:latest", "llama3:latest", "phi3:latest"],
        index=0
    )

    st.sidebar.info(f"Model: {st.session_state.model}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    # =========================
    # USER ANALYTICS (NEW)
    # =========================
    stats = get_user_stats(st.session_state.user)
    st.sidebar.metric("Total Analyses", stats["total"])
    st.sidebar.metric("Avg ATS Score", stats["avg_score"])

    # =========================
    # HISTORY TOGGLE
    # =========================
    if "show_history" not in st.session_state:
        st.session_state.show_history = False

    toggle_label = "📊 Show History" if not st.session_state.show_history else "❌ Hide History"

    if st.sidebar.button(toggle_label):
        st.session_state.show_history = not st.session_state.show_history
        st.rerun()

    if st.session_state.show_history:
        st.sidebar.markdown("## 📊 History")

        history = get_user_history(st.session_state.user)

        if history:
            for row in history:
                st.sidebar.markdown("---")
                st.sidebar.markdown(f"**🕒 {row['created_at']}**")
                st.sidebar.markdown(f"**Model :** **{row['model']}**")
                st.sidebar.markdown(f"**📊 ATS Score:** {row.get('ats_score', 'N/A')}")
                preview = row["content"][:150].replace("\n", " ")
                st.sidebar.write(preview + "...")
        else:
            st.sidebar.info("No history found")

    if not st.session_state.greeted:
        st.success(f"Welcome {st.session_state.user}")
        st.session_state.greeted = True

    st.markdown("---")

    # =========================
    # RATE LIMIT
    # =========================
    def check_rate():
        if time.time() - st.session_state.last_request < 2:
            st.warning("Too fast")
            st.stop()
        st.session_state.last_request = time.time()

    # =========================
    # RESUME ANALYZER
    # =========================
    st.subheader("📄 Resume Analyzer")

    resume = st.text_area("Resume", height=200)
    jd = st.text_area("Job Description", height=200)

    if st.button("Analyze"):

        if resume and jd:

            if not validate_input(resume) or not validate_input(jd):
                st.error("Invalid input")
                st.stop()

            check_rate()

            row_id = save_resume(st.session_state.user, resume, jd, st.session_state.model)

            with st.spinner("Running AI..."):

                result = run_all_agents(
                    resume[:1500],
                    jd[:1500],
                    True,
                    st.session_state.model
                )

                optimized = clean_skills(result["optimized_resume"])

            if row_id:
                update_result(row_id, optimized, result["keyword_ats"]["score"])

            st.session_state.last_resume = resume

            st.success("Done")

            # =========================
            # CARDS UI
            # =========================
            st.markdown(f"""
            <div class="card">
            <h3>📄 Optimized Resume</h3>
            <p>{optimized}</p>
            </div>
            """, unsafe_allow_html=True)

            # PDF DOWNLOAD (NEW)
            pdf_file = generate_pdf(optimized)
            with open(pdf_file, "rb") as f:
                st.download_button("📥 Download PDF Resume", f, file_name="resume.pdf")

            st.markdown(f"""
            <div class="card">
            <h3>📊 ATS Scores</h3>
            <p>Keyword: {result['keyword_ats']['score']}</p>
            <p>Semantic: {result['semantic_ats']['score']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card">
            <h3>🧠 Job Fit</h3>
            <p>{result['job_fit']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card">
            <h3>🎯 Job Recommendations</h3>
            <p>{result.get('job_recommendations', 'No recommendations')}</p>
            </div>
            """, unsafe_allow_html=True)

            # NEW FEATURES
            st.markdown(f"""
            <div class="card">
            <h3>📊 Resume Breakdown</h3>
            <p>{result.get('scoring', 'No scoring')}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card">
            <h3>🧠 Skill Roadmap</h3>
            <p>{result.get('roadmap', 'No roadmap')}</p>
            </div>
            """, unsafe_allow_html=True)

            # Suggestions
            st.markdown("### 💡 Suggestions")
            prompt = f"Give 3 improvements for this resume:\n{resume[:1000]}"
            suggestions = generate_response(prompt, st.session_state.model)
            st.write(suggestions)

        else:
            st.error("Fill both fields")

    # =========================
    # KEYWORD GENERATOR (NEW)
    # =========================
    st.markdown("---")
    st.subheader("🔍 Keyword Generator")

    role_input = st.text_input("Enter job role")

    if role_input:
        keywords = generate_keywords(role_input, st.session_state.model)
        st.write(keywords)

    # =========================
    # CHAT (UPGRADED)
    # =========================
    st.markdown("---")
    st.subheader("💬 Chat")

    user_input = st.chat_input("Ask...")

    if user_input:

        if not validate_input(user_input):
            st.error("Invalid input")
            st.stop()

        check_rate()

        st.session_state.chat_history.append(("user", user_input))

        history_text = "\n".join(
            [f"{r}: {m}" for r, m in st.session_state.chat_history[-5:]]
        )

        resume_ctx = st.session_state.get("last_resume", "")

        prompt = f"""
You are a career coach.

You help with:
- Resume improvement
- Interview prep
- Skill advice
- Career guidance

Conversation:
{history_text}

Resume:
{resume_ctx[:1000]}

User question:
{user_input}
"""

        response = generate_response(prompt, st.session_state.model)

        if not response:
            response = "No response"

        st.session_state.chat_history.append(("ai", response))

    for role, msg in st.session_state.chat_history:
        st.chat_message("assistant" if role == "ai" else "user").write(msg)