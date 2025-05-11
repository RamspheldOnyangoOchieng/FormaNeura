# handler.py

from twilio.twiml.messaging_response import MessagingResponse
from app.ai.gemini_form_builder import generate_form
from app.db.supabase_client import store_form_request
from utils.helpers import generate_random_id
from flask import request
import traceback

def handle_whatsapp_message():
    """
    Handles incoming WhatsApp messages, generates a form using AI, and stores the request in the database.
    """
    message = request.form.get('Body', '').lower()
    sender = request.form.get('From', '')
    response = MessagingResponse()

    if "form" in message:
        form_id = generate_random_id()
        try:
            # 1. Generate the AI-powered form (HTML)
            form_html = generate_form(form_id)

            # 2. Create a link (in practice, you'd host/save this HTML somewhere and return a URL)
            form_link = f"https://formaneura.onrender.com/forms/{form_id}"  # Update as needed

            # 3. Store request in Supabase
            store_form_request(sender, form_link)

            # 4. Respond to the user
            response.message(f"Your form has been generated. Fill it out here: {form_link}")

        except Exception:
            print(f"[WhatsApp Handler Error] Could not generate form:\n{traceback.format_exc()}")
            response.message("Sorry, we encountered an issue generating your form. Please try again later.")
    else:
        response.message("Hi there! To get started, type the kind of form you need (e.g., 'Support Form').")

    return str(response)
