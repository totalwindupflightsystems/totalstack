# spec:trace: aws/lightsail/create_instances_from_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-instances-from-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_instances_from_snapshot(store, request: dict) -> dict:
    """Creates one or more new instances from a manual or automatic snapshot of an instance. The create instances from snapshot operation supports tag-based access control via request tags and resource tags """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")

    if store.instances_from_snapshots(instance_names):
        raise ResourceInUseException("Resource instance_names already exists")

    record = {
        "instanceNames": instance_names,
        "attachedDiskMapping": attached_disk_mapping,
        "availabilityZone": availability_zone,
        "instanceSnapshotName": instance_snapshot_name,
        "bundleId": bundle_id,
        "userData": user_data,
        "keyPairName": key_pair_name,
        "tags": tags,
        "addOns": add_ons,
        "ipAddressType": ip_address_type,
        "sourceInstanceName": source_instance_name,
        "restoreDate": restore_date,
        "useLatestRestorableAutoSnapshot": use_latest_restorable_auto_snapshot,
    }

    store.instances_from_snapshots(instance_names, record)

    return {
        "operations": record.get("operations", {}),
    }

