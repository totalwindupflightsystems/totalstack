def handler(store, request: dict) -> dict:
    return store.reboot_broker(BrokerId=request["BrokerId"])
