from flask import Blueprint, render_template, request, redirect, url_for
from app.WhatsApp.handler import handle_whatsapp_message
from app.ai.gemini_form_builder import generate_form
from app.db.supabase_client import insert_form_data
from app.email.notifier import send_email

main = Blueprint('main', __name__)

@main.route('/form/<form_id>', methods=['GET'])
def form(form_id):
    # Retrieve form data from database (Supabase)
    form_data = get_form_by_id(form_id)
    return render_template('form.html', form=form_data)

@main.route('/form/submit', methods=['POST'])
def form_submit():
    form_data = request.form
    insert_form_data(form_data)  # Save to Supabase
    send_email(form_data)        # Notify via email
    return redirect(url_for('main.success'))

@main.route('/success')
def success():
    return render_template('submission_success.html')
