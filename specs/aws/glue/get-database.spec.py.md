---
id: "@specs/aws/glue/get-database"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/glue/meta"
  - "@specs/aws/glue/plan"
  - "@specs/aws/glue/create-database"
---

# GetDatabase — AWS Glue

> **@ref:** specs/aws/glue/glue.spec.plan.md
> **spec:trace:** specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
> **spec:id:** @specs/aws/glue/get-database

## AWS API Contract

Retrieves a database definition from the Data Catalog.

**Request:** `{ "Name": "string", "CatalogId": "string" }`
**Response:** `{ "Database": { "Name": "string", "Description": "string", "LocationUri": "string", "Parameters": {"string": "string"}, "CreateTime": number } }`
**Errors:** `EntityNotFoundException`, `InvalidInputException`

## Implementation

```speclang
# spec:trace: specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
# spec:id: @specs/aws/glue/get-database
# spec:generated: DO NOT EDIT — edit the spec instead

def handler(store, request: dict) -> dict:
    """Retrieve a Glue database from the Data Catalog."""
    name = request.get("Name")
    if not name:
        raise InvalidInputException("Name is required")

    catalog_id = request.get("CatalogId", "default")
    db = store.databases(name, catalog_id)
    if not db:
        raise EntityNotFoundException(f"Database '{name}' not found in catalog '{catalog_id}'")

    return {"Database": db}
```
