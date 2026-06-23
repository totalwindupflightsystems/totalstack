def handler(store, r): return store.detect_syntax(r["Text"], r.get("LanguageCode", "en"))
