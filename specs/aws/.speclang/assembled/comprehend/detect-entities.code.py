def handler(store, r): return store.detect_entities(r["Text"], r.get("LanguageCode", "en"))
