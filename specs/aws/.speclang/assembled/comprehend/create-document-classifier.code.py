def handler(store, r):
    rec = store.create_entity(r["DocumentClassifierArn"], r.get("DocumentClassifierName", "clf"), "document-classifier", LanguageCode=r.get("LanguageCode", "en"))
    return {"DocumentClassifierArn": rec.arn}
