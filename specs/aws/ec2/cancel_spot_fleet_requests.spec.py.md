---
id: "@specs/aws/ec2/cancel_spot_fleet_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelSpotFleetRequests"
---

# CancelSpotFleetRequests

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_spot_fleet_requests
> **spec:implements:** @kind:operation CancelSpotFleetRequests
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelSpotFleetRequests.spec.md

Cancels the specified Spot Fleet requests. After you cancel a Spot Fleet request, the Spot Fleet launches no new instances. You must also specify whether a canceled Spot Fleet request should terminate its instances. If you choose to terminate the instances, the Spot Fleet request enters the cancelled_terminating state. Otherwise, the Spot Fleet request enters the cancelled_running state and the instances continue to run until they are interrupted or you terminate them manually. Terminating an instance is permanent and irreversible. After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works . Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage. Restrictions You can delete up to 100 fleets in a single request. If you exceed the specified number, no fleets are deleted.

## Input Shape: CancelSpotFleetRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SpotFleetRequestIds | list[Any  # complex shape] | ✓ | The IDs of the Spot Fleet requests. Constraint: You can specify up to 100 IDs in a single request. |
| TerminateInstances | bool | ✓ | Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to termi |

## Output Shape: CancelSpotFleetRequestsResponse

- **SuccessfulFleetRequests** (Any  # complex shape): Information about the Spot Fleet requests that are successfully canceled.
- **UnsuccessfulFleetRequests** (Any  # complex shape): Information about the Spot Fleet requests that are not successfully canceled.

## Implementation

```speclang
def cancel_spot_fleet_requests(store, request: dict) -> dict:
    """Cancels the specified Spot Fleet requests. After you cancel a Spot Fleet request, the Spot Fleet launches no new instances. You must also specify whether a canceled Spot Fleet request should terminate"""
    spot_fleet_request_ids = request.get("SpotFleetRequestIds", "").strip() if isinstance(request.get("SpotFleetRequestIds"), str) else request.get("SpotFleetRequestIds")
    terminate_instances = request.get("TerminateInstances", "").strip() if isinstance(request.get("TerminateInstances"), str) else request.get("TerminateInstances")

    if not store.spot_fleet_requestss(spot_fleet_request_ids):
        raise ResourceNotFoundException(f"Resource spot_fleet_request_ids not found")
    store.delete_spot_fleet_requestss(spot_fleet_request_ids)
    return {}
```
