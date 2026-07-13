---
id: "@specs/aws/ec2/get_launch_template_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetLaunchTemplateData"
---

# GetLaunchTemplateData

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_launch_template_data
> **spec:implements:** @kind:operation GetLaunchTemplateData
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetLaunchTemplateData.spec.md

Retrieves the configuration data of the specified instance. You can use this data to create a launch template. This action calls on other describe actions to get instance information. Depending on your instance configuration, you may need to allow the following actions in your IAM policy: DescribeSpotInstanceRequests , DescribeInstanceCreditSpecifications , DescribeVolumes , and DescribeInstanceAttribute . Or, you can allow describe* depending on your instance requirements.

## Input Shape: GetLaunchTemplateDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |

## Output Shape: GetLaunchTemplateDataResult

- **LaunchTemplateData** (Any  # complex shape): The instance data.

## Implementation

```speclang
def get_launch_template_data(store, request: dict) -> dict:
    """Retrieves the configuration data of the specified instance. You can use this data to create a launch template. This action calls on other describe actions to get instance information. Depending on you"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.launch_template_datas(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")
    return {"InstanceId": instance_id, **resource}
```
