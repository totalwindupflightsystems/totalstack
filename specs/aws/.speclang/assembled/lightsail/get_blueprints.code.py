# spec:trace: aws/lightsail/get_blueprints.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-blueprints
# spec:generated: DO NOT EDIT — edit the spec instead

def get_blueprints(store, request: dict) -> dict:
    """Returns the list of available instance images, or blueprints . You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or developmen"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

