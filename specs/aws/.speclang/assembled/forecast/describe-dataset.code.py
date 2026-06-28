def handler(store, request: dict) -> dict:
    r = store.datasets(request["DatasetArn"])
    if not r:
        raise ResourceNotFoundException(f"Dataset {request['DatasetArn']} not found")
    return r.to_dict()
