import random
import string

def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def validate_email(email):
    # Placeholder function for email validation
    return '@' in email
