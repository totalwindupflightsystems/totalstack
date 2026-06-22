def handler(store, request: dict) -> dict:
    return store.create_db_parameter_group(
        name=request["name"],
        description=request.get("description"),
        parameters=request.get("parameters"),
        tags=request.get("tags"),
    )
