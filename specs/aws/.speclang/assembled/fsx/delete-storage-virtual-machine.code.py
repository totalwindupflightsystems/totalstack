def handler(store, request: dict) -> dict:
    store.delete_storage_virtual_machine(
        request["StorageVirtualMachineId"])
    return {}
