
def update_indexing_rule(store, request):
    name = request.get('Name', '')
    rule = request.get('Rule', {})
    if not name or not rule:
        raise InvalidRequestException('Name and Rule are required')
    if name not in store.indexing_rules:
        raise InvalidRequestException(f'Indexing rule not found')
    store.indexing_rules[name].update(rule)
    return {'IndexingRule': store.indexing_rules[name]}
