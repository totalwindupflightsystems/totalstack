---
id: "@specs/aws/elasticache/ModifyUser"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyUser

Changes user password(s) and/or access string.

## Input Shape: ModifyUserMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserId | UserId | ✓ |
| AccessString | AccessString |  |
| AppendAccessString | AccessString |  |
| Passwords | PasswordListInput |  |
| NoPasswordRequired | BooleanOptional |  |
| AuthenticationMode | AuthenticationMode |  |
| Engine | EngineType |  |

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
UserNotFoundFault, InvalidUserStateFault, ServiceLinkedRoleNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def modify_user(store, request):
    """Handle ModifyUser — modify a resource."""
    resource_name = request.get("UserId")
    if not resource_name:
        raise InvalidParameterValueException("UserId is required")
    if resource_name not in store.users:
        raise UserNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.users[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["UserId"] = resource_name
    return response
```
