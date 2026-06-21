# spec:trace: aws/lightsail/create_disk.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-disk
# spec:generated: DO NOT EDIT — edit the spec instead

def create_disk(store, request: dict) -> dict:
    """Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create disk operation supports tag-based access control via request """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    size_in_gb = request.get("sizeInGb", "").strip() if isinstance(request.get("sizeInGb"), str) else request.get("sizeInGb")
    if not size_in_gb:
        raise ValidationException("sizeInGb is required")

    if store.disks(disk_name):
        raise ResourceInUseException("Resource disk_name already exists")

    tags = request.get("tags", [])
    add_ons = request.get("addOns", [])

    record = {
        "diskName": disk_name,
        "availabilityZone": availability_zone,
        "sizeInGb": size_in_gb,
        "tags": tags,
        "addOns": add_ons,
    }

    store.disks(disk_name, record)

    return {
        "operations": record.get("operations", {}),
    }

