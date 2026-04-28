import streamlit as st
from database.queries import save_resume
from services.ollama_service import generate_response

st.set_page_config(page_title="AI Career Copilot")

st.title("🚀 AI Career Copilot (Local AI)")

resume = st.text_area("Paste your Resume")
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume and job_description:
        # Save to DB
        save_resume(resume, job_description)

        # Prompt (improved)
        prompt = f"""
        You are a professional resume optimizer.

        Improve the resume based on the job description.

        Resume:
        {resume}

        Job Description:
        {job_description}

        Instructions:
        - Make it ATS-friendly
        - Add missing keywords
        - Improve bullet points
        - Keep it concise and professional
        - Use clear formatting
        """

        with st.spinner("Running AI (llama3:instruct)..."):
            result = generate_response(prompt)

        st.success("Optimization Complete ✅")
        st.write(result)

    else:
        st.error("Please fill all fields")