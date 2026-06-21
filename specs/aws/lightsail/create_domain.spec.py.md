---
id: "@specs/aws/lightsail/create_domain"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDomain"
---

# CreateDomain

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_domain
> **spec:implements:** @kind:operation CreateDomain
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDomain.spec.md

Creates a domain resource for the specified domain (example.com). The create domain operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateDomainRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domainName | str | ✓ | The domain name to manage ( example.com ). |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateDomainResult

- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def create_domain(store, request: dict) -> dict:
    """Creates a domain resource for the specified domain (example.com). The create domain operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Develop"""
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.domains(domain_name):
        raise ResourceInUseException(f"Resource domain_name already exists")

    record = {
        "domainName": domain_name,
        "tags": tags,
    }

    store.domains(domain_name, record)

    return {
        "operation": record.get("operation", {}),
    }
```
