---
id: "@specs/aws/cloudformation/validate_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ValidateTemplate"
---

# ValidateTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/validate_template
> **spec:implements:** @kind:operation ValidateTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ValidateTemplate.spec.md

Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

## Input Shape: ValidateTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| TemplateBody | Any  # complex shape |  | Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. Conditio |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that is located in  |

## Output Shape: ValidateTemplateOutput

- **Capabilities** (Any  # complex shape): The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM
- **CapabilitiesReason** (Any  # complex shape): The list of resources that generated the values in the Capabilities response element.
- **DeclaredTransforms** (list[Any  # complex shape]): A list of the transforms that are declared in the template.
- **Description** (Any  # complex shape): The description found within the template.
- **Parameters** (Any  # complex shape): A list of TemplateParameter structures.

## Implementation

```speclang
def validate_template(store, request: dict) -> dict:
    """Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation r"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ValidateTemplate", request)
```
