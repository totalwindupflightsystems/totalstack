
def put_encryption_config(store, request):
    enc_type = request.get('Type', '')
    if not enc_type:
        raise InvalidRequestException('Type is required')
    key_id = request.get('KeyId', '')
    store.encryption_config = {'Type': enc_type, 'KeyId': key_id}
    return {'EncryptionConfig': dict(store.encryption_config)}
