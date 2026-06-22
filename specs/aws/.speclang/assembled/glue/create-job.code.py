# spec:trace: aws/glue/create-job.spec.py.md#implementation
# spec:id: @specs/aws/glue/create-job
# spec:generated: DO NOT EDIT — edit the spec instead

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

