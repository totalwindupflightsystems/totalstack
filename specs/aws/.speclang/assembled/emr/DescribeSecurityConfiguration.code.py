def handler(store, request: dict) -> dict:
    record = store.describe_security_configuration(request["Name"])
    return {"Name": record.Name, "SecurityConfiguration": record.SecurityConfiguration,
            "CreationDateTime": record.CreationDateTime}
