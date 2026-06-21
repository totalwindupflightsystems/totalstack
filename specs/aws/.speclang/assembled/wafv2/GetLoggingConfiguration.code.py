"""Handler for GetLoggingConfiguration — AWS WAFv2."""
def handler(store, request):
    return store.get_logging_configuration(request["ResourceArn"])
