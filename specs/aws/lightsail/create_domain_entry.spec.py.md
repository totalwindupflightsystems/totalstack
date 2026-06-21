---
id: "@specs/aws/lightsail/create_domain_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDomainEntry"
---

# CreateDomainEntry

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_domain_entry
> **spec:implements:** @kind:operation CreateDomainEntry
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDomainEntry.spec.md

Creates one of the following domain name system (DNS) records in a domain DNS zone: Address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT). The create domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateDomainEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domainEntry | Any  # complex shape | ✓ | An array of key-value pairs containing information about the domain entry request. |
| domainName | str | ✓ | The domain name ( example.com ) for which you want to create the domain entry. |

## Output Shape: CreateDomainEntryResult

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
def create_domain_entry(store, request: dict) -> dict:
    """Creates one of the following domain name system (DNS) records in a domain DNS zone: Address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locato"""
    domain_entry = request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    if not domain_entry:
        raise ValidationException("domainEntry is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.domain_entrys(domain_name):
        raise ResourceInUseException(f"Resource domain_name already exists")

    record = {
        "domainName": domain_name,
        "domainEntry": domain_entry,
    }

    store.domain_entrys(domain_name, record)

    return {
        "operation": record.get("operation", {}),
    }
```
