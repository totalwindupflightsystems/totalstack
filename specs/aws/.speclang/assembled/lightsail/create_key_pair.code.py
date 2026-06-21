# spec:trace: aws/lightsail/create_key_pair.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-key-pair
# spec:generated: DO NOT EDIT — edit the spec instead

def create_key_pair(store, request: dict) -> dict:
    """Creates a custom SSH key pair that you can use with an Amazon Lightsail instance. Use the DownloadDefaultKeyPair action to create a Lightsail default key pair in an Amazon Web Services Region where a """
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")

    if store.key_pairs(key_pair_name):
        raise ResourceInUseException("Resource key_pair_name already exists")

    tags = request.get("tags", [])

    record = {
        "keyPairName": key_pair_name,
        "tags": tags,
    }

    store.key_pairs(key_pair_name, record)

    return {
        "keyPair": record.get("keyPair", {}),
        "publicKeyBase64": record.get("publicKeyBase64", {}),
        "privateKeyBase64": record.get("privateKeyBase64", {}),
        "operation": record.get("operation", {}),
    }

