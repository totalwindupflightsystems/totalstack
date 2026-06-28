def list_bot_aliases(store, request: dict) -> dict:
    aliases = store.list_bot_aliases(request["botId"])
    return {"botAliasSummaries": aliases}
