# spec:trace: aws/lightsail/delete_contact_method.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-contact-method
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_contact_method(store, request: dict) -> dict:
    """Deletes a contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Ama"""
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")

    if not store.contact_methods(protocol):
        raise ResourceNotFoundException("Resource protocol not found")
    store.delete_contact_methods(protocol)
    return {}

