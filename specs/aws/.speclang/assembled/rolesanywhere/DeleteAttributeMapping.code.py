def handler(store, request):
    store.delete_attribute_mapping(request["profileId"], request["certificateField"])
    return {}
