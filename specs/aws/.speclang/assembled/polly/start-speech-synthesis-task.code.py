def handler(store, request: dict) -> dict:
    return store.start_speech_synthesis_task(
        OutputFormat=request["OutputFormat"],
        OutputS3BucketName=request["OutputS3BucketName"],
        Text=request["Text"],
        VoiceId=request["VoiceId"],
        Engine=request.get("Engine"),
        LanguageCode=request.get("LanguageCode"),
        LexiconNames=request.get("LexiconNames"),
        OutputS3KeyPrefix=request.get("OutputS3KeyPrefix"),
        SampleRate=request.get("SampleRate"),
        SnsTopicArn=request.get("SnsTopicArn"),
        SpeechMarkTypes=request.get("SpeechMarkTypes"),
        TextType=request.get("TextType"))

