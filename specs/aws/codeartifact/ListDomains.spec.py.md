---
id: "@specs/aws/codeartifact/list_domains"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/codeartifact/plan"
---

# ListDomains

Returns a list of DomainSummary objects for all domains owned by the AWS account making the call.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `maxResults` | Integer | No | Maximum number of results (1-1000, default 100) |
| `nextToken` | PaginationToken | No | Token for next page |

## Output Members
- `domains` (DomainSummary list): name, owner, arn, status, createdTime, encryptionKey
- `nextToken` (PaginationToken): token for next page or None

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_domains(store, request):
    """Returns a list of DomainSummary objects for all domains owned by the AWS account."""
    max_results = request.get("maxResults", 100)
    next_token = request.get("nextToken", None)

    domains = sorted(store.domains.values(), key=lambda d: d.name)

    if next_token:
        try:
            start_idx = int(next_token)
            domains = domains[start_idx:]
        except (ValueError, IndexError):
            pass

    items = domains[:max_results]
    result = {
        "domains": [
            {
                "name": d.name,
                "owner": d.owner,
                "arn": d.arn,
                "status": d.status,
                "createdTime": d.created_time,
                "encryptionKey": d.encryption_key,
            }
            for d in items
        ]
    }

    if len(domains) > max_results:
        result["nextToken"] = str(max_results)

    return result
```
