---
id: "@specs/aws/opensearchserverless/docs/auto-tune-enable"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enabling or disabling Auto-Tune"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Enabling or disabling Auto-Tune

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/auto-tune-enable
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enabling or disabling Auto-Tune
<a name="auto-tune-enable"></a>

OpenSearch Service enables Auto-Tune by default on new domains. To enable or disable Auto-Tune on existing domains, we recommend using the console, which simplifies the process. Enabling Auto-Tune doesn't cause a blue/green deployment.

You currently can't enable or disable Auto-Tune using AWS CloudFormation.

## Console
<a name="auto-tune-enable-console"></a>

**To enable Auto-Tune on an existing domain**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home ).

1. In the navigation pane, under **Domains**, choose the domain name to open the cluster configuration.

1. In the domain details page, choose the **Auto-Tune** tab, then select **Edit** to turn on or off Auto-Tune for the domain.

1. Optionally, select **Off-peak window** to schedule optimizations that require a blue/green deployment during the domain's configured off-peak window. For more information, see [Scheduling Auto-Tune enhancements](auto-tune-schedule.md).

1. Choose **Save changes**.

## CLI
<a name="auto-tune-enable-cli"></a>

To enable Auto-Tune using the AWS CLI, send an [UpdateDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html) request:

```
aws opensearch update-domain-config \
  --domain-name {{my-domain}} \
  --auto-tune-options DesiredState=ENABLED
```