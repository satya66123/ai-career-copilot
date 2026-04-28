def clean_skills(text):
    replacements = {
        "micro services": "Microservices",
        "llms": "LLMs",
        "ollama.open ai": "Ollama, OpenAI"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text