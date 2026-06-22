---
id: "@specs/aws/kafka/docs/create-iam-access-control-cluster-in-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a Amazon MSK cluster that uses IAM access control"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a Amazon MSK cluster that uses IAM access control

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-iam-access-control-cluster-in-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Amazon MSK cluster that uses IAM access control
<a name="create-iam-access-control-cluster-in-console"></a>

This section explains how you can use the AWS Management Console, the API, or the AWS CLI to create a Amazon MSK cluster that uses IAM access control. For information about how to turn on IAM access control for an existing cluster, see [Update security settings of a Amazon MSK cluster](msk-update-security.md).

**Use the AWS Management Console to create a cluster that uses IAM access control**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Choose **Create cluster**.

1. Choose **Create cluster with custom settings**.

1. In the **Authentication** section, choose **IAM access control**.

1. Complete the rest of the workflow for creating a cluster.

**Use the API or the AWS CLI to create a cluster that uses IAM access control**
+ To create a cluster with IAM access control enabled, use the [CreateCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#CreateCluster) API or the [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-cluster.html) CLI command, and pass the following JSON for the `ClientAuthentication` parameter: `"ClientAuthentication": { "Sasl": { "Iam": { "Enabled": true } }`. 