# spec:trace: aws/glue/get-database.spec.py.md#implementation
# spec:id: @specs/aws/glue/get-database
# spec:generated: DO NOT EDIT — edit the spec instead

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

