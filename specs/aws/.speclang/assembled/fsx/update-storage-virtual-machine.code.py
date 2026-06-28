def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items()
              if k != "StorageVirtualMachineId" and v is not None}
    record = store.update_storage_virtual_machine(
        request["StorageVirtualMachineId"], **kwargs)
    return record.to_dict()
