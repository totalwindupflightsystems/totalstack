---
id: "@specs/aws/ec2/create_network_insights_path"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkInsightsPath"
---

# CreateNetworkInsightsPath

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_insights_path
> **spec:implements:** @kind:operation CreateNetworkInsightsPath
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkInsightsPath.spec.md

Creates a path to analyze for reachability. Reachability Analyzer enables you to analyze and debug network reachability between two resources in your virtual private cloud (VPC). For more information, see the Reachability Analyzer Guide .

## Input Shape: CreateNetworkInsightsPathRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str | ✓ | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| Destination | Any  # complex shape |  | The ID or ARN of the destination. If the resource is in another account, you must specify an ARN. |
| DestinationIp | Any  # complex shape |  | The IP address of the destination. |
| DestinationPort | int |  | The destination port. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FilterAtDestination | Any  # complex shape |  | Scopes the analysis to network paths that match specific filters at the destination. If you specify this parameter, you  |
| FilterAtSource | Any  # complex shape |  | Scopes the analysis to network paths that match specific filters at the source. If you specify this parameter, you can't |
| Protocol | Any  # complex shape | ✓ | The protocol. |
| Source | Any  # complex shape | ✓ | The ID or ARN of the source. If the resource is in another account, you must specify an ARN. |
| SourceIp | Any  # complex shape |  | The IP address of the source. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to add to the path. |

## Output Shape: CreateNetworkInsightsPathResult

- **NetworkInsightsPath** (Any  # complex shape): Information about the path.

## Implementation

```speclang
def create_network_insights_path(store, request: dict) -> dict:
    """Creates a path to analyze for reachability. Reachability Analyzer enables you to analyze and debug network reachability between two resources in your virtual private cloud (VPC). For more information,"""
    client_token = request.get("ClientToken", "").strip() if isinstance(request.get("ClientToken"), str) else request.get("ClientToken")
    if not client_token:
        raise ValidationException("ClientToken is required")
    protocol = request.get("Protocol", "").strip() if isinstance(request.get("Protocol"), str) else request.get("Protocol")
    if not protocol:
        raise ValidationException("Protocol is required")
    source = request.get("Source", "").strip() if isinstance(request.get("Source"), str) else request.get("Source")
    if not source:
        raise ValidationException("Source is required")

    if store.network_insights_paths(client_token):
        raise ResourceInUseException(f"Resource client_token already exists")

    record = {
        "SourceIp": source_ip,
        "DestinationIp": destination_ip,
        "Source": source,
        "Destination": destination,
        "Protocol": protocol,
        "DestinationPort": destination_port,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "ClientToken": client_token,
        "FilterAtSource": filter_at_source,
        "FilterAtDestination": filter_at_destination,
    }

    store.network_insights_paths(client_token, record)

    return {
        "NetworkInsightsPath": record.get("NetworkInsightsPath", {}),
    }
```
