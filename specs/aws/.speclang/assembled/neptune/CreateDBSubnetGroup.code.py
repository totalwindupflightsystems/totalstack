"""CreateDBSubnetGroup handler for Neptune."""


def create_db_subnet_group(store, request):
    """Create a new DB subnet group."""
    name = request.get('DBSubnetGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBSubnetGroupName is required")

    description = request.get('DBSubnetGroupDescription', '').strip()
    if not description:
        raise InvalidParameterValueException("DBSubnetGroupDescription is required")

    subnet_ids = request.get('SubnetIds', [])
    if not subnet_ids or len(subnet_ids) < 2:
        raise DBSubnetGroupDoesNotCoverEnoughAZs(
            "DB subnet group must contain subnets in at least 2 Availability Zones")

    sg = store.create_subnet_group(
        name, description, subnet_ids,
        tags=request.get('Tags', []),
    )
    return {'DBSubnetGroup': sg.to_dict()}
