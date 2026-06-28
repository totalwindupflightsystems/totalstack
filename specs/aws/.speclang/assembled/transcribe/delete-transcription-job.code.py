def handler(store, request: dict) -> dict:
    return store.delete_transcription_job(request["TranscriptionJobName"])

