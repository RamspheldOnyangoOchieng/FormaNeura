import google.generativeai as genai
from config import Config  # ✅ Import your custom config class

genai.configure(api_key=Config.GEMINI_API_KEY)  # ✅ Use static config value

def generate_form(form_id):
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

        prompt = f"""
        Generate an HTML form for a support ticket with the following fields:
        - Full Name (text, required)
        - Email (email, required)
        - Issue Description (textarea, required)

        The form should post to "/submit/{form_id}" and include minimal Bootstrap styling.
        """

        response = model.generate_content(prompt)

        if not response or not hasattr(response, "text") or not response.text:
            raise Exception("Empty response from Gemini")

        return response.text

    except Exception as e:
        print(f"[Gemini Form Builder Error] Failed to generate form for ID {form_id}: {e}")
        raise Exception("Failed to generate form from Gemini.")

    return None