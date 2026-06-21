def handler(store, request):
    resource_arn = request.get("ResourceArn")
    action = request.get("Action")
    return store.enable_application_layer_automatic_response(resource_arn=resource_arn, action=action)
