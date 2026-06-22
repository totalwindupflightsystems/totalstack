
def update_sampling_rule(store, request):
    update = request.get('SamplingRuleUpdate')
    if not update:
        raise InvalidRequestException('SamplingRuleUpdate is required')
    rule_name = update.get('RuleName')
    if not rule_name:
        raise InvalidRequestException('RuleName is required in SamplingRuleUpdate')
    if rule_name not in store.sampling_rules:
        raise InvalidRequestException(f'Sampling rule not found')
    rule = store.sampling_rules[rule_name]
    updatable = ['ResourceARN', 'Priority', 'FixedRate', 'ReservoirSize', 'ServiceName',
                 'ServiceType', 'Host', 'HTTPMethod', 'URLPath', 'Attributes']
    for key in updatable:
        if key in update:
            rule[key] = update[key]
    rule['Version'] = rule.get('Version', 1) + 1
    store.sampling_rules[rule_name] = rule
    return {'SamplingRuleRecord': {'SamplingRule': dict(rule), 'CreatedAt': '2024-01-01T00:00:00Z', 'ModifiedAt': '2024-01-01T00:00:00Z'}}
