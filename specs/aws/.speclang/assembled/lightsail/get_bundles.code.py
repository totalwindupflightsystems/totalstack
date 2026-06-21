# spec:trace: aws/lightsail/get_bundles.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-bundles
# spec:generated: DO NOT EDIT — edit the spec instead

def get_bundles(store, request: dict) -> dict:
    """Returns the bundles that you can apply to an Amazon Lightsail instance when you create it. A bundle describes the specifications of an instance, such as the monthly cost, amount of memory, the number """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

