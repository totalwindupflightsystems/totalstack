def handler(store, r): return store.detect_targeted_sentiment(r["Text"], r.get("LanguageCode", "en"))
