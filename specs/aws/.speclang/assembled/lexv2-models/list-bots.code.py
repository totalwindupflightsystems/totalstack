def list_bots(store, request: dict) -> dict:
    bots = store.list_bots()
    return {"botSummaries": bots}
