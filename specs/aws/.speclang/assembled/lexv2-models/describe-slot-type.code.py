def describe_slot_type(store, request: dict) -> dict:
    return store.describe_slot_type(request["slotTypeName"], request["botId"], request["botVersion"], request["localeId"])
