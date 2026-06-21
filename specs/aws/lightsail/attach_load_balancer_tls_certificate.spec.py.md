---
id: "@specs/aws/lightsail/attach_load_balancer_tls_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_AttachLoadBalancerTlsCertificate"
---

# AttachLoadBalancerTlsCertificate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/attach_load_balancer_tls_certificate
> **spec:implements:** @kind:operation AttachLoadBalancerTlsCertificate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_AttachLoadBalancerTlsCertificate.spec.md

Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). Once you create and validate your certificate, you can attach it to your load balancer. You can also use this API to rotate the certificates on your account. Use the AttachLoadBalancerTlsCertificate action with the non-attached certificate, and it will replace the existing one and become the attached certificate. The AttachLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: AttachLoadBalancerTlsCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape | ✓ | The name of your SSL/TLS certificate. |
| loadBalancerName | Any  # complex shape | ✓ | The name of the load balancer to which you want to associate the SSL/TLS certificate. |

## Output Shape: AttachLoadBalancerTlsCertificateResult

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
def attach_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). Once you create and validate your certificate, yo"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachLoadBalancerTlsCertificate", request)
```
