
def get_encryption_config(store, request):
    config = store.encryption_config or {'Type': 'NONE', 'KeyId': ''}
    return {'EncryptionConfig': config}
