def handler(store, r):
    rec = store.create_entity(r["DatasetArn"], r.get("DatasetName", "ds"), "dataset")
    return {"DatasetArn": rec.arn}
