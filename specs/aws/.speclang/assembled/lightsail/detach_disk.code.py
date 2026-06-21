# spec:trace: aws/lightsail/detach_disk.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/detach-disk
# spec:generated: DO NOT EDIT — edit the spec instead

def detach_disk(store, request: dict) -> dict:
    """Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk. T"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachDisk", request)

