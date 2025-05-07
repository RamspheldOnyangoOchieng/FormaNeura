import requests
from flask import current_app

def generate_form(form_id):
    try:
        url = "https://api.gemini.com/form/generate"
        headers = {
            "Authorization": f"Bearer {current_app.config['GEMINI_API_KEY']}",
            "Content-Type": "application/json"
        }
        payload = {
            "form_id": form_id,
            "fields": [
                {"label": "Full Name", "type": "text", "required": True},
                {"label": "Email", "type": "email", "required": True},
                {"label": "Issue Description", "type": "textarea", "required": True}
            ]
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            form_link = response.json().get('form_link')
            if not form_link:
                raise ValueError("Form link missing in Gemini response.")
            return form_link
        else:
            error_msg = response.json().get("error", response.text)
            raise Exception(f"Gemini API Error: {error_msg}")

    except Exception as e:
        print(f"[Gemini Form Builder Error] Failed to generate form for ID {form_id}: {e}")
        raise Exception("Failed to generate form from Gemini.")
