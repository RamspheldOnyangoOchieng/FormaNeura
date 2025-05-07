from twilio.twiml.messaging_response import MessagingResponse
from app.ai.gemini_form_builder import generate_form
from app.db.supabase_client import store_form_request
from utils.helpers import generate_random_id

def handle_whatsapp_message():
    message = request.form.get('Body').lower()
    sender = request.form.get('From')
    response = MessagingResponse()

    # Process incoming message to generate form
    if "form" in message:
        form_id = generate_random_id()
        form_link = generate_form(form_id)  # AI-powered form creation
        store_form_request(sender, form_link)  # Store in database

        response.message(f"Your form has been generated. Fill it out here: {form_link}")
    else:
        response.message("Please specify the type of form you need (e.g., 'IT Support Form').")

    return str(response)
