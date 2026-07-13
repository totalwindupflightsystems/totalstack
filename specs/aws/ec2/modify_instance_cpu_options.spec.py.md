---
id: "@specs/aws/ec2/modify_instance_cpu_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceCpuOptions"
---

# ModifyInstanceCpuOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_cpu_options
> **spec:implements:** @kind:operation ModifyInstanceCpuOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceCpuOptions.spec.md

By default, all vCPUs for the instance type are active when you launch an instance. When you configure the number of active vCPUs for the instance, it can help you save on licensing costs and optimize performance. The base cost of the instance remains unchanged. The number of active vCPUs equals the number of threads per CPU core multiplied by the number of cores. The instance must be in a Stopped state before you make changes. Some instance type options do not support this capability. For more information, see Supported CPU options in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceCpuOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CoreCount | int |  | The number of CPU cores to activate for the specified instance. |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance to update. |
| NestedVirtualization | Any  # complex shape |  | Indicates whether to enable or disable nested virtualization for the instance. When nested virtualization is enabled, Vi |
| ThreadsPerCore | int |  | The number of threads to run for each CPU core. |

## Output Shape: ModifyInstanceCpuOptionsResult

- **CoreCount** (int): The number of CPU cores that are running for the specified instance after the update.
- **InstanceId** (Any  # complex shape): The ID of the instance that was updated.
- **NestedVirtualization** (Any  # complex shape): Indicates whether nested virtualization has been enabled or disabled.
- **ThreadsPerCore** (int): The number of threads that are running per CPU core for the specified instance after the update.

## Implementation

```speclang
def modify_instance_cpu_options(store, request: dict) -> dict:
    """By default, all vCPUs for the instance type are active when you launch an instance. When you configure the number of active vCPUs for the instance, it can help you save on licensing costs and optimize"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_cpu_optionss(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "CoreCount" in request:
        resource["CoreCount"] = core_count
    if "ThreadsPerCore" in request:
        resource["ThreadsPerCore"] = threads_per_core
    if "NestedVirtualization" in request:
        resource["NestedVirtualization"] = nested_virtualization
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.instance_cpu_optionss(instance_id, resource)
    return resource
```
