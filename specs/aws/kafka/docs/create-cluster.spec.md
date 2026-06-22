---
id: "@specs/aws/kafka/docs/create-cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a cluster"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 1: Create an MSK Provisioned cluster
<a name="create-cluster"></a>

In this step of [Getting Started Using Amazon MSK](getting-started.md), you create an Amazon MSK Provisioned cluster. You use the **Quick create** option in the AWS Management Console to create this cluster.

**To create an Amazon MSK cluster using the AWS Management Console**Create a cluster using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose **Create cluster**.

1. For **Creation method**, leave the **Quick create** option selected. The **Quick create** option lets you create a cluster with default settings.

1. For **Cluster name**, enter a descriptive name for your cluster. For example, **MSKTutorialCluster**.

1. For **General cluster properties**, do the following:

   1. For **Cluster type**, choose **Provisioned**.

   1. Choose an **Apache Kafka version** to run on the brokers. Choose **View version compatibility** to see a comparison table.

   1. For **Broker type**, choose either Standard or Express brokers.

   1. Choose a **Broker size**.

1. From the table under **All cluster settings**, copy the values of the following settings and save them because you need them later in this tutorial:
   + VPC
   + Subnets
   + Security groups associated with VPC

1. Choose **Create cluster**.

1. Check the cluster **Status** on the **Cluster summary** page. The status changes from **Creating** to **Active** as Amazon MSK provisions the cluster. When the status is **Active**, you can connect to the cluster. For more information about cluster status, see [Understand MSK Provisioned cluster states](msk-cluster-states.md).

**Next Step**

[Step 2: Create an IAM role granting access to create topics on the Amazon MSK cluster](create-client-iam-role.md)