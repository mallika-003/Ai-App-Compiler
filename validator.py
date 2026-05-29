def validate_schema(data):

    errors = []

    # Check app_type
    if "app_type" not in data:
        errors.append("Missing app_type")

    # Check features
    if "features" not in data:
        errors.append("Missing features")

    return errors


def validate_architecture(api_schema, db_schema):

    errors = []

    # Get all DB table names
    db_tables = [
        table["table_name"]
        for table in db_schema
    ]

    # Check if contacts API exists
    for api in api_schema:

        if (
            api["endpoint"] == "/contacts"
            and "contacts" not in db_tables
        ):
            errors.append(
                "Contacts API exists but contacts table missing"
            )

    return errors