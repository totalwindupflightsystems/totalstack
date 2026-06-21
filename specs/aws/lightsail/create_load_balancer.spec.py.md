---
id: "@specs/aws/lightsail/create_load_balancer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateLoadBalancer"
---

# CreateLoadBalancer

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_load_balancer
> **spec:implements:** @kind:operation CreateLoadBalancer
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateLoadBalancer.spec.md

Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see Configure your Lightsail instances for load balancing . You can create up to 10 load balancers per AWS Region in your account. When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the UpdateLoadBalancerAttribute operation. The create load balancer operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateLoadBalancerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateAlternativeNames | list[str] |  | The optional alternative domains and subdomains to use with your SSL/TLS certificate ( www.example.com , example.com , m |
| certificateDomainName | str |  | The domain name with which your certificate is associated ( example.com ). If you specify certificateDomainName , then c |
| certificateName | Any  # complex shape |  | The name of the SSL/TLS certificate. If you specify certificateName , then certificateDomainName is required (and vice-v |
| healthCheckPath | Any  # complex shape |  | The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail us |
| instancePort | int | ✓ | The instance port where you're creating your load balancer. |
| ipAddressType | Any  # complex shape |  | The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, ipv6 for IPv6 only, and dualstack |
| loadBalancerName | Any  # complex shape | ✓ | The name of your load balancer. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |
| tlsPolicyName | Any  # complex shape |  | The name of the TLS policy to apply to the load balancer. Use the GetLoadBalancerTlsPolicies action to get a list of TLS |

## Output Shape: CreateLoadBalancerResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def create_load_balancer(store, request: dict) -> dict:
    """Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see Configure your Lightsail instances for load balancing . You can create up to 10 load balan"""
    instance_port = request.get("instancePort", "").strip() if isinstance(request.get("instancePort"), str) else request.get("instancePort")
    if not instance_port:
        raise ValidationException("instancePort is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    if store.load_balancers(load_balancer_name):
        raise ResourceInUseException(f"Resource load_balancer_name already exists")

    record = {
        "loadBalancerName": load_balancer_name,
        "instancePort": instance_port,
        "healthCheckPath": health_check_path,
        "certificateName": certificate_name,
        "certificateDomainName": certificate_domain_name,
        "certificateAlternativeNames": certificate_alternative_names,
        "tags": tags,
        "ipAddressType": ip_address_type,
        "tlsPolicyName": tls_policy_name,
    }

    store.load_balancers(load_balancer_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
