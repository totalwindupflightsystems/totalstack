def handler(store, r: dict) -> dict:
    return store.describe_filesystems(r.get('FileSystemId'), r.get('CreationToken'))