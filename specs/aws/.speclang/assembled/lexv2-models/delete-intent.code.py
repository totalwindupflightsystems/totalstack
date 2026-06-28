def delete_intent(store, request: dict) -> dict:
    store.delete_intent(request["intentName"], request["botId"], request["botVersion"], request["localeId"])
    return {}
