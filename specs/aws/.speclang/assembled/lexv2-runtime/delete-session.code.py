def handler(store, request: dict) -> dict:
    return store.delete_session(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"])

