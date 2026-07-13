---
id: "@specs/aws/cloudformation/list_generated_templates"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListGeneratedTemplates"
---

# ListGeneratedTemplates

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_generated_templates
> **spec:implements:** @kind:operation ListGeneratedTemplates
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListGeneratedTemplates.spec.md

Lists your generated templates in this Region.

## Input Shape: ListGeneratedTemplatesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | If the number of available results exceeds this maximum, the response includes a NextToken value that you can use for th |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |

## Output Shape: ListGeneratedTemplatesOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **Summaries** (Any  # complex shape): A list of summaries of the generated templates.

## Implementation

```speclang
def list_generated_templates(store, request: dict) -> dict:
    """Lists your generated templates in this Region."""

    items = store.list_generated_templatess()
    return {"Summaries": list(items.values())}
```
