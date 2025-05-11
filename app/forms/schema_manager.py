def create_form_schema(fields):
    """
    Generates an HTML string for dynamic form generation based on the provided fields.
    """
    try:
        html = "<form method='POST' action='/form/submit'>"
        for field in fields:
            html += f"<label>{field['label']}</label>"
            if field['type'] in ['text', 'email']:
                html += f"<input type='{field['type']}' name='{field['label']}' required>"
            elif field['type'] == 'textarea':
                html += f"<textarea name='{field['label']}' required></textarea>"
            else:
                raise ValueError(f"Unsupported field type: {field['type']}")
            html += "<br>"
        html += "<button type='submit'>Submit</button></form>"
        return html
    except Exception as e:
        print(f"[Schema Manager Error] Could not create form schema: {e}")
        raise
