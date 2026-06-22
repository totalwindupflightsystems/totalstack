---
id: "@specs/aws/kafka/docs/enable-open-monitoring-at-creation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable open monitoring on new clusters"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Enable open monitoring on new clusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/enable-open-monitoring-at-creation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable open monitoring on new MSK Provisioned clusters
<a name="enable-open-monitoring-at-creation"></a>

This procedure describes how to enable open monitoring on a new MSK cluster using the AWS Management Console, the AWS CLI, or the Amazon MSK API.

**Using the AWS Management Console**

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the **Monitoring** section, select the check box next to **Enable open monitoring with Prometheus**.

1. Provide the required information in all the sections of the page, and review all the available options.

1. Choose **Create cluster**.

**Using the AWS CLI**
+ Invoke the [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/kafka/create-cluster.html) command and specify its `open-monitoring` option. Enable the `JmxExporter`, the `NodeExporter`, or both. If you specify `open-monitoring`, the two exporters can't be disabled at the same time.

**Using the API**
+ Invoke the [CreateCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#CreateCluster) operation and specify `OpenMonitoring`. Enable the `jmxExporter`, the `nodeExporter`, or both. If you specify `OpenMonitoring`, the two exporters can't be disabled at the same time.