def generate_db_schema(architecture):

    tables = architecture.get("database_tables", [])

    db_schema = []

    for table in tables:

        if table == "users":
            db_schema.append({
                "table_name": "users",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "email", "type": "string"},
                    {"name": "password", "type": "string"}
                ]
            })

        elif table == "contacts":
            db_schema.append({
                "table_name": "contacts",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "name", "type": "string"},
                    {"name": "phone", "type": "string"}
                ]
            })

    return db_schema