def handler(store, request):
    resource_arn = request.get("ResourceArn")
    return store.disable_application_layer_automatic_response(resource_arn=resource_arn)
