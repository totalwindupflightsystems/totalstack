---
id: "@specs/aws/kafka/docs/cloudwatch-metrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View metrics using CloudWatch"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# View metrics using CloudWatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/cloudwatch-metrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View Amazon MSK metrics using CloudWatch
<a name="cloudwatch-metrics"></a>

You can monitor metrics for Amazon MSK using the CloudWatch console, the command line, or the CloudWatch API. The following procedures show you how to access metrics using these different methods. 

**To access metrics using the CloudWatch console**

Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Choose the **All metrics** tab, and then choose **AWS/Kafka**.

1. To view topic-level metrics, choose **Topic, Broker ID, Cluster Name**; for broker-level metrics, choose **Broker ID, Cluster Name**; and for cluster-level metrics, choose **Cluster Name**.

1. (Optional) In the graph pane, select a statistic and a time period, and then create a CloudWatch alarm using these settings.

**To access metrics using the AWS CLI**  
Use the [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) and [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) commands.

**To access metrics using the CloudWatch CLI**  
Use the [mon-list-metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-list-metrics.html) and [mon-get-stats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-get-stats.html) commands.

**To access metrics using the CloudWatch API**  
Use the [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) and [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) operations.