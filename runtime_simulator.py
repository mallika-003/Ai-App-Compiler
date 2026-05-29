def simulate_runtime(ui_schema):

    pages = []

    for page in ui_schema:

        pages.append(
            f"Generated page: {page['page']}"
        )

    return pages