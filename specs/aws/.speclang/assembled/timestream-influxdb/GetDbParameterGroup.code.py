def handler(store, request: dict) -> dict:
    return store.get_db_parameter_group(
        identifier=request["identifier"],
    )
