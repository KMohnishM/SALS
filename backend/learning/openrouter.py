import requests
from dotenv import load_dotenv
import os


load_dotenv()
def call_openrouter(prompt, model="deepseek/deepseek-r1-0528-qwen3-8b:free"):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "HTTP-Referer": "https://yourdomain.com",
        "X-Title": "SALS Assistant"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You're a learning assistant for DSA/DAA topics."},
            {"role": "user", "content": prompt}
        ]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
    try:
        return res.json()
    except Exception as e:
        return {"error": f"Failed to parse JSON response: {str(e)}", "text": res.text}
