def handler(store, request: dict):
    return store.create_instance(request["DBInstanceIdentifier"], request["DBClusterIdentifier"], request["DBInstanceClass"], request["Engine"], **{k: v for k, v in request.items() if k not in ("DBInstanceIdentifier", "DBClusterIdentifier", "DBInstanceClass", "Engine")})
