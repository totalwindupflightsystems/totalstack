---
id: "@specs/aws/iam/create_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateDelegationRequest"
---

# CreateDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_delegation_request
> **spec:implements:** @kind:operation CreateDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateDelegationRequest.spec.md

Creates an IAM delegation request for temporary access delegation. This API is not available for general use. In order to use this API, a caller first need to go through an onboarding process described in the partner onboarding documentation .

## Input Shape: CreateDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape | ✓ | A description of the delegation request. |
| NotificationChannel | Any  # complex shape | ✓ | The notification channel for updates about the delegation request. At this time,only SNS topic ARNs are accepted for not |
| OnlySendByOwner | Any  # complex shape |  | Specifies whether the delegation token should only be sent by the owner. This flag prevents any party other than the own |
| OwnerAccountId | Any  # complex shape |  | The Amazon Web Services account ID this delegation request is targeted to. If the account ID is not known, this paramete |
| Permissions | Any  # complex shape | ✓ | The permissions to be delegated in this delegation request. |
| RedirectUrl | Any  # complex shape |  | The URL to redirect to after the delegation request is processed. This URL is used by the IAM console to show a link to  |
| RequestMessage | Any  # complex shape |  | A message explaining the reason for the delegation request. Requesters can utilize this field to add a custom note to th |
| RequestorWorkflowId | Any  # complex shape | ✓ | The workflow ID associated with the requestor. This is the unique identifier on the partner side that can be used to tra |
| SessionDuration | Any  # complex shape | ✓ | The duration for which the delegated session should remain active, in seconds. The active time window for the session st |

## Output Shape: CreateDelegationRequestResponse

- **ConsoleDeepLink** (Any  # complex shape): A deep link URL to the Amazon Web Services Management Console for managing the delegation request. For a console based w
- **DelegationRequestId** (Any  # complex shape): The unique identifier for the created delegation request.

## Errors
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def create_delegation_request(store, request: dict) -> dict:
    """Creates an IAM delegation request for temporary access delegation. This API is not available for general use. In order to use this API, a caller first need to go through an onboarding process describe"""
    description = request.get("Description", "").strip() if isinstance(request.get("Description"), str) else request.get("Description")
    if not description:
        raise ValidationException("Description is required")
    notification_channel = request.get("NotificationChannel", "").strip() if isinstance(request.get("NotificationChannel"), str) else request.get("NotificationChannel")
    if not notification_channel:
        raise ValidationException("NotificationChannel is required")
    permissions = request.get("Permissions", "").strip() if isinstance(request.get("Permissions"), str) else request.get("Permissions")
    if not permissions:
        raise ValidationException("Permissions is required")
    requestor_workflow_id = request.get("RequestorWorkflowId", "").strip() if isinstance(request.get("RequestorWorkflowId"), str) else request.get("RequestorWorkflowId")
    if not requestor_workflow_id:
        raise ValidationException("RequestorWorkflowId is required")
    session_duration = request.get("SessionDuration", "").strip() if isinstance(request.get("SessionDuration"), str) else request.get("SessionDuration")
    if not session_duration:
        raise ValidationException("SessionDuration is required")

    if store.delegation_requests(requestor_workflow_id):
        raise ResourceInUseException(f"Resource requestor_workflow_id already exists")

    record = {
        "OwnerAccountId": owner_account_id,
        "Description": description,
        "Permissions": permissions,
        "RequestMessage": request_message,
        "RequestorWorkflowId": requestor_workflow_id,
        "RedirectUrl": redirect_url,
        "NotificationChannel": notification_channel,
        "SessionDuration": session_duration,
        "OnlySendByOwner": only_send_by_owner,
    }

    store.delegation_requests(requestor_workflow_id, record)

    return {
        "ConsoleDeepLink": record.get("ConsoleDeepLink", {}),
        "DelegationRequestId": record.get("DelegationRequestId", {}),
    }
```
