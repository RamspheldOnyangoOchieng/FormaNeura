import google.generativeai as genai
from flask import current_app

genai.configure(api_key=current_app.config['GEMINI_API_KEY'])

def generate_form(form_id):
    try:
        model = genai.GenerativeModel('gemini-pro')

        prompt = f"""
        Generate an HTML form for a support ticket with the following fields:
        - Full Name (text, required)
        - Email (email, required)
        - Issue Description (textarea, required)

        The form should post to "/submit/{form_id}" and include minimal Bootstrap styling.
        """

        response = model.generate_content(prompt)

        if not response or not response.text:
            raise Exception("Empty response from Gemini")

        return response.text  # This is the HTML structure

    except Exception as e:
        print(f"[Gemini Form Builder Error] Failed to generate form for ID {form_id}: {e}")
        raise Exception("Failed to generate form from Gemini.")

    return None