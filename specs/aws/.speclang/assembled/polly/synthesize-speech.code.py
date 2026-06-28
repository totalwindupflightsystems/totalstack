def handler(store, request: dict) -> dict:
    return store.synthesize_speech(
        OutputFormat=request["OutputFormat"],
        Text=request["Text"],
        VoiceId=request["VoiceId"],
        Engine=request.get("Engine"),
        LanguageCode=request.get("LanguageCode"),
        LexiconNames=request.get("LexiconNames"),
        SampleRate=request.get("SampleRate"),
        SpeechMarkTypes=request.get("SpeechMarkTypes"),
        TextType=request.get("TextType"))

