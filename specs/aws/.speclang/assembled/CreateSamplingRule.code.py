
def create_sampling_rule(store, request):
    rule_input = request.get('SamplingRule')
    if not rule_input:
        raise InvalidRequestException('SamplingRule is required')
    rule_name = rule_input.get('RuleName')
    if not rule_name:
        raise InvalidRequestException('RuleName is required in SamplingRule')
    if rule_name in store.sampling_rules:
        raise InvalidRequestException(f'Sampling rule {rule_name} already exists')
    rule = {
        'RuleName': rule_name,
        'RuleARN': f'arn:aws:xray:us-east-1:000000000000:sampling-rule/{rule_name}',
        'ResourceARN': rule_input.get('ResourceARN', '*'),
        'Priority': rule_input.get('Priority', 1),
        'FixedRate': rule_input.get('FixedRate', 0.05),
        'ReservoirSize': rule_input.get('ReservoirSize', 1),
        'ServiceName': rule_input.get('ServiceName', '*'),
        'ServiceType': rule_input.get('ServiceType', '*'),
        'Host': rule_input.get('Host', '*'),
        'HTTPMethod': rule_input.get('HTTPMethod', '*'),
        'URLPath': rule_input.get('URLPath', '*'),
        'Version': 1,
        'Attributes': rule_input.get('Attributes', {}),
    }
    tags = request.get('Tags', [])
    if tags:
        arn = rule['RuleARN']
        store.tags[arn] = {t['Key']: t['Value'] for t in tags}
    store.sampling_rules[rule_name] = rule
    result = {'SamplingRuleRecord': {'SamplingRule': dict(rule), 'CreatedAt': '2024-01-01T00:00:00Z', 'ModifiedAt': '2024-01-01T00:00:00Z'}}
    return result
