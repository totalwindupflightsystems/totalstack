def handler(store, request: dict) -> dict:
    return store.recognize_text(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"],
        text=request["text"],
        sessionState=request.get("sessionState"),
        requestAttributes=request.get("requestAttributes"))

