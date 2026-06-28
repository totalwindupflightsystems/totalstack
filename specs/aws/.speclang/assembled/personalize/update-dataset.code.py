def handler(store, r): store.update_dataset(r["datasetArn"], schemaArn=r.get("schemaArn"), **{k:v for k,v in r.items() if k not in ("datasetArn","schemaArn")}); return {}
