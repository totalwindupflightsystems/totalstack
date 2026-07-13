---
id: "@specs/aws/ec2/create_customer_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCustomerGateway"
---

# CreateCustomerGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_customer_gateway
> **spec:implements:** @kind:operation CreateCustomerGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCustomerGateway.spec.md

Provides information to Amazon Web Services about your customer gateway device. The customer gateway device is the appliance at your end of the VPN connection. You must provide the IP address of the customer gateway device’s external interface. The IP address must be static and can be behind a device performing network address translation (NAT). For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN. For more information, see Customer gateway options for your Site-to-Site VPN connection in the Amazon Web Services Site-to-Site VPN User Guide . To create more than one customer gateway with the same VPN type, IP address, and BGP ASN, specify a unique device name for each customer gateway. An identical request returns information about the existing customer gateway; it doesn't create a new customer gateway.

## Input Shape: CreateCustomerGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BgpAsn | int |  | For customer gateway devices that support BGP, specify the device's ASN. You must specify either BgpAsn or BgpAsnExtende |
| BgpAsnExtended | int |  | For customer gateway devices that support BGP, specify the device's ASN. You must specify either BgpAsn or BgpAsnExtende |
| CertificateArn | str |  | The Amazon Resource Name (ARN) for the customer gateway certificate. |
| DeviceName | str |  | A name for the customer gateway device. Length Constraints: Up to 255 characters. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpAddress | str |  | The IP address for the customer gateway device's outside interface. The address must be static. If OutsideIpAddressType  |
| PublicIp | str |  | This member has been deprecated. The Internet-routable IP address for the customer gateway's outside interface. The addr |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the customer gateway. |
| Type | Any  # complex shape | ✓ | The type of VPN connection that this customer gateway supports ( ipsec.1 ). |

## Output Shape: CreateCustomerGatewayResult

- **CustomerGateway** (Any  # complex shape): Information about the customer gateway.

## Implementation

```speclang
def create_customer_gateway(store, request: dict) -> dict:
    """Provides information to Amazon Web Services about your customer gateway device. The customer gateway device is the appliance at your end of the VPN connection. You must provide the IP address of the c"""
    type = request.get("Type", "").strip() if isinstance(request.get("Type"), str) else request.get("Type")
    if not type:
        raise ValidationException("Type is required")

    if store.customer_gateways(type):
        raise ResourceInUseException(f"Resource type already exists")

    record = {
        "BgpAsn": bgp_asn,
        "PublicIp": public_ip,
        "CertificateArn": certificate_arn,
        "Type": type,
        "TagSpecifications": tag_specifications,
        "DeviceName": device_name,
        "IpAddress": ip_address,
        "BgpAsnExtended": bgp_asn_extended,
        "DryRun": dry_run,
    }

    store.customer_gateways(type, record)

    return {
        "CustomerGateway": record.get("CustomerGateway", {}),
    }
```
