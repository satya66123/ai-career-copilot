from services.ollama_service import generate_response

def resume_scoring(resume, job_description, model="mistral:latest"):

    prompt = f"""
Evaluate this resume vs job description.

Return ONLY:

Skills Match: <percentage>
Experience Match: <percentage>
AI Readiness: <percentage>

Resume:
{resume}

Job Description:
{job_description}
"""

    return generate_response(prompt, model)