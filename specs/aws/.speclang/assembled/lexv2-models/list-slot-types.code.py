def list_slot_types(store, request: dict) -> dict:
    types = store.list_slot_types(request["botId"], request["botVersion"], request["localeId"])
    return {"slotTypeSummaries": types}
