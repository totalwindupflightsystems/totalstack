---
id: "@specs/aws/elasticache/CreateUser"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateUser

For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user. For more information, see Using Role Based Access Control (RBAC).

## Input Shape: CreateUserMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserId | UserId | ✓ |
| UserName | UserName | ✓ |
| Engine | EngineType | ✓ |
| Passwords | PasswordListInput |  |
| AccessString | AccessString | ✓ |
| NoPasswordRequired | BooleanOptional |  |
| Tags | TagList |  |
| AuthenticationMode | AuthenticationMode |  |

## Output Shape: User
- UserId: String
- UserName: String
- Status: String
- Engine: EngineType
- MinimumEngineVersion: String
- AccessString: String
- UserGroupIds: UserGroupIdList
- Authentication: Authentication
- ARN: String

## Errors
UserAlreadyExistsFault, UserQuotaExceededFault, DuplicateUserNameFault, ServiceLinkedRoleNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def create_user(store, request):
    """Handle CreateUser — create a new resource."""
    if "UserId" not in request or not request["UserId"]:
        raise InvalidParameterValueException("UserId is required")
    if "UserName" not in request or not request["UserName"]:
        raise InvalidParameterValueException("UserName is required")
    if "Engine" not in request or not request["Engine"]:
        raise InvalidParameterValueException("Engine is required")
    if "AccessString" not in request or not request["AccessString"]:
        raise InvalidParameterValueException("AccessString is required")
    resource_name = request["UserId"]
    if resource_name in store.users:
        raise UserAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.users[resource_name] = record

    # Build response
    response = {}
    response["UserId"] = resource_name
    response["Status"] = "available"
    return response
```
