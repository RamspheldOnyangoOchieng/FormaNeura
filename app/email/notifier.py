from flask_mail import Message, Mail
from flask import current_app

mail = Mail()

def send_email(form_data):
    msg = Message(
        subject="New Form Submission",
        sender=current_app.config['EMAIL_USER'],
        recipients=[current_app.config['EMAIL_USER']],
        body=f"New form submission from {form_data['full_name']}:\n{form_data['form_data']}"
    )
    mail.send(msg)
