def generate_architecture(intent):

    features = intent.get("features", [])

    pages = []
    apis = []
    database_tables = []

    # Authentication feature
    if "authentication" in features:
        pages.append("login")
        apis.append("/login")
        database_tables.append("users")

    # Dashboard feature
    if "dashboard" in features:
        pages.append("dashboard")

    # Payments feature
    if "payments" in features:
        pages.append("payments")
        apis.append("/payments")
        database_tables.append("subscriptions")

    # Contacts feature
    pages.append("contacts")
    apis.append("/contacts")
    database_tables.append("contacts")

    return {
        "pages": pages,
        "apis": apis,
        "database_tables": database_tables
    }