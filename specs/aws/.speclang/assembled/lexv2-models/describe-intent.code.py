def describe_intent(store, request: dict) -> dict:
    return store.describe_intent(request["intentName"], request["botId"], request["botVersion"], request["localeId"])
