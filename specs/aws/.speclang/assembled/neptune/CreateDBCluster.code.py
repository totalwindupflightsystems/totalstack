"""CreateDBCluster handler for Neptune."""


def create_db_cluster(store, request):
    """Create a new Neptune DB cluster."""
    identifier = request.get('DBClusterIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBClusterIdentifier is required")
    if len(identifier) < 1 or len(identifier) > 63:
        raise InvalidParameterValueException(
            "DBClusterIdentifier must be between 1 and 63 characters")

    engine = request.get('Engine', 'neptune').strip()
    if engine != 'neptune':
        raise InvalidParameterValueException("Engine must be 'neptune' for Neptune clusters")

    # Required cross-field: if no DBSubnetGroupName and no VpcSecurityGroupIds,
    # need to use default
    cluster = store.create_cluster(
        identifier,
        engine,
        database_name=request.get('DatabaseName', ''),
        availability_zones=request.get('AvailabilityZones', []),
        backup_retention_period=request.get('BackupRetentionPeriod', 1),
        character_set_name=request.get('CharacterSetName', ''),
        db_cluster_parameter_group=request.get('DBClusterParameterGroupName', ''),
        db_subnet_group=request.get('DBSubnetGroupName', ''),
        deletion_protection=request.get('DeletionProtection', False),
        enable_cloudwatch_logs_exports=request.get('EnableCloudwatchLogsExports', []),
        engine_version=request.get('EngineVersion', ''),
        kms_key_id=request.get('KmsKeyId', ''),
        master_username=request.get('MasterUsername', ''),
        master_user_password=request.get('MasterUserPassword', ''),
        port=request.get('Port', 8182),
        preferred_backup_window=request.get('PreferredBackupWindow', ''),
        preferred_maintenance_window=request.get('PreferredMaintenanceWindow', ''),
        replication_source_identifier=request.get('ReplicationSourceIdentifier', ''),
        storage_encrypted=request.get('StorageEncrypted', False),
        copy_tags_to_snapshot=request.get('CopyTagsToSnapshot', False),
        iam_database_authentication_enabled=request.get(
            'EnableIAMDatabaseAuthentication', False),
        vpc_security_group_ids=request.get('VpcSecurityGroupIds', []),
        tags=request.get('Tags', []),
        status='available',
    )
    return {'DBCluster': cluster.to_dict()}
