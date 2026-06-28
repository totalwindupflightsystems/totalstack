def handler(store, request):
    result = store.put_attribute_mapping(
        request["profileId"],
        request["certificateField"],
        request.get("mappingRules", []),
    )
    return result
