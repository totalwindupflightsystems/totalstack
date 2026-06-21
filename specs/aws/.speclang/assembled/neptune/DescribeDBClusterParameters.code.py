"""DescribeDBClusterParameters handler for Neptune."""


def describe_db_cluster_parameters(store, request):
    """Describe parameters for a DB cluster parameter group."""
    name = request.get('DBClusterParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBClusterParameterGroupName is required")

    # Verify group exists
    store.get_cluster_param_group(name)

    # Return default parameters for Neptune family
    source = request.get('Source', 'user')
    return {
        'Parameters': [
            {
                'ParameterName': 'neptune_query_timeout',
                'ParameterValue': '120000',
                'Description': 'Graph query timeout in ms',
                'Source': source,
                'ApplyType': 'dynamic',
                'DataType': 'integer',
                'AllowedValues': '0-2147483647',
                'IsModifiable': True,
                'ApplyMethod': 'pending-reboot',
            },
            {
                'ParameterName': 'neptune_enable_audit_log',
                'ParameterValue': '0',
                'Description': 'Enable audit logging',
                'Source': source,
                'ApplyType': 'dynamic',
                'DataType': 'boolean',
                'AllowedValues': '0,1',
                'IsModifiable': True,
                'ApplyMethod': 'pending-reboot',
            },
            {
                'ParameterName': 'neptune_lab_mode',
                'ParameterValue': '',
                'Description': 'Enable lab mode features',
                'Source': source,
                'ApplyType': 'dynamic',
                'DataType': 'string',
                'AllowedValues': '',
                'IsModifiable': True,
                'ApplyMethod': 'pending-reboot',
            },
        ],
    }
