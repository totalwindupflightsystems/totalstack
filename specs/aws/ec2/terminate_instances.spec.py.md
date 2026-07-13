---
id: "@specs/aws/ec2/terminate_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_TerminateInstances"
---

# TerminateInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/terminate_instances
> **spec:implements:** @kind:operation TerminateInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_TerminateInstances.spec.md

Terminates (deletes) the specified instances. This operation is idempotent ; if you terminate an instance more than once, each call succeeds. Terminating an instance is permanent and irreversible. After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works . Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage. If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated. If you terminate multiple instances across multiple Availability Zones, and one or more of the specified instances are enabled for termination protection, the request fails with the following results: The specified instances that are in the same Availability Zone as the protected instance are not terminated. The specified instances that are in different Availability Zones, where no other specified instances are protected, are successfully terminated. For example, say you have the following instances: Instance A: us-east-1a ; Not protected Instance B: us-east-1a ; Not protected Instance C: us-east-1b ; Protected Instance D: us-east-1b ; not protected If you attempt to terminate all of these instances in the same request, the request reports failure with the following results: Instance A and Instance B are successfully terminated because none of the specified instances in us-east-1a are enabled for termination protection. Instance C and Instance D fail to terminate because at least one of the specified instances in us-east-1b (Instance C) is enabled for termination protection. Terminated instances remain visible after termination (for approximately one hour). By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running. By default, the TerminateInstances operation includes a graceful operating system (OS) shutdown. To bypass the graceful shutdown, use the skipOsShutdown parameter; however, this might risk data integrity. You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the DeleteOnTermination block device mapping parameter set to true are automatically deleted. For more information about the differences between stopping and terminating instances, see Amazon EC2 instance state changes in the Amazon EC2 User Guide . When you terminate an instance, we attempt to terminate it forcibly after a short while. If your instance appears stuck in the shutting-down state after a period of time, there might be an issue with the underlying host computer. For more information about terminating and troubleshooting terminating your instances, see Terminate Amazon EC2 instances and Troubleshooting terminating your instance in the Amazon EC2 User Guide .

## Input Shape: TerminateInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Force | bool |  | Forces the instances to terminate. The instance will first attempt a graceful shutdown, which includes flushing file sys |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances. Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batch |
| SkipOsShutdown | bool |  | Specifies whether to bypass the graceful OS shutdown process when the instance is terminated. Default: false |

## Output Shape: TerminateInstancesResult

- **TerminatingInstances** (list[Any  # complex shape]): Information about the terminated instances.

## Implementation

```speclang
def terminate_instances(store, request: dict) -> dict:
    """Terminates (deletes) the specified instances. This operation is idempotent ; if you terminate an instance more than once, each call succeeds. Terminating an instance is permanent and irreversible. Aft"""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")

    if not store.terminate_instancess(instance_ids):
        raise ResourceNotFoundException(f"Resource instance_ids not found")
    store.delete_terminate_instancess(instance_ids)
    return {}
```
