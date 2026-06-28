def handler(store, request: dict) -> dict:
    return store.get_session(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"])

