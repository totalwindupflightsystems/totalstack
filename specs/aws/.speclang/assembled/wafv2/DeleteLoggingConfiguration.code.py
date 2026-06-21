"""Handler for DeleteLoggingConfiguration — AWS WAFv2."""
def handler(store, request):
    return store.delete_logging_configuration(request["ResourceArn"])
