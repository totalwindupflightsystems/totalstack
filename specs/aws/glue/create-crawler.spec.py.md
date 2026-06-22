---
id: "@specs/aws/glue/create-crawler"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/glue/meta"
  - "@specs/aws/glue/plan"
---

# CreateCrawler — AWS Glue

> **@ref:** specs/aws/glue/glue.spec.plan.md
> **spec:trace:** specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
> **spec:id:** @specs/aws/glue/create-crawler

## AWS API Contract

Creates a new crawler with specified targets, role, configuration, and optional schedule.

**Request:** `{ "Name": "string", "Role": "string", "Targets": {...}, "DatabaseName": "string", "Description": "string", "Schedule": "string" }`
**Response:** `{ "Name": "string" }`
**Errors:** `AlreadyExistsException`, `InvalidInputException`

## Implementation

```speclang
# spec:trace: specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
# spec:id: @specs/aws/glue/create-crawler
# spec:generated: DO NOT EDIT — edit the spec instead

def handler(store, request: dict) -> dict:
    """Create a new Glue crawler."""
    name = request.get("Name")
    if not name:
        raise InvalidInputException("Name is required")

    if store.crawlers(name):
        raise AlreadyExistsException(f"Crawler '{name}' already exists")

    record = {
        "Name": name,
        "Role": request.get("Role", ""),
        "Targets": request.get("Targets", {}),
        "DatabaseName": request.get("DatabaseName", ""),
        "Description": request.get("Description", ""),
        "Schedule": request.get("Schedule", ""),
        "State": "READY",
        "CreationTime": int(__import__("time").time()),
    }
    store.crawlers(name, record)
    return {"Name": name}
```
