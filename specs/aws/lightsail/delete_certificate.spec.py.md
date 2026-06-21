---
id: "@specs/aws/lightsail/delete_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteCertificate"
---

# DeleteCertificate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_certificate
> **spec:implements:** @kind:operation DeleteCertificate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteCertificate.spec.md

Deletes an SSL/TLS certificate for your Amazon Lightsail content delivery network (CDN) distribution. Certificates that are currently attached to a distribution cannot be deleted. Use the DetachCertificateFromDistribution action to detach a certificate from a distribution.

## Input Shape: DeleteCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape | ✓ | The name of the certificate to delete. Use the GetCertificates action to get a list of certificate names that you can sp |

## Output Shape: DeleteCertificateResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def delete_certificate(store, request: dict) -> dict:
    """Deletes an SSL/TLS certificate for your Amazon Lightsail content delivery network (CDN) distribution. Certificates that are currently attached to a distribution cannot be deleted. Use the DetachCertif"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")

    if not store.certificates(certificate_name):
        raise ResourceNotFoundException(f"Resource certificate_name not found")
    store.delete_certificates(certificate_name)
    return {}
```
