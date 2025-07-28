import os
import requests
from dotenv import load_dotenv



load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
#API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": f"{GEMINI_API_KEY}"
}

def generate_learning_path(user_goal):
    prompt = f"""
Act as an expert learning and curriculum designer.

A user has the following learning goal: "{user_goal}"

Generate a structured 6–8 week learning path tailored to this goal. For each week, include:
- Topic
- Learning objective
- Estimated time (in hours)
- A free learning resource with title and URL

Return output in JSON format with keys: "week", "topic", "objective", "time_hours", "resource_title", "resource_url".
"""

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        try:
            content = response.json()
            text = content['candidates'][0]['content']['parts'][0]['text']
            return text
        except Exception as e:
            return f"Error parsing response: {e}"
    else:
        return f"API Error: {response.status_code} - {response.text}"

