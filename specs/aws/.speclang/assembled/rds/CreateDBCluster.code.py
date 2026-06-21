def handler(store, request: dict) -> dict:
    """CreateDBCluster handler."""
    return store.create_db_cluster(
        db_cluster_identifier=request["DBClusterIdentifier"],
        engine=request["Engine"],
        db_cluster_parameter_group_name=request.get("DBClusterParameterGroupName"),
        vpc_security_group_ids=request.get("VpcSecurityGroupIds"),
        db_subnet_group_name=request.get("DBSubnetGroupName"),
        database_name=request.get("DatabaseName"),
        master_username=request.get("MasterUsername"),
        master_user_password=request.get("MasterUserPassword"),
        port=request.get("Port"),
        engine_version=request.get("EngineVersion"),
        backup_retention_period=request.get("BackupRetentionPeriod"),
        preferred_backup_window=request.get("PreferredBackupWindow"),
        preferred_maintenance_window=request.get("PreferredMaintenanceWindow"),
        storage_encrypted=request.get("StorageEncrypted", False),
        kms_key_id=request.get("KmsKeyId"),
        tags=request.get("Tags"),
    )
