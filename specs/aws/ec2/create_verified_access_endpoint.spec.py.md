---
id: "@specs/aws/ec2/create_verified_access_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVerifiedAccessEndpoint"
---

# CreateVerifiedAccessEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_verified_access_endpoint
> **spec:implements:** @kind:operation CreateVerifiedAccessEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVerifiedAccessEndpoint.spec.md

An Amazon Web Services Verified Access endpoint is where you define your application along with an optional endpoint-level access policy.

## Input Shape: CreateVerifiedAccessEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ApplicationDomain | str |  | The DNS name for users to reach your application. |
| AttachmentType | Any  # complex shape | ✓ | The type of attachment. |
| CidrOptions | Any  # complex shape |  | The CIDR options. This parameter is required if the endpoint type is cidr . |
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access endpoint. |
| DomainCertificateArn | Any  # complex shape |  | The ARN of the public TLS/SSL certificate in Amazon Web Services Certificate Manager to associate with the endpoint. The |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndpointDomainPrefix | str |  | A custom identifier that is prepended to the DNS name that is generated for the endpoint. |
| EndpointType | Any  # complex shape | ✓ | The type of Verified Access endpoint to create. |
| LoadBalancerOptions | Any  # complex shape |  | The load balancer details. This parameter is required if the endpoint type is load-balancer . |
| NetworkInterfaceOptions | Any  # complex shape |  | The network interface details. This parameter is required if the endpoint type is network-interface . |
| PolicyDocument | str |  | The Verified Access policy document. |
| RdsOptions | Any  # complex shape |  | The RDS details. This parameter is required if the endpoint type is rds . |
| SecurityGroupIds | list[Any  # complex shape] |  | The IDs of the security groups to associate with the Verified Access endpoint. Required if AttachmentType is set to vpc  |
| SseSpecification | Any  # complex shape |  | The options for server side encryption. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Verified Access endpoint. |
| VerifiedAccessGroupId | Any  # complex shape | ✓ | The ID of the Verified Access group to associate the endpoint with. |

## Output Shape: CreateVerifiedAccessEndpointResult

- **VerifiedAccessEndpoint** (Any  # complex shape): Details about the Verified Access endpoint.

## Implementation

```speclang
def create_verified_access_endpoint(store, request: dict) -> dict:
    """An Amazon Web Services Verified Access endpoint is where you define your application along with an optional endpoint-level access policy."""
    attachment_type = request.get("AttachmentType", "").strip() if isinstance(request.get("AttachmentType"), str) else request.get("AttachmentType")
    if not attachment_type:
        raise ValidationException("AttachmentType is required")
    endpoint_type = request.get("EndpointType", "").strip() if isinstance(request.get("EndpointType"), str) else request.get("EndpointType")
    if not endpoint_type:
        raise ValidationException("EndpointType is required")
    verified_access_group_id = request.get("VerifiedAccessGroupId", "").strip() if isinstance(request.get("VerifiedAccessGroupId"), str) else request.get("VerifiedAccessGroupId")
    if not verified_access_group_id:
        raise ValidationException("VerifiedAccessGroupId is required")

    if store.verified_access_endpoints(verified_access_group_id):
        raise ResourceInUseException(f"Resource verified_access_group_id already exists")

    record = {
        "VerifiedAccessGroupId": verified_access_group_id,
        "EndpointType": endpoint_type,
        "AttachmentType": attachment_type,
        "DomainCertificateArn": domain_certificate_arn,
        "ApplicationDomain": application_domain,
        "EndpointDomainPrefix": endpoint_domain_prefix,
        "SecurityGroupIds": security_group_ids,
        "LoadBalancerOptions": load_balancer_options,
        "NetworkInterfaceOptions": network_interface_options,
        "Description": description,
        "PolicyDocument": policy_document,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "SseSpecification": sse_specification,
        "RdsOptions": rds_options,
        "CidrOptions": cidr_options,
    }

    store.verified_access_endpoints(verified_access_group_id, record)

    return {
        "VerifiedAccessEndpoint": record.get("VerifiedAccessEndpoint", {}),
    }
```
