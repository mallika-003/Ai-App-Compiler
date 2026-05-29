def repair_schema(data, errors, db_schema=None):

    if "Missing features" in errors:
        data["features"] = []

    if "Missing app_type" in errors:
        data["app_type"] = "Unknown"

    # Repair missing contacts table
    if "Contacts API exists but contacts table missing" in errors:

        if db_schema is not None:

            db_schema.append({
                "table_name": "contacts",
                "columns": []
            })

    return data