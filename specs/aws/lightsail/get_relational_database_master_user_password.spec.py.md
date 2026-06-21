---
id: "@specs/aws/lightsail/get_relational_database_master_user_password"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRelationalDatabaseMasterUserPassword"
---

# GetRelationalDatabaseMasterUserPassword

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_relational_database_master_user_password
> **spec:implements:** @kind:operation GetRelationalDatabaseMasterUserPassword
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRelationalDatabaseMasterUserPassword.spec.md

Returns the current, previous, or pending versions of the master user password for a Lightsail database. The GetRelationalDatabaseMasterUserPassword operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName.

## Input Shape: GetRelationalDatabaseMasterUserPasswordRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| passwordVersion | Any  # complex shape |  | The password version to return. Specifying CURRENT or PREVIOUS returns the current or previous passwords respectively. S |
| relationalDatabaseName | Any  # complex shape | ✓ | The name of your database for which to get the master user password. |

## Output Shape: GetRelationalDatabaseMasterUserPasswordResult

- **createdAt** (Any  # complex shape): The timestamp when the specified version of the master user password was created.
- **masterUserPassword** (Any  # complex shape): The master user password for the password version specified.

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
def get_relational_database_master_user_password(store, request: dict) -> dict:
    """Returns the current, previous, or pending versions of the master user password for a Lightsail database. The GetRelationalDatabaseMasterUserPassword operation supports tag-based access control via res"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_master_user_passwords(relational_database_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}
```
