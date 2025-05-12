# supabase_client.py

import supabase
from flask import current_app
import traceback
import logging
import traceback

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_client():
    """
    Initializes and returns a Supabase client using the Flask app context.
    """
    try:
        client = supabase.create_client(
            current_app.config['SUPABASE_URL'],
            current_app.config['SUPABASE_KEY']
        )
        print("[Supabase Client Initialized]")  # Debugging log
        return client
    except Exception:
        print(f"[Supabase Init Error]\n{traceback.format_exc()}")
        raise

def insert_form_data(form_data):
    """
    Inserts form data into the 'form_submissions' table.
    """
    try:
        client = get_client()
        response = client.table('form_submissions').insert(form_data).execute()
        print(f"[Supabase Insert Form Data Response] {response}")  # Debugging log
        return response
    except Exception:
        print(f"[Supabase Insert Form Data Error] Form Data: {form_data}\n{traceback.format_exc()}")
        raise

def store_form_request(user, form_link):
    """
    Stores a form request in the 'form_requests' table.
    """
    try:
        client = get_client()
        payload = {"username": user, "form_link": form_link}
        logger.info(f"[Supabase Store Request] Payload: {payload}")
        
        response = client.table('form_requests').insert(payload).execute()
        logger.info(f"[Supabase Store Request Response] {response}")
        
        if not response.data:
            raise ValueError(f"No data returned from Supabase: {response}")
        
        return response

    except Exception:
        logger.error(f"[Supabase Store Request Error] Payload: {payload}\n{traceback.format_exc()}")
        raise

def get_form_by_id(form_id):
    """
    Retrieves a form by its ID from the 'forms' table.
    """
    try:
        client = get_client()
        print(f"[Supabase Get Form] ID: {form_id}")  # Debugging log
        response = client.table('forms').select("*").eq("id", form_id).single().execute()
        print(f"[Supabase Get Form Response] {response}")  # Debugging log
        return response.data
    except Exception:
        print(f"[Supabase Get Form Error] ID: {form_id}\n{traceback.format_exc()}")
        raise
