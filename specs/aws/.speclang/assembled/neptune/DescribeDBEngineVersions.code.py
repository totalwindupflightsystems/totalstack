"""DescribeDBEngineVersions handler for Neptune."""


def describe_db_engine_versions(store, request):
    """Describe available DB engine versions."""
    engine_version = request.get('EngineVersion', '').strip()
    db_parameter_group_family = request.get('DBParameterGroupFamily', '').strip()

    versions = [
        {
            'Engine': 'neptune',
            'EngineVersion': '1.3.3.0',
            'DBParameterGroupFamily': 'neptune1.3',
            'EngineDescription': 'Amazon Neptune',
            'ValidUpgradeTarget': [
                {'Engine': 'neptune', 'EngineVersion': '1.4.0.0',
                 'Description': 'Neptune 1.4.0.0', 'AutoUpgrade': False, 'IsMajorVersionUpgrade': True},
            ],
            'SupportedEngineModes': ['serverless'],
        },
        {
            'Engine': 'neptune',
            'EngineVersion': '1.4.0.0',
            'DBParameterGroupFamily': 'neptune1.4',
            'EngineDescription': 'Amazon Neptune',
            'ValidUpgradeTarget': [],
            'SupportedEngineModes': ['serverless'],
        },
    ]

    if engine_version:
        versions = [v for v in versions if v['EngineVersion'] == engine_version]
    if db_parameter_group_family:
        versions = [v for v in versions if v['DBParameterGroupFamily'] == db_parameter_group_family]

    return {'DBEngineVersions': versions}
