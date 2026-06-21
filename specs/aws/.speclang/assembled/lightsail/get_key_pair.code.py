# spec:trace: aws/lightsail/get_key_pair.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-key-pair
# spec:generated: DO NOT EDIT — edit the spec instead

def get_key_pair(store, request: dict) -> dict:
    """Returns information about a specific key pair."""
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")

    resource = store.key_pairs(key_pair_name)
    if not resource:
        raise ResourceNotFoundException("Resource key_pair_name not found")
    return {"keyPairName": key_pair_name, **resource}

