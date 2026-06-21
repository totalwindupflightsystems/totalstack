# spec:trace: aws/lightsail/get_relational_database_bundles.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-bundles
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_bundles(store, request: dict) -> dict:
    """Returns the list of bundles that are available in Amazon Lightsail. A bundle describes the performance specifications for a database. You can use a bundle ID to create a new database with explicit per"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

