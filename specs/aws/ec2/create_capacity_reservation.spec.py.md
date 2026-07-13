---
id: "@specs/aws/ec2/create_capacity_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCapacityReservation"
---

# CreateCapacityReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_capacity_reservation
> **spec:implements:** @kind:operation CreateCapacityReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCapacityReservation.spec.md

Creates a new Capacity Reservation with the specified attributes. Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. You can create a Capacity Reservation at any time, and you can choose when it starts. You can create a Capacity Reservation for immediate use or you can request a Capacity Reservation for a future date. For more information, see Reserve compute capacity with On-Demand Capacity Reservations in the Amazon EC2 User Guide . Your request to create a Capacity Reservation could fail if: Amazon EC2 does not have sufficient capacity. In this case, try again at a later time, try in a different Availability Zone, or request a smaller Capacity Reservation. If your workload is flexible across instance types and sizes, try with different instance attributes. The requested quantity exceeds your On-Demand Instance quota. In this case, increase your On-Demand Instance quota for the requested instance type and try again. For more information, see Amazon EC2 Service Quotas in the Amazon EC2 User Guide .

## Input Shape: CreateCapacityReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | Any  # complex shape |  | The Availability Zone in which to create the Capacity Reservation. |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone in which to create the Capacity Reservation. |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| CommitmentDuration | Any  # complex shape |  | Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this para |
| DeliveryPreference | Any  # complex shape |  | Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this para |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EbsOptimized | bool |  | Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throug |
| EndDate | Any  # complex shape |  | The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity  |
| EndDateType | Any  # complex shape |  | Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types |
| EphemeralStorage | bool |  | Deprecated. |
| InstanceCount | int | ✓ | The number of instances for which to reserve capacity. You can request future-dated Capacity Reservations for an instanc |
| InstanceMatchCriteria | Any  # complex shape |  | Indicates the type of instance launches that the Capacity Reservation accepts. The options include: open - The Capacity  |
| InstancePlatform | Any  # complex shape | ✓ | The type of operating system for which to reserve capacity. |
| InstanceType | str | ✓ | The instance type for which to reserve capacity. You can request future-dated Capacity Reservations for instance types i |
| OutpostArn | Any  # complex shape |  | Not supported for future-dated Capacity Reservations. The Amazon Resource Name (ARN) of the Outpost on which to create t |
| PlacementGroupArn | Any  # complex shape |  | Not supported for future-dated Capacity Reservations. The Amazon Resource Name (ARN) of the cluster placement group in w |
| StartDate | Any  # complex shape |  | Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this para |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Capacity Reservation during launch. |
| Tenancy | Any  # complex shape |  | Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings |

## Output Shape: CreateCapacityReservationResult

- **CapacityReservation** (Any  # complex shape): Information about the Capacity Reservation.

## Implementation

```speclang
def create_capacity_reservation(store, request: dict) -> dict:
    """Creates a new Capacity Reservation with the specified attributes. Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. Y"""
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")
    instance_platform = request.get("InstancePlatform", "").strip() if isinstance(request.get("InstancePlatform"), str) else request.get("InstancePlatform")
    if not instance_platform:
        raise ValidationException("InstancePlatform is required")
    instance_type = request.get("InstanceType", "").strip() if isinstance(request.get("InstanceType"), str) else request.get("InstanceType")
    if not instance_type:
        raise ValidationException("InstanceType is required")

    if store.capacity_reservations(instance_count):
        raise ResourceInUseException(f"Resource instance_count already exists")

    record = {
        "ClientToken": client_token,
        "InstanceType": instance_type,
        "InstancePlatform": instance_platform,
        "AvailabilityZone": availability_zone,
        "AvailabilityZoneId": availability_zone_id,
        "Tenancy": tenancy,
        "InstanceCount": instance_count,
        "EbsOptimized": ebs_optimized,
        "EphemeralStorage": ephemeral_storage,
        "EndDate": end_date,
        "EndDateType": end_date_type,
        "InstanceMatchCriteria": instance_match_criteria,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "OutpostArn": outpost_arn,
        "PlacementGroupArn": placement_group_arn,
        "StartDate": start_date,
        "CommitmentDuration": commitment_duration,
        "DeliveryPreference": delivery_preference,
    }

    store.capacity_reservations(instance_count, record)

    return {
        "CapacityReservation": record.get("CapacityReservation", {}),
    }
```
