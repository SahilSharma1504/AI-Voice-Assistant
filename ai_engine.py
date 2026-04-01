from google import genai

# -------------------------------
# Gemini Client Setup
# -------------------------------
client = genai.Client(api_key="Enter your Gemini API Key:")


# -------------------------------
# AI Chat Function
# -------------------------------
def ask_ai(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        if response and response.text:
            return response.text

        return "AI returned no response."

    except Exception as e:

        print("AI ERROR:", e)
        return "AI service is not available."