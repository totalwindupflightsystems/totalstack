---
id: "@specs/aws/lambda/docs/monitoring-metrics-view"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View function metrics"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# View function metrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/monitoring-metrics-view
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Viewing metrics for Lambda functions
<a name="monitoring-metrics-view"></a>

Use the CloudWatch console to view metrics for your Lambda functions. In the console, you can filter and sort function metrics by function name, alias, version, or event source mapping UUID.

**To view metrics on the CloudWatch console**

1. Open the [Metrics page](https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#metricsV2:graph=~();namespace=~'AWS*2fLambda) (`AWS/Lambda` namespace) of the CloudWatch console.

1. On the **Browse** tab, under **Metrics**, choose any of the following dimensions:
   + **By Function Name** (`FunctionName`) – View aggregate metrics for all versions and aliases of a function.
   + **By Resource** (`Resource`) – View metrics for a version or alias of a function.
   + **By Executed Version** (`ExecutedVersion`) – View metrics for a combination of alias and version. Use the `ExecutedVersion` dimension to compare error rates for two versions of a function that are both targets of a [weighted alias](configuration-aliases.md).
   + **By Event Source Mapping UUID** (`EventSourceMappingUUID`) – View metrics for an event source mapping.
   + **Across All Functions** (none) – View aggregate metrics for all functions in the current AWS Region.

1. Choose a metric. The metric should automatically appear in the visual graph, as well as under the **Graphed metrics** tab.

By default, graphs use the `Sum` statistic for all metrics. To choose a different statistic and customize the graph, use the options on the **Graphed metrics** tab.

**Note**  
The timestamp on a metric reflects when the function was invoked. Depending on the duration of the invocation, this can be several minutes before the metric is emitted. For example, if your function has a 10-minute timeout, then look more than 10 minutes in the past for accurate metrics.

For more information about CloudWatch, see the [ Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).