def handler(store, r): return {"campaigns": [c.to_dict() for c in store.campaigns()], "nextToken": ""}
