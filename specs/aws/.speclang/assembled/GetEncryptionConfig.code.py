// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetEncryptionConfig.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_encryption_config(store, request):
    config = store.encryption_config or {'Type': 'NONE', 'KeyId': ''}
    return {'EncryptionConfig': config}