---
id: "@specs/aws/iam/get_human_readable_summary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetHumanReadableSummary"
---

# GetHumanReadableSummary

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_human_readable_summary
> **spec:implements:** @kind:operation GetHumanReadableSummary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetHumanReadableSummary.spec.md

Retrieves a human readable summary for a given entity. At this time, the only supported entity type is delegation-request This method uses a Large Language Model (LLM) to generate the summary. If a delegation request has no owner or owner account, GetHumanReadableSummary for that delegation request can be called by any account. If the owner account is assigned but there is no owner id, only identities within that owner account can call GetHumanReadableSummary for the delegation request to retrieve a summary of that request. Once the delegation request is fully owned, the owner of the request gets a default permission to get that delegation request. For more details, read default permissions granted to delegation requests . These rules are identical to GetDelegationRequest API behavior, such that a party who has permissions to call GetDelegationRequest for a given delegation request will always be able to retrieve the human readable summary for that request.

## Input Shape: GetHumanReadableSummaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EntityArn | Any  # complex shape | ✓ | Arn of the entity to be summarized. At this time, the only supported entity type is delegation-request |
| Locale | Any  # complex shape |  | A string representing the locale to use for the summary generation. The supported locale strings are based on the Suppor |

## Output Shape: GetHumanReadableSummaryResponse

- **Locale** (Any  # complex shape): The locale that this response was generated for. This maps to the input locale.
- **SummaryContent** (Any  # complex shape): Summary content in the specified locale. Summary content is non-empty only if the SummaryState is AVAILABLE .
- **SummaryState** (Any  # complex shape): State of summary generation. This generation process is asynchronous and this attribute indicates the state of the gener

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_human_readable_summary(store, request: dict) -> dict:
    """Retrieves a human readable summary for a given entity. At this time, the only supported entity type is delegation-request This method uses a Large Language Model (LLM) to generate the summary. If a de"""
    entity_arn = request.get("EntityArn", "").strip() if isinstance(request.get("EntityArn"), str) else request.get("EntityArn")
    if not entity_arn:
        raise ValidationException("EntityArn is required")

    resource = store.human_readable_summarys(entity_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource entity_arn not found")
    return {"EntityArn": entity_arn, **resource}
```
