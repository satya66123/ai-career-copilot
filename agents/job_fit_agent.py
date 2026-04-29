from services.ollama_service import generate_response

def analyze_job_fit(resume, job_description, strict_mode=True, model ="mistral:latest"):

    prompt = f"""
You MUST follow this format EXACTLY.

DO NOT write paragraphs.
DO NOT explain.
DO NOT summarize.

ONLY OUTPUT THIS:

## Fit Score
<number>

## Strengths
- point 1
- point 2
- point 3

## Gaps
- point 1
- point 2
- point 3

## Suggestions
- point 1
- point 2
- point 3

Rules:
- Only bullet points
- Use ONLY given resume
- No extra text before or after

Resume:
{resume}

Job Description:
{job_description}
"""
    return generate_response(prompt,model)