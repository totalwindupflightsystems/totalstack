---
id: "@specs/aws/cloudformation/estimate_template_cost"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_EstimateTemplateCost"
---

# EstimateTemplateCost

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/estimate_template_cost
> **spec:implements:** @kind:operation EstimateTemplateCost
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_EstimateTemplateCost.spec.md

Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

## Input Shape: EstimateTemplateCostInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Parameters | Any  # complex shape |  | A list of Parameter structures that specify input parameters. |
| TemplateBody | Any  # complex shape |  | Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. Conditio |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template that's located in an Amazon S3 bucke |

## Output Shape: EstimateTemplateCostOutput

- **Url** (Any  # complex shape): An Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run th

## Implementation

```speclang
def estimate_template_cost(store, request: dict) -> dict:
    """Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("EstimateTemplateCost", request)
```
