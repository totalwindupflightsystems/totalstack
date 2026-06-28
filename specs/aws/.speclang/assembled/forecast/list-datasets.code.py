def handler(store, request: dict) -> dict:
    datasets = store.datasets()
    items = [{"DatasetArn": d.DatasetArn, "DatasetName": d.DatasetName,
              "Domain": d.Domain, "DatasetType": d.DatasetType,
              "CreationTime": d.CreationTime} for d in datasets]
    return {"Datasets": items, "NextToken": ""}
