from services.ollama_service import generate_response

def optimize_resume(resume, job_description, strict_mode=True, model="mistral:latest"):

    if strict_mode:
        rules = """
- DO NOT change company names, roles, dates
- DO NOT create fake data
- DO NOT use placeholders
- ONLY improve wording
"""
    else:
        rules = "You can improve freely."

    prompt = f"""
You are a resume editor.

{rules}

Resume:
{resume}

Job Description:
{job_description}

Output structured resume.
"""

    return generate_response(prompt,model)
