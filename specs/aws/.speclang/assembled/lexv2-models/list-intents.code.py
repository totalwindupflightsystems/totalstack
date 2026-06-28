def list_intents(store, request: dict) -> dict:
    intents = store.list_intents(request["botId"], request["botVersion"], request["localeId"])
    return {"intentSummaries": intents}
