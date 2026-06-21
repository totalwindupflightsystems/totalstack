"""ModifyDBCluster handler for Neptune."""


def modify_db_cluster(store, request):
    """Modify a Neptune DB cluster."""
    identifier = request.get('DBClusterIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBClusterIdentifier is required")

    cluster = store.modify_cluster(
        identifier,
        backup_retention_period=request.get('BackupRetentionPeriod'),
        db_cluster_parameter_group=request.get('DBClusterParameterGroupName'),
        deletion_protection=request.get('DeletionProtection'),
        enable_cloudwatch_logs_exports=request.get('CloudwatchLogsExportConfiguration'),
        engine_version=request.get('EngineVersion'),
        master_user_password=request.get('MasterUserPassword'),
        port=request.get('Port'),
        preferred_backup_window=request.get('PreferredBackupWindow'),
        preferred_maintenance_window=request.get('PreferredMaintenanceWindow'),
        vpc_security_group_ids=request.get('VpcSecurityGroupIds'),
        copy_tags_to_snapshot=request.get('CopyTagsToSnapshot'),
        iam_database_authentication_enabled=request.get('EnableIAMDatabaseAuthentication'),
    )
    return {'DBCluster': cluster.to_dict()}
