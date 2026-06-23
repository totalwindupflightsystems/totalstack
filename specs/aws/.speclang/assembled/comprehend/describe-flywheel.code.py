def handler(store, r): return store.describe_entity(r["FlywheelArn"]).to_dict()
