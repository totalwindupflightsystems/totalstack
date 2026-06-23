def handler(store, r): return store.detect_sentiment(r["Text"], r.get("LanguageCode", "en"))
