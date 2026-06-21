def handler(store, request: dict) -> dict:
    identifier = request["DBInstanceIdentifier"]
    return store.create_instance(
        identifier,
        Engine=request.get("Engine", "mysql"),
        DBInstanceClass=request.get("DBInstanceClass", "db.t3.micro"),
        AllocatedStorage=request.get("AllocatedStorage", 20),
        MasterUsername=request.get("MasterUsername", "admin"),
        MasterUserPassword=request.get("MasterUserPassword", ""),
    )
