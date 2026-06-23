def handler(store, r): return store.contains_pii_entities(r["Text"], r.get("LanguageCode", "en"))
