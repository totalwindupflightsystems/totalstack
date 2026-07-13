---
id: "@specs/aws/ec2/create_traffic_mirror_filter"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTrafficMirrorFilter"
---

# CreateTrafficMirrorFilter

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_traffic_mirror_filter
> **spec:implements:** @kind:operation CreateTrafficMirrorFilter
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTrafficMirrorFilter.spec.md

Creates a Traffic Mirror filter. A Traffic Mirror filter is a set of rules that defines the traffic to mirror. By default, no traffic is mirrored. To mirror traffic, use CreateTrafficMirrorFilterRule to add Traffic Mirror rules to the filter. The rules you add define what traffic gets mirrored. You can also use ModifyTrafficMirrorFilterNetworkServices to mirror supported network services.

## Input Shape: CreateTrafficMirrorFilterRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| Description | str |  | The description of the Traffic Mirror filter. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to a Traffic Mirror filter. |

## Output Shape: CreateTrafficMirrorFilterResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H
- **TrafficMirrorFilter** (Any  # complex shape): Information about the Traffic Mirror filter.

## Implementation

```speclang
def create_traffic_mirror_filter(store, request: dict) -> dict:
    """Creates a Traffic Mirror filter. A Traffic Mirror filter is a set of rules that defines the traffic to mirror. By default, no traffic is mirrored. To mirror traffic, use CreateTrafficMirrorFilterRule """


    record = {
        "Description": description,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "ClientToken": client_token,
    }

    store.traffic_mirror_filters(record)

    return {
        "TrafficMirrorFilter": record.get("TrafficMirrorFilter", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
