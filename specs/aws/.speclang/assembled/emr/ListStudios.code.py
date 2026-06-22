def handler(store, request: dict) -> dict:
    studios = store.list_studios()
    return {"Studios": [s.to_dict() for s in studios]}
