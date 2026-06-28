def handler(store, r): return {"solutions": [s.to_dict() for s in store.solutions()], "nextToken": ""}
