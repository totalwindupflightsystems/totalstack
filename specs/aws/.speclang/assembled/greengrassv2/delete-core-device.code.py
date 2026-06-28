def delete_core_device(store, request: dict) -> dict:
    store.delete_core_device(request["coreDeviceThingName"])
    return {}
