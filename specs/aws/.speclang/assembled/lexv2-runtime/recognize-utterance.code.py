def handler(store, request: dict) -> dict:
    return store.recognize_utterance(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"],
        inputStream=request.get("inputStream"),
        requestAttributes=request.get("requestAttributes"),
        sessionState=request.get("sessionState"),
        responseContentType=request.get("responseContentType"))

