# spec:trace: aws/lightsail/get_relational_databases.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-databases
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_databases(store, request: dict) -> dict:
    """Returns information about all of your databases in Amazon Lightsail."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

