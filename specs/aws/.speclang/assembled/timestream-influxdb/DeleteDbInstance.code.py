def handler(store, request: dict) -> dict:
    return store.delete_db_instance(
        identifier=request["identifier"],
    )
