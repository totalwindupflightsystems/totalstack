---
id: "@specs/aws/ec2/export_transit_gateway_routes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ExportTransitGatewayRoutes"
---

# ExportTransitGatewayRoutes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/export_transit_gateway_routes
> **spec:implements:** @kind:operation ExportTransitGatewayRoutes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ExportTransitGatewayRoutes.spec.md

Exports routes from the specified transit gateway route table to the specified S3 bucket. By default, all routes are exported. Alternatively, you can filter by CIDR range. The routes are saved to the specified bucket in a JSON file. For more information, see Export route tables to Amazon S3 in the Amazon Web Services Transit Gateways Guide .

## Input Shape: ExportTransitGatewayRoutesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: attachment.transit-gateway-attachment-id - The id of the transit gateway a |
| S3Bucket | str | ✓ | The name of the S3 bucket. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the route table. |

## Output Shape: ExportTransitGatewayRoutesResult

- **S3Location** (str): The URL of the exported file in Amazon S3. For example, s3:// bucket_name /VPCTransitGateway/TransitGatewayRouteTables/ 

## Implementation

```speclang
def export_transit_gateway_routes(store, request: dict) -> dict:
    """Exports routes from the specified transit gateway route table to the specified S3 bucket. By default, all routes are exported. Alternatively, you can filter by CIDR range. The routes are saved to the """
    s3_bucket = request.get("S3Bucket", "").strip() if isinstance(request.get("S3Bucket"), str) else request.get("S3Bucket")
    if not s3_bucket:
        raise ValidationException("S3Bucket is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportTransitGatewayRoutes", request)
```
