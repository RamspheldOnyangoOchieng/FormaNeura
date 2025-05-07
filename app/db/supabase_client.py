import supabase
from flask import current_app

def insert_form_data(form_data):
    client = supabase.create_client(current_app.config['SUPABASE_URL'], current_app.config['SUPABASE_KEY'])
    response = client.table('form_submissions').insert(form_data).execute()
    return response

def store_form_request(user, form_link):
    client = supabase.create_client(current_app.config['SUPABASE_URL'], current_app.config['SUPABASE_KEY'])
    response = client.table('form_requests').insert({"user": user, "form_link": form_link}).execute()
    return response
