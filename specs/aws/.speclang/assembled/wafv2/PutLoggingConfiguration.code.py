"""Handler for PutLoggingConfiguration — AWS WAFv2."""
def handler(store, request):
    logging_config = request.get("LoggingConfiguration")
    if not logging_config:
        raise WAFInvalidParameterException("LoggingConfiguration is required")
    if not logging_config.get("ResourceArn"):
        raise WAFInvalidParameterException("ResourceArn is required in LoggingConfiguration")
    return store.put_logging_configuration(logging_config)
