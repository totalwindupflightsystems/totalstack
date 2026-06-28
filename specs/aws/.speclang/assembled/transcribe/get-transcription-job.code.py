def handler(store, request: dict) -> dict:
    return store.get_transcription_job(request["TranscriptionJobName"])

