def handler(store, r): return store.detect_key_phrases(r["Text"], r.get("LanguageCode", "en"))
