---
id: "@specs/aws/lightsail/update_relational_database_parameters"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateRelationalDatabaseParameters"
---

# UpdateRelationalDatabaseParameters

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_relational_database_parameters
> **spec:implements:** @kind:operation UpdateRelationalDatabaseParameters
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateRelationalDatabaseParameters.spec.md

Allows the update of one or more parameters of a database in Amazon Lightsail. Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which parameter updates are applied: dynamic or pending-reboot . Parameters marked with a dynamic apply type are applied immediately. Parameters marked with a pending-reboot apply type are applied only after the database is rebooted using the reboot relational database operation. The update relational database parameters operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: UpdateRelationalDatabaseParametersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| parameters | list[Any  # complex shape] | ✓ | The database parameters to update. |
| relationalDatabaseName | Any  # complex shape | ✓ | The name of your database for which to update parameters. |

## Output Shape: UpdateRelationalDatabaseParametersResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def update_relational_database_parameters(store, request: dict) -> dict:
    """Allows the update of one or more parameters of a database in Amazon Lightsail. Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. H"""
    parameters = request.get("parameters", "").strip() if isinstance(request.get("parameters"), str) else request.get("parameters")
    if not parameters:
        raise ValidationException("parameters is required")
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_parameterss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource relational_database_name not found")

    # Update mutable fields

    store.relational_database_parameterss(relational_database_name, resource)
    return resource
```
