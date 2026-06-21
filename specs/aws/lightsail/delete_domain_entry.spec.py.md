---
id: "@specs/aws/lightsail/delete_domain_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteDomainEntry"
---

# DeleteDomainEntry

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_domain_entry
> **spec:implements:** @kind:operation DeleteDomainEntry
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteDomainEntry.spec.md

Deletes a specific domain entry. The delete domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteDomainEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domainEntry | Any  # complex shape | ✓ | An array of key-value pairs containing information about your domain entries. |
| domainName | str | ✓ | The name of the domain entry to delete. |

## Output Shape: DeleteDomainEntryResult

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
def delete_domain_entry(store, request: dict) -> dict:
    """Deletes a specific domain entry. The delete domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the"""
    domain_entry = request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")

    if not store.domain_entrys(domain_name):
        raise ResourceNotFoundException(f"Resource domain_name not found")
    store.delete_domain_entrys(domain_name)
    return {}
```
