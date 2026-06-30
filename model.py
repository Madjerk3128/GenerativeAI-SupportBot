import os
import google.generativeai as genai

# Load API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

genai.configure(api_key=GEMINI_API_KEY)

# Using gemini-2.5-flash as supported by the environment/API key with active quota
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(prompt):
    try:
        if not GEMINI_API_KEY:
            return "Error: GEMINI_API_KEY environment variable is not set."

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Sorry, I encountered an error while processing your request: {str(e)}"
