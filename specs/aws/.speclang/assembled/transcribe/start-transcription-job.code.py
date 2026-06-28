def handler(store, request: dict) -> dict:
    return store.start_transcription_job(
        TranscriptionJobName=request["TranscriptionJobName"],
        Media=request["Media"],
        LanguageCode=request.get("LanguageCode"),
        OutputBucketName=request.get("OutputBucketName"),
        OutputKey=request.get("OutputKey"),
        MediaFormat=request.get("MediaFormat"),
        MediaSampleRateHertz=request.get("MediaSampleRateHertz"),
        Settings=request.get("Settings"),
        Tags=request.get("Tags"))

