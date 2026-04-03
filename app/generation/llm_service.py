import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"


def generate_answer(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "")