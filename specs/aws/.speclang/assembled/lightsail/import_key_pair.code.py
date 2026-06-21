# spec:trace: aws/lightsail/import_key_pair.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/import-key-pair
# spec:generated: DO NOT EDIT — edit the spec instead

def import_key_pair(store, request: dict) -> dict:
    """Imports a public SSH key from a specific key pair."""
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")
    public_key_base64 = request.get("publicKeyBase64", "").strip() if isinstance(request.get("publicKeyBase64"), str) else request.get("publicKeyBase64")
    if not public_key_base64:
        raise ValidationException("publicKeyBase64 is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportKeyPair", request)

