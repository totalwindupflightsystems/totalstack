# spec:trace: aws/lightsail/create_gui_session_access_details.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-gui-session-access-details
# spec:generated: DO NOT EDIT — edit the spec instead

def create_gui_session_access_details(store, request: dict) -> dict:
    """Creates two URLs that are used to access a virtual computer’s graphical user interface (GUI) session. The primary URL initiates a web-based Amazon DCV session to the virtual computer's application. Th"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.gui_session_access_detailss(resource_name):
        raise ResourceInUseException("Resource resource_name already exists")

    record = {
        "resourceName": resource_name,
    }

    store.gui_session_access_detailss(resource_name, record)

    return {
        "resourceName": resource_name,
        "status": record.get("status", {}),
        "percentageComplete": record.get("percentageComplete", {}),
        "failureReason": record.get("failureReason", {}),
        "sessions": record.get("sessions", {}),
    }

