"""ModifyDBInstance handler for Neptune."""


def modify_db_instance(store, request):
    """Modify a Neptune DB instance."""
    identifier = request.get('DBInstanceIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBInstanceIdentifier is required")

    instance = store.modify_instance(
        identifier,
        db_instance_class=request.get('DBInstanceClass'),
        db_parameter_group=request.get('DBParameterGroupName'),
        auto_minor_version_upgrade=request.get('AutoMinorVersionUpgrade'),
        monitoring_interval=request.get('MonitoringInterval'),
        monitoring_role_arn=request.get('MonitoringRoleArn'),
        promotion_tier=request.get('PromotionTier'),
        publicly_accessible=request.get('PubliclyAccessible'),
    )
    return {'DBInstance': instance.to_dict()}
