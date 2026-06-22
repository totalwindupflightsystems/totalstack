
def delete_sampling_rule(store, request):
    rule_name = request.get('RuleName', '')
    rule_arn = request.get('RuleARN', '')
    if not rule_name and not rule_arn:
        raise InvalidRequestException('RuleName or RuleARN is required')
    if rule_arn:
        rule = next((r for r in store.sampling_rules.values() if r.get('RuleARN') == rule_arn), None)
        if rule:
            rule_name = rule['RuleName']
    if rule_name not in store.sampling_rules:
        raise InvalidRequestException(f'Sampling rule not found')
    rule = store.sampling_rules.pop(rule_name)
    store.tags.pop(rule.get('RuleARN', ''), None)
    return {}
