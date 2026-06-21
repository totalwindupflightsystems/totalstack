# spec:trace: aws/lightsail/get_cloud_formation_stack_records.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-cloud-formation-stack-records
# spec:generated: DO NOT EDIT — edit the spec instead

def get_cloud_formation_stack_records(store, request: dict) -> dict:
    """Returns the CloudFormation stack record created as a result of the create cloud formation stack operation. An AWS CloudFormation stack is used to create a new Amazon EC2 instance from an exported Ligh"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

