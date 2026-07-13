---
id: "@specs/aws/ec2/describe_scheduled_instance_availability"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeScheduledInstanceAvailability"
---

# DescribeScheduledInstanceAvailability

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_scheduled_instance_availability
> **spec:implements:** @kind:operation DescribeScheduledInstanceAvailability
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeScheduledInstanceAvailability.spec.md

Finds available schedules that meet the specified criteria. You can search for an available schedule no more than 3 months in advance. You must meet the minimum required duration of 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours. After you find a schedule that meets your needs, call PurchaseScheduledInstances to purchase Scheduled Instances with that schedule.

## Input Shape: DescribeScheduledInstanceAvailabilityRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone (for example, us-west-2a ). instance-type - The instance type (fo |
| FirstSlotStartTimeRange | Any  # complex shape | ✓ | The time period for the first schedule to start. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. |
| MaxSlotDurationInHours | int |  | The maximum available duration, in hours. This value must be greater than MinSlotDurationInHours and less than 1,720. |
| MinSlotDurationInHours | int |  | The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimu |
| NextToken | str |  | The token for the next set of results. |
| Recurrence | Any  # complex shape | ✓ | The schedule recurrence. |

## Output Shape: DescribeScheduledInstanceAvailabilityResult

- **NextToken** (str): The token required to retrieve the next set of results. This value is null when there are no more results to return.
- **ScheduledInstanceAvailabilitySet** (Any  # complex shape): Information about the available Scheduled Instances.

## Implementation

```speclang
def describe_scheduled_instance_availability(store, request: dict) -> dict:
    """Finds available schedules that meet the specified criteria. You can search for an available schedule no more than 3 months in advance. You must meet the minimum required duration of 1,200 hours per ye"""
    first_slot_start_time_range = request.get("FirstSlotStartTimeRange", "").strip() if isinstance(request.get("FirstSlotStartTimeRange"), str) else request.get("FirstSlotStartTimeRange")
    if not first_slot_start_time_range:
        raise ValidationException("FirstSlotStartTimeRange is required")
    recurrence = request.get("Recurrence", "").strip() if isinstance(request.get("Recurrence"), str) else request.get("Recurrence")
    if not recurrence:
        raise ValidationException("Recurrence is required")

    resource = store.scheduled_instance_availabilitys(first_slot_start_time_range)
    if not resource:
        raise ResourceNotFoundException(f"Resource first_slot_start_time_range not found")
    return {"FirstSlotStartTimeRange": first_slot_start_time_range, **resource}
```
