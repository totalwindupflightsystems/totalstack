---
id: "@specs/aws/ec2/start_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StartInstances"
---

# StartInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/start_instances
> **spec:implements:** @kind:operation StartInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StartInstances.spec.md

Starts an Amazon EBS-backed instance that you've previously stopped. Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the compute resources are released and you are not billed for instance usage. However, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. You can restart your instance at any time. Every time you start your instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage. Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM. Performing this operation on an instance that uses an instance store as its root device returns an error. If you attempt to start a T3 instance with host tenancy and the unlimited CPU credit option, the request fails. The unlimited CPU credit option is not supported on Dedicated Hosts. Before you start the instance, either change its CPU credit option to standard , or change its tenancy to default or dedicated . For more information, see Stop and start Amazon EC2 instances in the Amazon EC2 User Guide .

## Input Shape: StartInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AdditionalInfo | str |  | Reserved. |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances. |

## Output Shape: StartInstancesResult

- **StartingInstances** (list[Any  # complex shape]): Information about the started instances.

## Implementation

```speclang
def start_instances(store, request: dict) -> dict:
    """Starts an Amazon EBS-backed instance that you've previously stopped. Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the co"""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    if store.instancess(instance_ids):
        raise ResourceInUseException(f"Resource instance_ids already exists")

    record = {
        "InstanceIds": instance_ids,
        "AdditionalInfo": additional_info,
        "DryRun": dry_run,
    }

    store.instancess(instance_ids, record)

    return {
        "StartingInstances": record.get("StartingInstances", {}),
    }
```
