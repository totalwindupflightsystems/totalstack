---
id: "@specs/aws/lightsail/get_domain"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDomain"
---

# GetDomain

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_domain
> **spec:implements:** @kind:operation GetDomain
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDomain.spec.md

Returns information about a specific domain recordset.

## Input Shape: GetDomainRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domainName | str | ✓ | The domain name for which your want to return information about. |

## Output Shape: GetDomainResult

- **domain** (Any  # complex shape): An array of key-value pairs containing information about your get domain request.

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
def get_domain(store, request: dict) -> dict:
    """Returns information about a specific domain recordset."""
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    resource = store.domains(domain_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource domain_name not found")
    return {"domainName": domain_name, **resource}
```
