def handler(store, r): return store.classify_document(r["Text"], r["EndpointArn"])
