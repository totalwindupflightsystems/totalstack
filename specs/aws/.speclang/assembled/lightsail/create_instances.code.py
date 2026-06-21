# spec:trace: aws/lightsail/create_instances.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-instances
# spec:generated: DO NOT EDIT — edit the spec instead

def create_instances(store, request: dict) -> dict:
    """Creates one or more Amazon Lightsail instances. The create instances operation supports tag-based access control via request tags. For more information, see the Lightsail Developer Guide ."""
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    blueprint_id = request.get("blueprintId", "").strip() if isinstance(request.get("blueprintId"), str) else request.get("blueprintId")
    if not blueprint_id:
        raise ValidationException("blueprintId is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")
    instance_names = request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")

    # Normalize to list
    if isinstance(instance_names, str):
        name_list = [instance_names.strip()]
    elif isinstance(instance_names, list):
        name_list = [n.strip() if isinstance(n, str) else str(n) for n in instance_names]
    else:
        name_list = [str(instance_names)]

    if not name_list:
        raise ValidationException("instanceNames is required")

    # Check for duplicates
    for name in name_list:
        if store.instances(name):
            raise ResourceInUseException(f"Resource {name} already exists")

    custom_image_name = request.get("customImageName", "")
    user_data = request.get("userData", "")
    key_pair_name = request.get("keyPairName", "")
    tags = request.get("tags", [])
    add_ons = request.get("addOns", [])
    ip_address_type = request.get("ipAddressType", "ipv4")

    operations = []
    for name in name_list:
        record = {
            "name": name,
            "availabilityZone": availability_zone,
            "customImageName": custom_image_name,
            "blueprintId": blueprint_id,
            "bundleId": bundle_id,
            "userData": user_data,
            "keyPairName": key_pair_name,
            "tags": tags,
            "addOns": add_ons,
            "ipAddressType": ip_address_type,
        }
        store.instances(name, record)
        operations.append({"name": name, "status": "created"})

    return {
        "operations": operations,
    }

