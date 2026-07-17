def handler(store, r: dict) -> dict:
    return store.create_filesystem(r.get('CreationToken', 'test'))