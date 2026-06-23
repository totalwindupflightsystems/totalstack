def handler(store, r):
    rec = store.create_entity(r["EntityRecognizerArn"], r.get("RecognizerName", "er"), "entity-recognizer", LanguageCode=r.get("LanguageCode", "en"))
    return {"EntityRecognizerArn": rec.arn}
