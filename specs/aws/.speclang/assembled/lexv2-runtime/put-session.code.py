def handler(store, request: dict) -> dict:
    return store.put_session(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"],
        sessionState=request.get("sessionState"),
        messages=request.get("messages"),
        requestAttributes=request.get("requestAttributes"),
        responseContentType=request.get("responseContentType"))

