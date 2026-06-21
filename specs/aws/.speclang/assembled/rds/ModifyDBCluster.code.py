def handler(store, request: dict) -> dict:
    """ModifyDBCluster handler."""
    kwargs = {}
    for key in ("DBClusterParameterGroupName", "BackupRetentionPeriod",
                "PreferredBackupWindow", "PreferredMaintenanceWindow",
                "EngineVersion", "AllowMajorVersionUpgrade",
                "MasterUserPassword", "NewDBClusterIdentifier",
                "StorageEncrypted", "ApplyImmediately", "Port",
                "VpcSecurityGroupIds"):
        if key in request:
            kwargs[key.lower()] = request[key]
    return store.modify_db_cluster(
        db_cluster_identifier=request["DBClusterIdentifier"], **kwargs)
