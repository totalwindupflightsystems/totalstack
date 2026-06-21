# spec:trace: aws/lightsail/create_contact_method.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-contact-method
# spec:generated: DO NOT EDIT — edit the spec instead

def create_contact_method(store, request: dict) -> dict:
    """Creates an email or SMS text message contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number"""
    contact_endpoint = request.get("contactEndpoint", "").strip() if isinstance(request.get("contactEndpoint"), str) else request.get("contactEndpoint")
    if not contact_endpoint:
        raise ValidationException("contactEndpoint is required")
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")
    if not protocol:
        raise ValidationException("protocol is required")

    if store.contact_methods(contact_endpoint):
        raise ResourceInUseException("Resource contact_endpoint already exists")

    record = {
        "protocol": protocol,
        "contactEndpoint": contact_endpoint,
    }

    store.contact_methods(contact_endpoint, record)

    return {
        "operations": record.get("operations", {}),
    }

