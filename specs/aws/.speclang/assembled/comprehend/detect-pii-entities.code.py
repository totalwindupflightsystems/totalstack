def handler(store, r): return store.detect_pii_entities(r["Text"], r.get("LanguageCode", "en"))
