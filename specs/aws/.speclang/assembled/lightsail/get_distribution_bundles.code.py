# spec:trace: aws/lightsail/get_distribution_bundles.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-distribution-bundles
# spec:generated: DO NOT EDIT — edit the spec instead

def get_distribution_bundles(store, request: dict) -> dict:
    """Returns the bundles that can be applied to your Amazon Lightsail content delivery network (CDN) distributions. A distribution bundle specifies the monthly network transfer quota and monthly cost of yo"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

