def handler(store, request: dict) -> dict:
    svm_ids = request.get("StorageVirtualMachineIds", [])
    if svm_ids:
        records = []
        for sid in svm_ids:
            try:
                records.append(
                    store.get_storage_virtual_machine(sid).to_dict())
            except StorageVirtualMachineNotFound:
                pass
        return {"StorageVirtualMachines": records}
    return {"StorageVirtualMachines":
            [r.to_dict() for r in store.storage_virtual_machines()]}
