def describe_core_device(store, request: dict) -> dict:
    return store.describe_core_device(request["coreDeviceThingName"])
