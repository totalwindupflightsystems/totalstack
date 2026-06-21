"""DescribeDBParameters handler for Neptune."""


def describe_db_parameters(store, request):
    """Describe parameters for a DB parameter group."""
    name = request.get('DBParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBParameterGroupName is required")

    # Verify group exists
    store.get_param_group(name)

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
        ],
    }
