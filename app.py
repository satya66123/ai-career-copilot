import streamlit as st
import time

from auth import login_user, register_user
from agents.orchestrator import run_all_agents
from database.queries import save_resume, update_result
from utils.validators import clean_skills
from utils.helpers import validate_input
from services.ollama_service import generate_response

st.set_page_config(page_title="AI Career Copilot", layout="wide")

# =========================
# SESSION STATE INIT
# =========================
if "user" not in st.session_state:
    st.session_state.user = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "greeted" not in st.session_state:
    st.session_state.greeted = False

if "login_time" not in st.session_state:
    st.session_state.login_time = 0

if "last_request" not in st.session_state:
    st.session_state.last_request = 0


# =========================
# SESSION TIMEOUT (1 hour)
# =========================
if st.session_state.user:
    if time.time() - st.session_state.login_time > 3600:
        st.session_state.user = None
        st.warning("Session expired. Please login again.")
        st.rerun()


# =========================
# AUTH SECTION
# =========================
if st.session_state.user is None:

    st.title("🔐 Login / Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # LOGIN
    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)

            if user:
                st.session_state.user = username
                st.session_state.login_time = time.time()
                st.success("✅ Login successful")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

    # REGISTER
    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            register_user(new_user, new_pass)
            st.success("✅ Registered successfully")

# =========================
# MAIN APP
# =========================
else:

    st.title("🚀 AI Career Copilot")

    # Greeting
    if not st.session_state.greeted:
        st.success(f"👋 Welcome {st.session_state.user}!")
        st.session_state.greeted = True

    # Logout
    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.chat_history = []
        st.session_state.greeted = False
        st.rerun()

    st.markdown("---")

    # =========================
    # RATE LIMIT (2 sec)
    # =========================
    def check_rate_limit():
        if time.time() - st.session_state.last_request < 2:
            st.warning("Too many requests. Please wait...")
            st.stop()
        st.session_state.last_request = time.time()

    # =========================
    # RESUME ANALYZER
    # =========================
    st.subheader("📄 Resume Analyzer")

    resume = st.text_area("Paste Resume", height=200)
    job_description = st.text_area("Paste Job Description", height=200)

    if st.button("Analyze Resume"):

        if resume and job_description:

            # 🔐 Validate input
            if not validate_input(resume) or not validate_input(job_description):
                st.error("Invalid input detected")
                st.stop()

            # ⏱ Rate limit
            check_rate_limit()

            # Save input
            row_id = save_resume(resume, job_description)

            with st.spinner("🤖 Running AI Agents..."):

                result = run_all_agents(
                    resume[:1500],
                    job_description[:1500],
                    strict_mode=True
                )

                optimized = clean_skills(result["optimized_resume"])

            # Save results
            if row_id:
                update_result(row_id, optimized, result["keyword_ats"]["score"])

            st.success("✅ Analysis Complete")

            col1, col2 = st.columns(2)

            # LEFT
            with col1:
                st.markdown("## 📄 Optimized Resume")
                st.markdown(optimized)

                st.download_button(
                    "📥 Download Resume",
                    optimized,
                    file_name="resume.txt"
                )

            # RIGHT
            with col2:
                st.markdown("## 📊 ATS Scores")

                st.metric("Keyword", f"{result['keyword_ats']['score']}/100")
                st.metric("Semantic", f"{result['semantic_ats']['score']}/100")

                st.markdown("### ❌ Missing Keywords")
                st.write(", ".join(result["keyword_ats"]["missing"]))

            # Job Fit
            st.markdown("---")
            st.markdown("## 🧠 Job Fit Analysis")
            st.markdown(result["job_fit"])

        else:
            st.error("Please enter both fields")

    # =========================
    # CHAT SYSTEM
    # =========================
    st.markdown("---")
    st.subheader("💬 AI Career Chat")

    user_input = st.chat_input("Ask anything about your career...")

    if user_input:

        # 🔐 Validate
        if not validate_input(user_input):
            st.error("Invalid input")
            st.stop()

        # ⏱ Rate limit
        check_rate_limit()

        st.session_state.chat_history.append(("user", user_input))

        prompt = f"""
You are a helpful AI career assistant.

User question:
{user_input[:500]}

Give a helpful, concise answer.
"""

        response = generate_response(prompt)

        st.session_state.chat_history.append(("ai", response))

    # Show chat
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

    # End session
    if st.button("End Session"):
        st.info("👋 Goodbye! Thanks for using AI Career Copilot.")