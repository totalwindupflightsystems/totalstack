def handler(store, request: dict) -> dict:
    record = store.create_security_configuration(
        request["Name"], request["SecurityConfiguration"])
    return {"Name": record.Name, "CreationDateTime": record.CreationDateTime}
