def generate_ui_schema(architecture):

    pages = architecture.get("pages", [])

    ui_schema = []

    for page in pages:

        if page == "login":
            ui_schema.append({
                "page": "login",
                "components": [
                    "email_input",
                    "password_input",
                    "login_button"
                ]
            })

        elif page == "dashboard":
            ui_schema.append({
                "page": "dashboard",
                "components": [
                    "sidebar",
                    "analytics_cards",
                    "charts"
                ]
            })

        elif page == "contacts":
            ui_schema.append({
                "page": "contacts",
                "components": [
                    "contact_table",
                    "add_contact_button"
                ]
            })

    return ui_schema