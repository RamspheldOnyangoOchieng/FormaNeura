from twilio.twiml.messaging_response import MessagingResponse
from app.ai.gemini_form_builder import generate_form
from app.db.supabase_client import store_form_request
from utils.helpers import generate_random_id
from flask import request

def handle_whatsapp_message():
    message = request.form.get('Body', '').lower()
    sender = request.form.get('From', '')
    response = MessagingResponse()

    if "form" in message:
        form_id = generate_random_id()
        try:
            form_link = generate_form(form_id)  # AI-powered form creation
            store_form_request(sender, form_link)  # Store in database
            response.message(f"Your form has been generated. Fill it out here: {form_link}")
        except Exception as e:
            print(f"[WhatsApp Handler Error] Could not generate form: {e}")
            response.message("Sorry, we encountered an issue generating your form. Please try again later.")
    else:
        response.message("Hi there! To get started, type the kind of form you need (e.g., 'Support Form').")

    return str(response)
# This function handles incoming WhatsApp messages, generates a form using AI, and stores the request in the database.