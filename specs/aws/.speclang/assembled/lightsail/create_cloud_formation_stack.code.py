# spec:trace: aws/lightsail/create_cloud_formation_stack.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-cloud-formation-stack
# spec:generated: DO NOT EDIT — edit the spec instead

def create_cloud_formation_stack(store, request: dict) -> dict:
    """Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to tra"""
    instances = request.get("instances", "").strip() if isinstance(request.get("instances"), str) else request.get("instances")
    if not instances:
        raise ValidationException("instances is required")

    if store.cloud_formation_stacks(instances):
        raise ResourceInUseException("Resource instances already exists")

    record = {
        "instances": instances,
    }

    store.cloud_formation_stacks(instances, record)

    return {
        "operations": record.get("operations", {}),
    }

