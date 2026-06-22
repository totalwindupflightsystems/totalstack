---
id: "@specs/aws/kafka/docs/cluster-alerts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use storage capacity alerts"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Use storage capacity alerts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/cluster-alerts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use Amazon MSK storage capacity alerts
<a name="cluster-alerts"></a>

On Amazon MSK provisioned clusters, you choose the cluster's primary storage capacity. If you exhaust the storage capacity on a broker in your provisioned cluster, it can affect its ability to produce and consume data, leading to costly downtime. Amazon MSK offers CloudWatch metrics to help you monitor your cluster's storage capacity. However, to make it easier for you to detect and resolve storage capacity issues, Amazon MSK automatically sends you dynamic cluster storage capacity alerts. The storage capacity alerts include recommendations for short-term and long-term steps to manage your cluster's storage capacity. From the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/), you can use quick links within the alerts to take recommended actions immediately.

There are two types of MSK storage capacity alerts: proactive and remedial.
+ Proactive ("Action required") storage capacity alerts warn you about potential storage issues with your cluster. When a broker in an MSK cluster has used over 60% or 80% of its disk storage capacity, you'll receive proactive alerts for the affected broker. 
+ Remedial ("Critical action required") storage capacity alerts require you to take remedial action to fix a critical cluster issue when one of the brokers in your MSK cluster has run out of disk storage capacity.

Amazon MSK automatically sends these alerts to the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/), [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health/), [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/), and email contacts for your AWS account. You can also [configure Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html) to deliver these alerts to Slack or to tools such as New Relic, and Datadog. 

Storage capacity alerts are enabled by default for all MSK provisioned clusters and can't be turned off. This feature is supported in all regions where MSK is available.

## Monitor storage capacity alerts
<a name="cluster-alerts-monitoring"></a>

You can check for storage capacity alerts in several ways:
+ Go to the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/). Storage capacity alerts are displayed in the cluster alerts pane for 90 days. The alerts contain recommendations and single-click link actions to address disk storage capacity issues.
+ Use [ListClusters](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#ListClusters), [ListClustersV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html#ListClustersV2), [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster), or [DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html#DescribeClusterV2) APIs to view `CustomerActionStatus` and all the alerts for a cluster.
+ Go to the [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health/) to view alerts from MSK and other AWS services.
+ Set up [AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html) to route alert notifications to 3rd party platforms such as Datadog, NewRelic, and Slack.