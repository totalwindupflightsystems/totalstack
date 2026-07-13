---
id: "@specs/aws/cloudformation/get_template_summary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_GetTemplateSummary"
---

# GetTemplateSummary

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/get_template_summary
> **spec:implements:** @kind:operation GetTemplateSummary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_GetTemplateSummary.spec.md

Returns information about a new or existing template. The GetTemplateSummary action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or StackSet. You can use the GetTemplateSummary action when you submit a template, or you can get template information for a StackSet, or a running or deleted stack. For deleted stacks, GetTemplateSummary returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a ValidationError is returned.

## Input Shape: GetTemplateSummaryInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| StackName | Any  # complex shape |  | The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you  |
| StackSetName | Any  # complex shape |  | The name or unique ID of the StackSet from which the stack was created. Conditional: You must specify only one of the fo |
| TemplateBody | Any  # complex shape |  | Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. Conditio |
| TemplateSummaryConfig | Any  # complex shape |  | Specifies options for the GetTemplateSummary API action. |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in a |

## Output Shape: GetTemplateSummaryOutput

- **Capabilities** (Any  # complex shape): The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM
- **CapabilitiesReason** (Any  # complex shape): The list of resources that generated the values in the Capabilities response element.
- **DeclaredTransforms** (list[Any  # complex shape]): A list of the transforms that are declared in the template.
- **Description** (Any  # complex shape): The value that's defined in the Description property of the template.
- **Metadata** (Any  # complex shape): The value that's defined for the Metadata property of the template.
- **Parameters** (Any  # complex shape): A list of parameter declarations that describe various properties for each parameter.
- **ResourceIdentifierSummaries** (Any  # complex shape): A list of resource identifier summaries that describe the target resources of an import operation and the properties you
- **ResourceTypes** (Any  # complex shape): A list of all the template resource types that are defined in the template, such as AWS::EC2::Instance , AWS::Dynamo::Ta
- **Version** (Any  # complex shape): The Amazon Web Services template format version, which identifies the capabilities of the template.
- **Warnings** (Any  # complex shape): An object that contains any warnings returned.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def get_template_summary(store, request: dict) -> dict:
    """Returns information about a new or existing template. The GetTemplateSummary action is useful for viewing parameter information, such as default parameter values and parameter types, before you create"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
