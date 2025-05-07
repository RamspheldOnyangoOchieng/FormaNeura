import requests
from flask import current_app

def generate_form(form_id):
    url = "https://api.gemini.com/form/generate"
    headers = {"Authorization": f"Bearer {current_app.config['GEMINI_API_KEY']}"}
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
        return form_link
    else:
        raise Exception("Failed to generate form from Gemini.")
