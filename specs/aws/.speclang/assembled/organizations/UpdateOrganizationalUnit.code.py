"""UpdateOrganizationalUnit handler."""


def handle_update_organizational_unit(store, request: dict) -> dict:
    ou_id = request.get("OrganizationalUnitId", "")
    name = request.get("Name")

    if not ou_id:
        raise InvalidInputException("OrganizationalUnitId is required")

    result = store.update_organizational_unit(ou_id=ou_id, name=name)
    return result
