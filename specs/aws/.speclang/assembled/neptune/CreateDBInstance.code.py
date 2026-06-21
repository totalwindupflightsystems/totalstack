"""CreateDBInstance handler for Neptune."""


def create_db_instance(store, request):
    """Create a new Neptune DB instance."""
    identifier = request.get('DBInstanceIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBInstanceIdentifier is required")

    instance_class = request.get('DBInstanceClass', '').strip()
    if not instance_class:
        raise InvalidParameterValueException("DBInstanceClass is required")
    valid_classes = [
        'db.r5.large', 'db.r5.xlarge', 'db.r5.2xlarge', 'db.r5.4xlarge',
        'db.r5.8xlarge', 'db.r5.12xlarge', 'db.r5.16xlarge', 'db.r5.24xlarge',
        'db.r4.large', 'db.r4.xlarge', 'db.r4.2xlarge', 'db.r4.4xlarge',
        'db.r4.8xlarge', 'db.t3.medium', 'db.t4g.medium',
        'db.r6g.large', 'db.r6g.xlarge', 'db.r6g.2xlarge', 'db.r6g.4xlarge',
        'db.r6g.8xlarge', 'db.r6g.12xlarge', 'db.r6g.16xlarge',
        'db.x2g.8xlarge', 'db.x2g.12xlarge', 'db.x2g.16xlarge',
    ]
    # Accept class with or without 'db.' prefix
    if instance_class not in valid_classes and f'db.{instance_class}' not in valid_classes:
        if not any(instance_class.startswith(p) for p in ['db.r', 'db.t', 'db.x']):
            raise InvalidParameterValueException(
                f"Invalid DBInstanceClass: {instance_class}")

    engine = request.get('Engine', 'neptune').strip()
    if engine != 'neptune':
        raise InvalidParameterValueException("Engine must be 'neptune'")

    cluster_id = request.get('DBClusterIdentifier', '').strip()
    if not cluster_id:
        raise InvalidParameterValueException("DBClusterIdentifier is required")

    instance = store.create_instance(
        identifier,
        instance_class,
        engine,
        cluster_id,
        availability_zone=request.get('AvailabilityZone', ''),
        db_parameter_group=request.get('DBParameterGroupName', ''),
        engine_version=request.get('EngineVersion', ''),
        auto_minor_version_upgrade=request.get('AutoMinorVersionUpgrade', True),
        monitoring_interval=request.get('MonitoringInterval', 0),
        monitoring_role_arn=request.get('MonitoringRoleArn', ''),
        promotion_tier=request.get('PromotionTier', 1),
        publicly_accessible=request.get('PubliclyAccessible', False),
        tags=request.get('Tags', []),
        status='available',
    )
    return {'DBInstance': instance.to_dict()}
