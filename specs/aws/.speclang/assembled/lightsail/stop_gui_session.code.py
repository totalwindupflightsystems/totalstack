# spec:trace: aws/lightsail/stop_gui_session.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/stop-gui-session
# spec:generated: DO NOT EDIT — edit the spec instead

def stop_gui_session(store, request: dict) -> dict:
    """Terminates a web-based Amazon DCV session that’s used to access a virtual computer’s operating system or application. The session will close and any unsaved data will be lost."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")

    if not store.gui_sessions(resource_name):
        raise ResourceNotFoundException("Resource resource_name not found")
    store.delete_gui_sessions(resource_name)
    return {}

