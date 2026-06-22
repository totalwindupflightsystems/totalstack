def handler(store, request: dict) -> dict:
    return store.get_db_instance(
        identifier=request["identifier"],
    )
