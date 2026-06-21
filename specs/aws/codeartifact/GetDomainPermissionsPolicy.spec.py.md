---
id: "@specs/aws/codeartifact/domain_policy_get"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# GetDomainPermissionsPolicy

Returns the resource policy attached to the specified domain.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Name of the domain |
| `domainOwner` | AccountId | No | Domain owner account ID |

## Errors
- `AccessDeniedException`, `InternalServerException`, `ResourceNotFoundException`, `ThrottlingException`, `ValidationException`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_get_domain_permissions_policy(store, request):
    """Returns the resource policy attached to the specified domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    domain = store._get_domain(domain_name)
    policy = store.domain_policies.get(domain_name, "")
    return {"policy": {"resourceArn": domain.arn, "document": policy, "revision": str(uuid.uuid4().hex[:8])}}
```
