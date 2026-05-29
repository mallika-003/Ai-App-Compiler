def generate_api_schema(architecture):

    apis = architecture.get("apis", [])

    api_schema = []

    for api in apis:

        if api == "/login":
            api_schema.append({
                "endpoint": "/login",
                "method": "POST"
            })

        elif api == "/contacts":
            api_schema.append({
                "endpoint": "/contacts",
                "method": "GET"
            })

    return api_schema