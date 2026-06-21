# spec:trace: aws/lightsail/get_disk.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-disk
# spec:generated: DO NOT EDIT — edit the spec instead

def get_disk(store, request: dict) -> dict:
    """Returns information about a specific block storage disk."""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")

    resource = store.disks(disk_name)
    if not resource:
        raise ResourceNotFoundException("Resource disk_name not found")
    return {"diskName": disk_name, **resource}

