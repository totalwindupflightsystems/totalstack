def handler(store, request: dict) -> dict:
    return store.get_speech_synthesis_task(request["TaskId"])

