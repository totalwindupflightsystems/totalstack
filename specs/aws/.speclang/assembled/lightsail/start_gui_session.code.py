# spec:trace: aws/lightsail/start_gui_session.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/start-gui-session
# spec:generated: DO NOT EDIT — edit the spec instead

def start_gui_session(store, request: dict) -> dict:
    """Initiates a graphical user interface (GUI) session that’s used to access a virtual computer’s operating system and application. The session will be active for 1 hour. Use this action to resume the ses"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.gui_sessions(resource_name):
        raise ResourceInUseException("Resource resource_name already exists")

    record = {
        "resourceName": resource_name,
    }

    store.gui_sessions(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }

