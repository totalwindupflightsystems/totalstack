# spec:trace: aws/lightsail/download_default_key_pair.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/download-default-key-pair
# spec:generated: DO NOT EDIT — edit the spec instead

def download_default_key_pair(store, request: dict) -> dict:
    """Downloads the regional Amazon Lightsail default key pair. This action also creates a Lightsail default key pair if a default key pair does not currently exist in the Amazon Web Services Region."""


    record = {
        "publicKeyBase64": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl totalstack-default-key",
        "privateKeyBase64": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA totalstack-default-key\n-----END RSA PRIVATE KEY-----",
        "createdAt": 1735689600,
    }

    store.download_default_key_pairs(record)

    return record

