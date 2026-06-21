# spec:trace: aws/lightsail/delete_key_pair.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-key-pair
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_key_pair(store, request: dict) -> dict:
    """Deletes the specified key pair by removing the public key from Amazon Lightsail. You can delete key pairs that were created using the ImportKeyPair and CreateKeyPair actions, as well as the Lightsail """
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")

    if not store.key_pairs(key_pair_name):
        raise ResourceNotFoundException("Resource key_pair_name not found")
    store.delete_key_pairs(key_pair_name)
    return {}

