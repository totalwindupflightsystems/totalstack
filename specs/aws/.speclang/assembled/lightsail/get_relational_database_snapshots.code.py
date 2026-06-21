# spec:trace: aws/lightsail/get_relational_database_snapshots.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-snapshots
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_snapshots(store, request: dict) -> dict:
    """Returns information about all of your database snapshots in Amazon Lightsail."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

