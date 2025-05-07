




# **What Each Folder Does:**

**Folder/File**	                   **Purpose**

app/routes.py	              Registers Flask routes (/whatsapp, /form/<id>, /submit)

whatsapp/handler.py	          Handles message states, extracts intents, and interacts with Gemini

ai/gemini_form_builder.py	  Talks to Gemini API to generate HTML form structure

db/supabase_client.py	      Stores/retrieves form data from Supabase

email/notifier.py	          Sends form and response notifications via SMTP

forms/schema_manager.py	      Structures form inputs, builds forms dynamically

templates/*.html	          Flask templates for form and success page

utils/helpers.py	          Random ID generator, email validator, etc.

# **🛠 Optional Enhancements**
tests/: For unit testing

logs/: Store logs or errors if needed

docs/: Auto-generated documentation

config.py: For environment-aware config handling (dev/staging/prod)

