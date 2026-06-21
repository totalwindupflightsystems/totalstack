---
id: "@specs/aws/lightsail/create_load_balancer_tls_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateLoadBalancerTlsCertificate"
---

# CreateLoadBalancerTlsCertificate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_load_balancer_tls_certificate
> **spec:implements:** @kind:operation CreateLoadBalancerTlsCertificate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateLoadBalancerTlsCertificate.spec.md

Creates an SSL/TLS certificate for an Amazon Lightsail load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). The CreateLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateLoadBalancerTlsCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateAlternativeNames | list[str] |  | An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the  |
| certificateDomainName | str | ✓ | The domain name ( example.com ) for your SSL/TLS certificate. |
| certificateName | Any  # complex shape | ✓ | The SSL/TLS certificate name. You can have up to 10 certificates in your account at one time. Each Lightsail load balanc |
| loadBalancerName | Any  # complex shape | ✓ | The load balancer name where you want to create the SSL/TLS certificate. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateLoadBalancerTlsCertificateResult

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
def create_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate for an Amazon Lightsail load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). The CreateLoadBalancerTlsCertificate operation supports """
    certificate_domain_name = request.get("certificateDomainName", "").strip() if isinstance(request.get("certificateDomainName"), str) else request.get("certificateDomainName")
    if not certificate_domain_name:
        raise ValidationException("certificateDomainName is required")
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    if store.load_balancer_tls_certificates(certificate_domain_name):
        raise ResourceInUseException(f"Resource certificate_domain_name already exists")

    record = {
        "loadBalancerName": load_balancer_name,
        "certificateName": certificate_name,
        "certificateDomainName": certificate_domain_name,
        "certificateAlternativeNames": certificate_alternative_names,
        "tags": tags,
    }

    store.load_balancer_tls_certificates(certificate_domain_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
