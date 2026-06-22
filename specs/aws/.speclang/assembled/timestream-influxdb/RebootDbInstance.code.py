def handler(store, request: dict) -> dict:
    return store.reboot_db_instance(
        identifier=request["identifier"],
    )
