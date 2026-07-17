def handler(store, r: dict) -> dict:
    return store.delete_filesystem(r['FileSystemId'])