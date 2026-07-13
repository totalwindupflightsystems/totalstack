---
id: "@specs/aws/ec2/stop_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StopInstances"
---

# StopInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/stop_instances
> **spec:implements:** @kind:operation StopInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StopInstances.spec.md

Stops an Amazon EBS-backed instance. You can restart your instance at any time using the StartInstances API. For more information, see Stop and start Amazon EC2 instances in the Amazon EC2 User Guide . When you stop or hibernate an instance, we shut it down. By default, this includes a graceful operating system (OS) shutdown. To bypass the graceful shutdown, use the skipOsShutdown parameter; however, this might risk data integrity. You can use the StopInstances operation together with the Hibernate parameter to hibernate an instance if the instance is enabled for hibernation and meets the hibernation prerequisites . Stopping an instance doesn't preserve data stored in RAM, while hibernation does. If hibernation fails, a normal shutdown occurs. For more information, see Hibernate your Amazon EC2 instance in the Amazon EC2 User Guide . If your instance appears stuck in the stopping state, there might be an issue with the underlying host computer. You can use the StopInstances operation together with the Force parameter to force stop your instance. For more information, see Troubleshoot Amazon EC2 instance stop issues in the Amazon EC2 User Guide . Stopping and hibernating an instance differs from rebooting or terminating it. For example, a stopped or hibernated instance retains its root volume and any data volumes, unlike terminated instances where these volumes are automatically deleted. For more information about the differences between stopping, hibernating, rebooting, and terminating instances, see Amazon EC2 instance state changes in the Amazon EC2 User Guide . We don't charge for instance usage or data transfer fees when an instance is stopped. However, the root volume and any data volumes remain and continue to persist your data, and you're charged for volume usage. Every time you start your instance, Amazon EC2 charges a one-minute minimum for instance usage, followed by per-second billing. You can't stop or hibernate instance store-backed instances.

## Input Shape: StopInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Force | bool |  | Forces the instance to stop. The instance will first attempt a graceful shutdown, which includes flushing file system ca |
| Hibernate | bool |  | Hibernates the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successf |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances. |
| SkipOsShutdown | bool |  | Specifies whether to bypass the graceful OS shutdown process when the instance is stopped. Bypassing the graceful OS shu |

## Output Shape: StopInstancesResult

- **StoppingInstances** (list[Any  # complex shape]): Information about the stopped instances.

## Implementation

```speclang
def stop_instances(store, request: dict) -> dict:
    """Stops an Amazon EBS-backed instance. You can restart your instance at any time using the StartInstances API. For more information, see Stop and start Amazon EC2 instances in the Amazon EC2 User Guide """
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")

    if not store.instancess(instance_ids):
        raise ResourceNotFoundException(f"Resource instance_ids not found")
    store.delete_instancess(instance_ids)
    return {}
```
