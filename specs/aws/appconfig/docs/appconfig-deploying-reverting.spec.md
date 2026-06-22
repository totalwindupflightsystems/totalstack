---
id: "@specs/aws/appconfig/docs/appconfig-deploying-reverting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Reverting a configuration"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Reverting a configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-deploying-reverting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Reverting a configuration
<a name="appconfig-deploying-reverting"></a>

During a deployment, you can mitigate situations where malformed or incorrect configuration data causes errors in your application by using automatic rollbacks (if an alarm triggers during a deployment) or by reverting the configuration data to the previous version (if a deployment successfully completed).

For automatic rollbacks, you can use a combination of AWS AppConfig [deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html) and Amazon CloudWatch alarms. Once configured, if one or more CloudWatch alarms go into the `ALARM` state during a deployment, AWS AppConfig automatically rolls back your configuration data to the previous version, thereby preventing application outages or errors. To get started, see [Configure permissions for automatic rollback](setting-up-appconfig.md#getting-started-with-appconfig-cloudwatch-alarms-permissions).

**Note**  
You can also roll back a configuration by calling the [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html) API operation while a deployment is still in progress.

For deployments that successfully complete, AWS AppConfig also supports reverting configuration data to a previous version by using the `AllowRevert` parameter with the [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html) API operation. For some customers, reverting to a previous configuration after a successful deployment guarantees the data will be the same as it was before the deployment. Reverting also ignores alarm monitors, which may prevent a roll forward from progressing during an application emergency.

**Important**  
If you call `StopDeployment` with the `AllowRevert` parameter enabled, AWS AppConfig will revert the deployment only if the deployment succeeded within the last 72 hours. After 72 hours, the deployment can no longer be reverted. You must create a new deployment.

Here's a breakdown of the `StopDeployment` functionality based on different situations.

1. If `StopDeployment` is called on an in-progress deployment, the resulting deployment state will be `ROLLED_BACK`.

1. If `StopDeployment` (with `AllowRevert`) is called on an in-progress deployment, the resulting deployment state will be `ROLLED_BACK`.

1. If `StopDeployment` is called on a completed deployment, a `BadRequestException` will be thrown.

1. If `StopDeployment` (with `AllowRevert`) is called on a completed deployment, the resulting deployment state will be `REVERTED`.

1. If `StopDeployment` (with `AllowRevert`) is called on a completed deployment after 72 hours, a `BadRequestException` will be thrown.

You can use the AWS CLI to call the [StopDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html) operation with the `AllowRevert` parameter. Here's an example AWS CLI command that includes the `AllowRevert` parameter.

```
aws appconfig stop-deployment \
    --application-id 339ohji \
    --environment-id 54j1r29 \
    --deployment-number 2 \
    --allow-revert
```