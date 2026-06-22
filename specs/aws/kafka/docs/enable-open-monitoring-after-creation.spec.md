---
id: "@specs/aws/kafka/docs/enable-open-monitoring-after-creation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable open monitoring on existing Provisioned clusters"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Enable open monitoring on existing Provisioned clusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/enable-open-monitoring-after-creation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable open monitoring on existing MSK Provisioned cluster
<a name="enable-open-monitoring-after-creation"></a>

To enable open monitoring, make sure that the MSK Provisioned cluster is in the `ACTIVE` state.

**Using the AWS Management Console**

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the name of the cluster that you want to update. This takes you to a page the contains details for the cluster.

1. On the **Properties** tab, scroll down to find the **Monitoring** section.

1. Choose **Edit**.

1. Select the check box next to **Enable open monitoring with Prometheus**.

1. Choose **Save changes**.

**Using the AWS CLI**
+ Invoke the [update-monitoring](https://docs.aws.amazon.com/cli/latest/reference/kafka/update-monitoring.html) command and specify its `open-monitoring` option. Enable the `JmxExporter`, the `NodeExporter`, or both. If you specify `open-monitoring`, the two exporters can't be disabled at the same time.

**Using the API**
+ Invoke the [UpdateMonitoring](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-monitoring.html#UpdateMonitoring) operation and specify `OpenMonitoring`. Enable the `jmxExporter`, the `nodeExporter`, or both. If you specify `OpenMonitoring`, the two exporters can't be disabled at the same time.