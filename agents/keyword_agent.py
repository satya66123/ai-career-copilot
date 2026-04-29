from services.ollama_service import generate_response

def generate_keywords(role, model="mistral:latest"):

    prompt = f"""
Generate ATS-optimized keywords for: {role}

STRICT RULES:
- Focus only on TECHNICAL skills
- NO soft skills
- NO generic words
- Keep it concise and relevant

FORMAT:

## Core Skills
- (only technical skills)

## Technologies
- (frameworks, architectures)

## Tools
- (only important tools used in resumes)

Limit:
- Max 6 per section
"""

    return generate_response(prompt, model)