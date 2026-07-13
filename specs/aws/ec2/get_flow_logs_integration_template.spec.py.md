---
id: "@specs/aws/ec2/get_flow_logs_integration_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetFlowLogsIntegrationTemplate"
---

# GetFlowLogsIntegrationTemplate

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_flow_logs_integration_template
> **spec:implements:** @kind:operation GetFlowLogsIntegrationTemplate
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetFlowLogsIntegrationTemplate.spec.md

Generates a CloudFormation template that streamlines and automates the integration of VPC flow logs with Amazon Athena. This make it easier for you to query and gain insights from VPC flow logs data. Based on the information that you provide, we configure resources in the template to do the following: Create a table in Athena that maps fields to a custom log format Create a Lambda function that updates the table with new partitions on a daily, weekly, or monthly basis Create a table partitioned between two timestamps in the past Create a set of named queries in Athena that you can use to get started quickly GetFlowLogsIntegrationTemplate does not support integration between Amazon Web Services Transit Gateway Flow Logs and Amazon Athena.

## Input Shape: GetFlowLogsIntegrationTemplateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConfigDeliveryS3DestinationArn | str | ✓ | To store the CloudFormation template in Amazon S3, specify the location in Amazon S3. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FlowLogId | Any  # complex shape | ✓ | The ID of the flow log. |
| IntegrateServices | Any  # complex shape | ✓ | Information about the service integration. |

## Output Shape: GetFlowLogsIntegrationTemplateResult

- **Result** (str): The generated CloudFormation template.

## Implementation

```speclang
def get_flow_logs_integration_template(store, request: dict) -> dict:
    """Generates a CloudFormation template that streamlines and automates the integration of VPC flow logs with Amazon Athena. This make it easier for you to query and gain insights from VPC flow logs data. """
    config_delivery_s3_destination_arn = request.get("ConfigDeliveryS3DestinationArn", "").strip() if isinstance(request.get("ConfigDeliveryS3DestinationArn"), str) else request.get("ConfigDeliveryS3DestinationArn")
    if not config_delivery_s3_destination_arn:
        raise ValidationException("ConfigDeliveryS3DestinationArn is required")
    flow_log_id = request.get("FlowLogId", "").strip() if isinstance(request.get("FlowLogId"), str) else request.get("FlowLogId")
    if not flow_log_id:
        raise ValidationException("FlowLogId is required")
    integrate_services = request.get("IntegrateServices", "").strip() if isinstance(request.get("IntegrateServices"), str) else request.get("IntegrateServices")
    if not integrate_services:
        raise ValidationException("IntegrateServices is required")

    resource = store.flow_logs_integration_templates(flow_log_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource flow_log_id not found")
    return {"FlowLogId": flow_log_id, **resource}
```
