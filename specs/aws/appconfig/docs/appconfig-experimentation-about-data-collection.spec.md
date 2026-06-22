---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-data-collection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS About data collection"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# About data collection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-data-collection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# About data collection
<a name="appconfig-experimentation-about-data-collection"></a>

While AWS AppConfig experimentation provides aggregate metrics on your experiment, it does not provide analytics for experiment results. The experiment dashboard includes real-time monitoring of experiment traffic. You can view audience exposure levels, treatment allocation over time, and traffic distribution across treatments.

For per-user metrics analysis, you can use CloudWatch, Snowflake, Datadog, or other analytics platforms. To monitor operational metrics, choose **View in CloudWatch** from the experiment dashboard to access operational metrics directly. With CloudWatch, you can monitor key metrics such as page load time, conversion rate, and error rates during an experiment run. You can also configure CloudWatch alarms to alert you when key metrics exceed acceptable thresholds during an experiment run.

For experiment results analysis such as conversion rates, user engagement, and feature adoption, use CloudWatch or your existing analytics platforms. You can export experiment data to data warehouses such as [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html), Snowflake, or Databricks. You can also integrate with monitoring tools such as Datadog, New Relic, or Dynatrace, or use AWS services such as Amazon S3 for durable data storage and [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to capture client-side user interactions. This approach gives you full control over how metrics are defined, collected, and interpreted.

**Exporting experiment assignment data**

To capture which users are assigned to which treatments during an experiment run, configure AWS AppConfig Agent with the `EXPERIMENT_ASSIGNMENT_LOG_DESTINATION` option. When configured, the agent writes assignment logs to the specified destination. If this option is not set, no assignment logs are emitted.

Currently, the agent supports writing logs to disk. Specify a file path as the destination value (for example, `file:/var/log/appconfig/experiments/`).

Assignment logs are stored in the following directory structure:

```
BASE_DIR/
  <region>/
    <account-id>/
      <application-id>/
        <experiment-definition-id>/
          <run-number>_<unique-id>.jsonl
```

Each log file contains one JSON record per line (JSONL format). Each record includes the timestamp, the treatment assignment, and the entity ID:

```
{"timestamp":"2026-01-01T12:00:00Z","treatmentKey":"__t1__","entityId":"user1"}
{"timestamp":"2026-01-01T12:00:01Z","treatmentKey":"__c__","entityId":"user2"}
```

After logs are written to disk, you are responsible for exporting them to persistent storage such as Amazon S3 or a data warehouse for analysis.

After you begin an experiment, verify that data collection works correctly for the selected audience. Ensure that tracking and logging are functioning as expected. Also, confirm that data is complete and available for analysis. Incomplete or inaccurate data can invalidate experiment results.