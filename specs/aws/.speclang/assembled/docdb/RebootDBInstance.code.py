def handler(store, request: dict):
    return store.reboot_instance(request["DBInstanceIdentifier"])
