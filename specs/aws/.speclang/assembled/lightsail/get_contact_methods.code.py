# spec:trace: aws/lightsail/get_contact_methods.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-contact-methods
# spec:generated: DO NOT EDIT — edit the spec instead

def get_contact_methods(store, request: dict) -> dict:
    """Returns information about the configured contact methods. Specify a protocol in your request to return information about a specific contact method. A contact method is used to send you notifications a"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

