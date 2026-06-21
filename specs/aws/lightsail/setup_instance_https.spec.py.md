---
id: "@specs/aws/lightsail/setup_instance_https"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_SetupInstanceHttps"
---

# SetupInstanceHttps

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/setup_instance_https
> **spec:implements:** @kind:operation SetupInstanceHttps
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_SetupInstanceHttps.spec.md

Creates an SSL/TLS certificate that secures traffic for your website. After the certificate is created, it is installed on the specified Lightsail instance. If you provide more than one domain name in the request, at least one name must be less than or equal to 63 characters in length.

## Input Shape: SetupInstanceHttpsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateProvider | Any  # complex shape | ✓ | The certificate authority that issues the SSL/TLS certificate. |
| domainNames | list[Any  # complex shape] | ✓ | The name of the domain and subdomains that were specified for the SSL/TLS certificate. |
| emailAddress | Any  # complex shape | ✓ | The contact method for SSL/TLS certificate renewal alerts. You can enter one email address. |
| instanceName | Any  # complex shape | ✓ | The name of the Lightsail instance. |

## Output Shape: SetupInstanceHttpsResult

- **operations** (list[Any  # complex shape]): The available API operations for SetupInstanceHttps .

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def setup_instance_https(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate that secures traffic for your website. After the certificate is created, it is installed on the specified Lightsail instance. If you provide more than one domain name in"""
    certificate_provider = request.get("certificateProvider", "").strip() if isinstance(request.get("certificateProvider"), str) else request.get("certificateProvider")
    if not certificate_provider:
        raise ValidationException("certificateProvider is required")
    domain_names = request.get("domainNames", "").strip() if isinstance(request.get("domainNames"), str) else request.get("domainNames")
    if not domain_names:
        raise ValidationException("domainNames is required")
    email_address = request.get("emailAddress", "").strip() if isinstance(request.get("emailAddress"), str) else request.get("emailAddress")
    if not email_address:
        raise ValidationException("emailAddress is required")
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.setup_instance_httpss(certificate_provider)
    if not resource:
        raise ResourceNotFoundException(f"Resource certificate_provider not found")

    # Update mutable fields

    store.setup_instance_httpss(certificate_provider, resource)
    return resource
```
