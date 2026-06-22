---
id: "@specs/aws/opensearchserverless/docs/auto-tune-schedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scheduling Auto-Tune enhancements"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Scheduling Auto-Tune enhancements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/auto-tune-schedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Scheduling Auto-Tune enhancements
<a name="auto-tune-schedule"></a>

Prior to February 16, 2023, Auto-Tune used *maintenance windows* to schedule changes that required a blue/green deployment. Maintenance windows are now deprecated in favor of the [off-peak window](off-peak.md), which is a daily 10-hour time block during which your domain typically experiences low traffic. You can modify the default start time for the off-peak window, but you can't modify the length.

Any domains that had Auto-Tune maintenance windows enabled before the introduction of off-peak windows on February 16, 2023 can continue to use legacy maintenance windows with no interruption. However, we recommend that you migrate your existing domains to use the off-peak window for domain maintenance instead. For instructions, see [Migrating from Auto-Tune maintenance windows](off-peak.md#off-peak-migrate).

## Console
<a name="auto-tune-schedule-console"></a>

**To schedule Auto-Tune actions the off-peak window**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home ).

1. In the navigation pane, under **Domains**, choose the domain name to open the cluster configuration.

1. Go to the **Auto-Tune** tab and choose **Edit**.

1. In the domain details page, choose the **Auto-Tune** tab, then select **Edit** to turn on or off Auto-Tune for the domain.

1. Under **Schedule optimizations during off-peak window**, select **Off-peak window**.

1. Choose **Save changes**.

## CLI
<a name="auto-tune-schedule-cli"></a>

To configure your domain to schedule Auto-Tune actions during the configured off-peak window, include `UseOffPeakWindow` in the [UpdateDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html) request:

```
aws opensearch update-domain-config \
  --domain-name {{my-domain}} \
  --auto-tune-options DesiredState=ENABLED,UseOffPeakWindow=true,MaintenanceSchedules=null
```