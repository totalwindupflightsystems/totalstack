# spec:trace: aws/lightsail/update_instance_metadata_options.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-instance-metadata-options
# spec:generated: DO NOT EDIT — edit the spec instead

def update_instance_metadata_options(store, request: dict) -> dict:
    """Modifies the Amazon Lightsail instance metadata parameters on a running or stopped instance. When you modify the parameters on a running instance, the GetInstance or GetInstances API operation initial"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_metadata_optionss(instance_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_name not found")

    # Update mutable fields
    if "httpTokens" in request:
        resource["httpTokens"] = http_tokens
    if "httpEndpoint" in request:
        resource["httpEndpoint"] = http_endpoint
    if "httpPutResponseHopLimit" in request:
        resource["httpPutResponseHopLimit"] = http_put_response_hop_limit
    if "httpProtocolIpv6" in request:
        resource["httpProtocolIpv6"] = http_protocol_ipv6

    store.instance_metadata_optionss(instance_name, resource)
    return resource

