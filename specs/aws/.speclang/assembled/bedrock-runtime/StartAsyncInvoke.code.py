def handler(store, request: dict) -> dict:
    """Start a new async model invocation job."""
    modelId = request["modelId"]
    modelInput = request["modelInput"]
    outputDataConfig = request["outputDataConfig"]
    clientRequestToken = request.get("clientRequestToken")
    tags = request.get("tags")
    return store.start_async_invoke(modelId, modelInput, outputDataConfig,
                                    clientRequestToken=clientRequestToken,
                                    tags=tags)
