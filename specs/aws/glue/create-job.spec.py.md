---
id: "@specs/aws/glue/create-job"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/glue/meta"
  - "@specs/aws/glue/plan"
---

# CreateJob — AWS Glue

> **@ref:** specs/aws/glue/glue.spec.plan.md
> **spec:trace:** specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
> **spec:id:** @specs/aws/glue/create-job

## AWS API Contract

Creates a new Glue ETL job definition.

**Request:** `{ "Name": "string", "Role": "string", "Command": {"Name": "string", "ScriptLocation": "string", "PythonVersion": "string"}, "Description": "string", "MaxRetries": number, "Timeout": number }`
**Response:** `{ "Name": "string" }`
**Errors:** `AlreadyExistsException`, `InvalidInputException`

## Implementation

```speclang
# spec:trace: specs/aws/glue/glue.spec.plan.md#phase-1-core-crud
# spec:id: @specs/aws/glue/create-job
# spec:generated: DO NOT EDIT — edit the spec instead

def handler(store, request: dict) -> dict:
    """Create a new Glue ETL job definition."""
    name = request.get("Name")
    if not name:
        raise InvalidInputException("Name is required")

    if store.jobs(name):
        raise AlreadyExistsException(f"Job '{name}' already exists")

    record = {
        "Name": name,
        "Role": request.get("Role", ""),
        "Command": request.get("Command", {}),
        "Description": request.get("Description", ""),
        "MaxRetries": request.get("MaxRetries", 0),
        "Timeout": request.get("Timeout", 2880),
        "CreatedOn": int(__import__("time").time()),
        "LastModifiedOn": int(__import__("time").time()),
    }
    store.jobs(name, record)
    return {"Name": name}
```
