# spec:trace: aws/lightsail/get_relational_database_blueprints.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-blueprints
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_blueprints(store, request: dict) -> dict:
    """Returns a list of available database blueprints in Amazon Lightsail. A blueprint describes the major engine version of a database. You can use a blueprint ID to create a new database that runs a speci"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

