"""DeleteOrganizationalUnit handler."""


def handle_delete_organizational_unit(store, request: dict) -> dict:
    ou_id = request.get("OrganizationalUnitId", "")
    if not ou_id:
        raise InvalidInputException("OrganizationalUnitId is required")

    store.delete_organizational_unit(ou_id=ou_id)
    return {}
