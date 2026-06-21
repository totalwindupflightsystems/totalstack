---
id: "@specs/aws/lightsail/update_domain_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateDomainEntry"
---

# UpdateDomainEntry

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_domain_entry
> **spec:implements:** @kind:operation UpdateDomainEntry
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateDomainEntry.spec.md

Updates a domain recordset after it is created. The update domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: UpdateDomainEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domainEntry | Any  # complex shape | ✓ | An array of key-value pairs containing information about the domain entry. |
| domainName | str | ✓ | The name of the domain recordset to update. |

## Output Shape: UpdateDomainEntryResult

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
def update_domain_entry(store, request: dict) -> dict:
    """Updates a domain recordset after it is created. The update domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more infor"""
    domain_entry = request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    if not domain_entry:
        raise ValidationException("domainEntry is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    resource = store.domain_entrys(domain_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource domain_name not found")

    # Update mutable fields

    store.domain_entrys(domain_name, resource)
    return resource
```
