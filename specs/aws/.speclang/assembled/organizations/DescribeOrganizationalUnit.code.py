"""DescribeOrganizationalUnit handler."""


def handle_describe_organizational_unit(store, request: dict) -> dict:
    ou_id = request.get("OrganizationalUnitId", "")
    if not ou_id:
        raise InvalidInputException("OrganizationalUnitId is required")

    ou = store.describe_organizational_unit(ou_id=ou_id)
    return {"OrganizationalUnit": ou.to_dict()}
