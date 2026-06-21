"""CreateAccount handler."""


def handle_create_account(store, request: dict) -> dict:
    email = request.get("Email", "")
    name = request.get("AccountName", "")

    if not email:
        raise InvalidInputException("Email is required")
    if not name:
        raise InvalidInputException("AccountName is required")
    if "@" not in email:
        raise InvalidInputException("Invalid email address")
    if len(name) < 1 or len(name) > 50:
        raise InvalidInputException("AccountName must be between 1 and 50 characters")

    role_name = request.get("RoleName")
    iam_access = request.get("IamUserAccessToBilling", "ALLOW")
    tags = request.get("Tags", [])

    result = store.create_account(
        email=email, name=name, role_name=role_name,
        iam_user_access_to_billing=iam_access, tags=tags,
    )
    return result
