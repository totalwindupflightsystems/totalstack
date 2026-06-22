---
id: "@specs/aws/glue/create-database"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/glue/meta"
  - "@specs/aws/glue/plan"
  - "@specs/aws/glue/docs/create-databases-tables-s3-catalog"
---

# CreateDatabase — AWS Glue

> **@ref:** specs/aws/glue/docs/create-databases-tables-s3-catalog.spec.md
> **@ref:** specs/aws/glue/glue.spec.meta.md
> **@ref:** specs/aws/glue/glue.spec.plan.md
> **spec:trace:** specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
> **spec:id:** @specs/aws/glue/create-database

## AWS API Contract

Creates a new database in the Glue Data Catalog.

**Request:** `{ "Name": "string", "CatalogId": "string", "Description": "string", "LocationUri": "string", "Parameters": {"string": "string"} }`
**Response:** `{ "Name": "string" }`
**Errors:** `AlreadyExistsException`, `InvalidInputException`, `InternalServiceException`

## Implementation

```speclang
# spec:trace: specs/aws/glue/docs/create-databases-tables-s3-catalog.spec.md
# spec:id: @specs/aws/glue/create-database
# spec:generated: DO NOT EDIT — edit the spec instead

import uuid

def handler(store, request: dict) -> dict:
    """Create a new Glue database in the Data Catalog."""
    # Validate required field
    name = request.get("Name")
    if not name or not isinstance(name, str):
        raise InvalidInputException("Name is required and must be a string")

    catalog_id = request.get("CatalogId", "default")

    # Check for duplicate
    if store.databases(name, catalog_id):
        raise AlreadyExistsException(f"Database '{name}' already exists in catalog '{catalog_id}'")

    # Build record
    record = {
        "Name": name,
        "CatalogId": catalog_id,
        "Description": request.get("Description", ""),
        "LocationUri": request.get("LocationUri", ""),
        "Parameters": request.get("Parameters", {}),
        "CreateTime": int(__import__("time").time()),
    }

    store.databases(name, catalog_id, record)
    return {"Name": name}
```
