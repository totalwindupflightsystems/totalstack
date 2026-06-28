def handler(store, request: dict) -> dict:
    backup_ids = request.get("BackupIds", [])
    if backup_ids:
        records = []
        for bid in backup_ids:
            try:
                records.append(store.get_backup(bid).to_dict())
            except BackupNotFound:
                pass
        return {"Backups": records}
    return {"Backups": [r.to_dict() for r in store.backups()]}
