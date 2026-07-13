---
id: "@specs/aws/ec2/delete_fleets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteFleets"
---

# DeleteFleets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_fleets
> **spec:implements:** @kind:operation DeleteFleets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteFleets.spec.md

Deletes the specified EC2 Fleet request. After you delete an EC2 Fleet request, it launches no new instances. You must also specify whether a deleted EC2 Fleet request should terminate its instances. If you choose to terminate the instances, the EC2 Fleet request enters the deleted_terminating state. Otherwise, it enters the deleted_running state, and the instances continue to run until they are interrupted or you terminate them manually. A deleted instant fleet with running instances is not supported. When you delete an instant fleet, Amazon EC2 automatically terminates all its instances. For fleets with more than 1000 instances, the deletion request might fail. If your fleet has more than 1000 instances, first terminate most of the instances manually, leaving 1000 or fewer. Then delete the fleet, and the remaining instances will be terminated automatically. Terminating an instance is permanent and irreversible. After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works . Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage. Restrictions You can delete up to 25 fleets of type instant in a single request. You can delete up to 100 fleets of type maintain or request in a single request. You can delete up to 125 fleets in a single request, provided you do not exceed the quota for each fleet type, as specified above. If you exceed the specified number of fleets to delete, no fleets are deleted. For more information, see Delete an EC2 Fleet request and the instances in the fleet in the Amazon EC2 User Guide .

## Input Shape: DeleteFleetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FleetIds | Any  # complex shape | ✓ | The IDs of the EC2 Fleets. Constraints: In a single request, you can specify up to 25 instant fleet IDs and up to 100 ma |
| TerminateInstances | bool | ✓ | Indicates whether to terminate the associated instances when the EC2 Fleet is deleted. The default is to terminate the i |

## Output Shape: DeleteFleetsResult

- **SuccessfulFleetDeletions** (Any  # complex shape): Information about the EC2 Fleets that are successfully deleted.
- **UnsuccessfulFleetDeletions** (Any  # complex shape): Information about the EC2 Fleets that are not successfully deleted.

## Implementation

```speclang
def delete_fleets(store, request: dict) -> dict:
    """Deletes the specified EC2 Fleet request. After you delete an EC2 Fleet request, it launches no new instances. You must also specify whether a deleted EC2 Fleet request should terminate its instances. """
    fleet_ids = request.get("FleetIds", "").strip() if isinstance(request.get("FleetIds"), str) else request.get("FleetIds")
    terminate_instances = request.get("TerminateInstances", "").strip() if isinstance(request.get("TerminateInstances"), str) else request.get("TerminateInstances")

    if not store.fleetss(fleet_ids):
        raise ResourceNotFoundException(f"Resource fleet_ids not found")
    store.delete_fleetss(fleet_ids)
    return {}
```
