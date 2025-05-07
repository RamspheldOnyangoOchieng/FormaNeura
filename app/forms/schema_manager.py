def create_form_schema(fields):
    # Returns HTML string for dynamic form generation
    html = "<form method='POST' action='/form/submit'>"
    for field in fields:
        html += f"<label>{field['label']}</label>"
        if field['type'] == 'text' or field['type'] == 'email':
            html += f"<input type='{field['type']}' name='{field['label']}' required>"
        elif field['type'] == 'textarea':
            html += f"<textarea name='{field['label']}' required></textarea>"
        html += "<br>"
    html += "<button type='submit'>Submit</button></form>"
    return html
