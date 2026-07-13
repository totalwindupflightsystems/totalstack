---
id: "@specs/aws/ec2/release_hosts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReleaseHosts"
---

# ReleaseHosts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/release_hosts
> **spec:implements:** @kind:operation ReleaseHosts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReleaseHosts.spec.md

When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into released state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, for example, to modify the host. You must stop or terminate all instances on a host before it can be released. When Dedicated Hosts are released, it may take some time for them to stop counting toward your limit and you may receive capacity errors when trying to allocate new Dedicated Hosts. Wait a few minutes and then try again. Released hosts still appear in a DescribeHosts response.

## Input Shape: ReleaseHostsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| HostIds | list[Any  # complex shape] | ✓ | The IDs of the Dedicated Hosts to release. |

## Output Shape: ReleaseHostsResult

- **Successful** (list[str]): The IDs of the Dedicated Hosts that were successfully released.
- **Unsuccessful** (list[Any  # complex shape]): The IDs of the Dedicated Hosts that could not be released, including an error message.

## Implementation

```speclang
def release_hosts(store, request: dict) -> dict:
    """When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into released state. The host ID of Dedicated Hosts that have been release"""
    host_ids = request.get("HostIds", "").strip() if isinstance(request.get("HostIds"), str) else request.get("HostIds")
    if not host_ids:
        raise ValidationException("HostIds is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReleaseHosts", request)
```
