"""CreateOrganizationalUnit handler."""


def handle_create_organizational_unit(store, request: dict) -> dict:
    parent_id = request.get("ParentId", "")
    name = request.get("Name", "")

    if not parent_id:
        raise InvalidInputException("ParentId is required")
    if not name:
        raise InvalidInputException("Name is required")
    if len(name) < 1 or len(name) > 128:
        raise InvalidInputException("Name must be between 1 and 128 characters")

    ou = store.create_organizational_unit(parent_id=parent_id, name=name)
    return {"OrganizationalUnit": ou.to_dict()}
