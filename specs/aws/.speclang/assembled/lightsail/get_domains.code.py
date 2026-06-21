# spec:trace: aws/lightsail/get_domains.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-domains
# spec:generated: DO NOT EDIT — edit the spec instead

def get_domains(store, request: dict) -> dict:
    """Returns a list of all domains in the user's account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

