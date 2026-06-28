def delete_slot_type(store, request: dict) -> dict:
    store.delete_slot_type(request["slotTypeName"], request["botId"], request["botVersion"], request["localeId"])
    return {}
