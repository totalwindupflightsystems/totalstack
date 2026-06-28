def handler(store, r): return {"datasets": [d.to_dict() for d in store.datasets()], "nextToken": ""}
