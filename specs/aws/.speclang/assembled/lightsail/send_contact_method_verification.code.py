# spec:trace: aws/lightsail/send_contact_method_verification.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/send-contact-method-verification
# spec:generated: DO NOT EDIT — edit the spec instead

def send_contact_method_verification(store, request: dict) -> dict:
    """Sends a verification request to an email contact method to ensure it's owned by the requester. SMS contact methods don't need to be verified. A contact method is used to send you notifications about y"""
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")
    if not protocol:
        raise ValidationException("protocol is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendContactMethodVerification", request)

