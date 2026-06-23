def handler(store, r): return store.describe_entity(r["EntityRecognizerArn"]).to_dict()
