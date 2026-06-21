def handler(store, request: dict) -> dict:
    """ModifyDBInstance handler."""
    kwargs = {}
    for key in ("DBInstanceClass", "AllocatedStorage", "DBParameterGroupName",
                "BackupRetentionPeriod", "PreferredBackupWindow",
                "PreferredMaintenanceWindow", "MultiAZ", "EngineVersion",
                "AllowMajorVersionUpgrade", "AutoMinorVersionUpgrade",
                "Iops", "OptionGroupName", "NewDBInstanceIdentifier",
                "StorageType", "CopyTagsToSnapshot", "MonitoringInterval",
                "MonitoringRoleArn", "PubliclyAccessible",
                "VpcSecurityGroupIds", "MasterUserPassword",
                "ApplyImmediately"):
        if key in request:
            kwargs[key.lower()] = request[key]
    return store.modify_db_instance(
        db_instance_identifier=request["DBInstanceIdentifier"], **kwargs)
