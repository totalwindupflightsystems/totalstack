---
id: "@specs/aws/ec2/get_instance_types_from_instance_requirements"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetInstanceTypesFromInstanceRequirements"
---

# GetInstanceTypesFromInstanceRequirements

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_instance_types_from_instance_requirements
> **spec:implements:** @kind:operation GetInstanceTypesFromInstanceRequirements
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetInstanceTypesFromInstanceRequirements.spec.md

Returns a list of instance types with the specified instance attributes. You can use the response to preview the instance types without launching instances. Note that the response does not consider capacity. When you specify multiple parameters, you get instance types that satisfy all of the specified parameters. If you specify multiple values for a parameter, you get instance types that satisfy any of the specified values. For more information, see Preview instance types with specified attributes , Specify attributes for instance type selection for EC2 Fleet or Spot Fleet , and Spot placement score in the Amazon EC2 User Guide , and Creating mixed instance groups using attribute-based instance type selection in the Amazon EC2 Auto Scaling User Guide .

## Input Shape: GetInstanceTypesFromInstanceRequirementsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ArchitectureTypes | Any  # complex shape | ✓ | The processor architecture type. |
| Context | str |  | Reserved. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceRequirements | Any  # complex shape | ✓ | The attributes required for the instance types. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VirtualizationTypes | Any  # complex shape | ✓ | The virtualization type. |

## Output Shape: GetInstanceTypesFromInstanceRequirementsResult

- **InstanceTypes** (Any  # complex shape): The instance types with the specified instance attributes.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def get_instance_types_from_instance_requirements(store, request: dict) -> dict:
    """Returns a list of instance types with the specified instance attributes. You can use the response to preview the instance types without launching instances. Note that the response does not consider ca"""
    architecture_types = request.get("ArchitectureTypes", "").strip() if isinstance(request.get("ArchitectureTypes"), str) else request.get("ArchitectureTypes")
    if not architecture_types:
        raise ValidationException("ArchitectureTypes is required")
    instance_requirements = request.get("InstanceRequirements", "").strip() if isinstance(request.get("InstanceRequirements"), str) else request.get("InstanceRequirements")
    if not instance_requirements:
        raise ValidationException("InstanceRequirements is required")
    virtualization_types = request.get("VirtualizationTypes", "").strip() if isinstance(request.get("VirtualizationTypes"), str) else request.get("VirtualizationTypes")
    if not virtualization_types:
        raise ValidationException("VirtualizationTypes is required")

    resource = store.instance_types_from_instance_requirementss(architecture_types)
    if not resource:
        raise ResourceNotFoundException(f"Resource architecture_types not found")
    return {"ArchitectureTypes": architecture_types, **resource}
```
