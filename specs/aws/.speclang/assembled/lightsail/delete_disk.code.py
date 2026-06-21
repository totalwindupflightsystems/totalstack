# spec:trace: aws/lightsail/delete_disk.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-disk
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_disk(store, request: dict) -> dict:
    """Deletes the specified block storage disk. The disk must be in the available state (not attached to a Lightsail instance). The disk may remain in the deleting state for several minutes. The delete disk"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")

    if not store.disks(disk_name):
        raise ResourceNotFoundException("Resource disk_name not found")
    store.delete_disks(disk_name)
    return {}

