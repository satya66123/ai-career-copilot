import requests

def generate_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:latest",
                "prompt": prompt[:1200],
                "stream": False
            },
            timeout=360
        )

        if response.status_code != 200:
            return f"Ollama error: {response.text}"

        data = response.json()
        return data.get("response", "No response from model")

    except requests.exceptions.ConnectionError:
        return "⚠️ Ollama is not running. Start it with: `ollama serve`"
    except Exception as e:
        return f"Error: {str(e)}"