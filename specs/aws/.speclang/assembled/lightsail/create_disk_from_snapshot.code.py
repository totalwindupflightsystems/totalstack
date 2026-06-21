# spec:trace: aws/lightsail/create_disk_from_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-disk-from-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_disk_from_snapshot(store, request: dict) -> dict:
    """Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    size_in_gb = request.get("sizeInGb", "").strip() if isinstance(request.get("sizeInGb"), str) else request.get("sizeInGb")
    if not size_in_gb:
        raise ValidationException("sizeInGb is required")

    if store.disk_from_snapshots(disk_name):
        raise ResourceInUseException("Resource disk_name already exists")

    record = {
        "diskName": disk_name,
        "diskSnapshotName": disk_snapshot_name,
        "availabilityZone": availability_zone,
        "sizeInGb": size_in_gb,
        "tags": tags,
        "addOns": add_ons,
        "sourceDiskName": source_disk_name,
        "restoreDate": restore_date,
        "useLatestRestorableAutoSnapshot": use_latest_restorable_auto_snapshot,
    }

    store.disk_from_snapshots(disk_name, record)

    return {
        "operations": record.get("operations", {}),
    }

