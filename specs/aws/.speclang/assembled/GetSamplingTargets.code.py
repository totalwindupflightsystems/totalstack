// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetSamplingTargets.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_sampling_targets(store, request):
    docs = request.get('SamplingStatisticsDocuments', [])
    targets = []
    for doc in docs:
        rule_name = doc.get('RuleName', '')
        rule = store.sampling_rules.get(rule_name)
        if rule:
            targets.append({
                'RuleName': rule_name,
                'FixedRate': rule.get('FixedRate', 0.05),
                'ReservoirQuota': rule.get('ReservoirSize', 1),
                'ReservoirQuotaTTL': '2024-12-31T23:59:59Z',
                'Interval': 10,
            })
    unprocessed = [doc['RuleName'] for doc in docs if doc.get('RuleName') not in store.sampling_rules]
    result = {'SamplingTargetDocuments': targets}
    if unprocessed:
        result['UnprocessedStatistics'] = [{'RuleName': n, 'ErrorCode': 'RuleNotFound', 'Message': 'Unknown rule'} for n in unprocessed]
    result['LastRuleModification'] = '2024-01-01T00:00:00Z'
    return result