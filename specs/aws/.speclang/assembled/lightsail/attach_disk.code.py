# spec:trace: aws/lightsail/attach_disk.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/attach-disk
# spec:generated: DO NOT EDIT — edit the spec instead

def attach_disk(store, request: dict) -> dict:
    """Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name. The attach disk operation supports tag-based access control via re"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    disk_path = request.get("diskPath", "").strip() if isinstance(request.get("diskPath"), str) else request.get("diskPath")
    if not disk_path:
        raise ValidationException("diskPath is required")
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachDisk", request)

