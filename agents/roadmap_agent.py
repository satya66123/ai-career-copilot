from services.ollama_service import generate_response

def skill_roadmap(resume, job_description, model="mistral:latest"):

    prompt = f"""
Create a learning roadmap for missing skills.

Resume:
{resume}

Job Description:
{job_description}

Return step-by-step plan with timeline.
"""

    return generate_response(prompt, model)