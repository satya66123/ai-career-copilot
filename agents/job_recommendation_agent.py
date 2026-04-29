from services.ollama_service import generate_response

def recommend_jobs(resume, model="mistral:latest"):

    prompt = f"""
You are a career advisor.

Analyze this resume and suggest:

1. Top 3 suitable job roles
2. Required skills for each role
3. Why the candidate fits

Resume:
{resume}

Format:

## Recommended Roles
- Role 1
- Role 2
- Role 3

## Skills Needed
- skill list

## Why Fit
- explanation
"""

    return generate_response(prompt, model)