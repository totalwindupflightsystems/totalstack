---
id: "@specs/aws/lightsail/delete_load_balancer_tls_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteLoadBalancerTlsCertificate"
---

# DeleteLoadBalancerTlsCertificate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_load_balancer_tls_certificate
> **spec:implements:** @kind:operation DeleteLoadBalancerTlsCertificate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteLoadBalancerTlsCertificate.spec.md

Deletes an SSL/TLS certificate associated with a Lightsail load balancer. The DeleteLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteLoadBalancerTlsCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape | ✓ | The SSL/TLS certificate name. |
| force | Any  # complex shape |  | When true , forces the deletion of an SSL/TLS certificate. There can be two certificates associated with a Lightsail loa |
| loadBalancerName | Any  # complex shape | ✓ | The load balancer name. |

## Output Shape: DeleteLoadBalancerTlsCertificateResult

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
def delete_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Deletes an SSL/TLS certificate associated with a Lightsail load balancer. The DeleteLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource ide"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")

    if not store.load_balancer_tls_certificates(certificate_name):
        raise ResourceNotFoundException(f"Resource certificate_name not found")
    store.delete_load_balancer_tls_certificates(certificate_name)
    return {}
```
