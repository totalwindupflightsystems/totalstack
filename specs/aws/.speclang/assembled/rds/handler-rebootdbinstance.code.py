def handler(store, request: dict) -> dict:
    identifier = request["DBInstanceIdentifier"]
    return store.reboot_instance(identifier)
