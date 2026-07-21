# spec:trace: aws/glue/create-database.spec.py.md#implementation
# spec:id: @specs/aws/glue/create-database
# spec:generated: DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/glue/docs/create-databases-tables-s3-catalog.spec.md
# spec:id: @specs/aws/glue/create-database
# spec:generated: DO NOT EDIT — edit the spec instead


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
    return {}

