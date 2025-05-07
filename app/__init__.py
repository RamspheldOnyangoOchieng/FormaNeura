from flask import Flask
from .routes import main
from .whatsapp.handler import handle_whatsapp_message
from .email.notifier import send_email
from .db.supabase_client import insert_form_data

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(main)

    # Register Twilio webhook for WhatsApp
    app.add_url_rule('/whatsapp', view_func=handle_whatsapp_message, methods=['POST'])
    
    return app
