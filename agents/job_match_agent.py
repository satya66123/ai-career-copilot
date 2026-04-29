from services.ollama_service import generate_response

def match_jobs(resume, job_list, model="mistral:latest"):

    prompt = f"""
Match this resume with jobs and rank them.

Resume:
{resume}

Jobs:
{job_list}

Return ranked list with scores.
"""

    return generate_response(prompt, model)