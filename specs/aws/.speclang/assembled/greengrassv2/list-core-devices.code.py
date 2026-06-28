def list_core_devices(store, request: dict) -> dict:
    devs = store.list_core_devices()
    return {"coreDevices": devs}
