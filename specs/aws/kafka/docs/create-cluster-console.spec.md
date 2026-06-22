---
id: "@specs/aws/kafka/docs/create-cluster-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a cluster using AWS Management Console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a cluster using AWS Management Console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-cluster-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create an MSK Provisioned cluster using the AWS Management Console
<a name="create-cluster-console"></a>

The procedures in this topic describe the common task of creating an MSK Provisioned cluster using the **Custom create** option in the AWS Management Console. Using other options available in the AWS Management Console, you can also create the following:
+ [A serverless cluster](create-serverless-cluster.md)
+ [An MSK Provisioned cluster](create-cluster.md) using the **Quick create** option

****Procedures in this topic
+ [Step 1: Initial cluster setup and configuration](#cluster-initial-setup)
+ [Step 2: Configure the storage and cluster settings](#cluster-storage-config)
+ [Step 3: Configure the network settings](#cluster-network-config)
+ [Step 4: Configure the security settings](#cluster-security-settings-config)
+ [Step 5: Configure monitoring options](#cluster-monitoring-config)
+ [Step 6: Review the cluster configuration](#review-cluster-custom-create)

## Step 1: Initial cluster setup and configuration
<a name="cluster-initial-setup"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Choose **Create cluster**.

1. For **Cluster creation method**, choose **Custom create**.

1. For **Cluster name**, specify a name that is unique and contains no more than 64 characters.

1. For **Cluster type**, choose **Provisioned**.

1. For **Apache Kafka version**, choose a version to run on the brokers. To see a comparison of Amazon MSK features that are supported by each Apache Kafka version, choose **View version compatibility**.

1. In the **Brokers** section, do the following:

   1. For **Broker type**, choose one of the following options:
      + **Express brokers**: High-performance, scalable brokers with fully managed virtual storage. Choose this broker type for demanding, high-throughput applications.
      + **Standard brokers**: Traditional Kafka broker with full configuration control. Choose this broker type for general-purpose workloads with moderate throughput requirements.

      For more information about these broker types, see [Amazon MSK broker types](broker-instance-types.md).

   1. For **Broker size**, choose a size to use for the cluster based on the cluster’s compute, memory, and storage needs.

   1. For **Number of zones**, choose the number of [AWS Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html) across which brokers are distributed.

      Express brokers require three Availability Zones for higher availability.

   1. For **Brokers per zone**, specify the number of brokers you want Amazon MSK to create in each Availability Zone. The minimum is one broker per Availability Zone and the maximum is 30 brokers per cluster for ZooKeeper-based clusters and 60 brokers per cluster for [KRaft-based clusters](metadata-management.md#kraft-intro).

## Step 2: Configure the storage and cluster settings
<a name="cluster-storage-config"></a>

This procedure describes how you can configure your data storage needs across all brokers and specify the storage mode. This helps you define your data storage requirements based on your workload needs. Additionally, this procedure describes the cluster configuration settings that control how your brokers operate. These settings include broker configurations, default topic settings, and tiered storage policy.

1. If you selected the broker type as **Standard**, do the following in the **Storage** section:

   1. For **Storage**, choose the initial amount of storage you want your cluster to have. You can't decrease storage capacity after you create the cluster.

   1. (Optional) Depending on the broker size (instance size) you selected, you can also specify **Provisioned storage throughput per broker**. This option allows you to allocate dedicated input and output (I/O) performance for the Amazon EBS volumes of each broker.

      To enable this option, choose broker size (instance size) kafka.m5.4xlarge or larger for x86, and kafka.m7g.2xlarge or larger for Graviton-based instances. Then, choose the **Enable provisioned storage throughput** checkbox. By selecting this checkbox, you can manually set a minimum of 250 MiB per second of throughput. This is helpful for I/O-intensive workloads or applications that require high-speed, predictable storage performance. For more information, see [Provision storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput.md).

   1. For **Cluster storage mode**, specify how data is stored and managed within your cluster. This option determines the type and configuration of storage used for your brokers. Choose one of the following options:
      + **EBS storage only**: Stores all topic data locally on Amazon Elastic Block Store (Amazon EBS) volumes attached to each broker. Choose this mode for consistent performance needs and fast access to recent messages.
      + **Tiered storage and EBS storage**: Combines local Amazon EBS data with remote, cost-efficient storage for large datasets in Amazon S3. This mode reduces Amazon EBS storage costs, supports longer data retention, and scales storage automatically without manual intervention. Choose this mode when you want to retain data for longer periods at lower cost, or expect your storage needs to grow significantly.
**Note**  
You don't need to manage storage for Express brokers.

1. For **Cluster configuration**, specify one of the following options to define your cluster's behavior:
   + **Amazon MSK default configuration**: Contains a predefined set of configurations optimized for general-purpose use cases. Choose this option for quick cluster setup and deployment. For information about Amazon MSK configurations, see [Amazon MSK Provisioned configuration](msk-configuration.md).
   + **Custom configuration**: Lets you specify your own broker and topic settings. You can either choose an existing, custom configuration from the list or create a new custom configuration. Choose this option for fine-tuned control for your brokers, such as specific performance tuning, security settings, and more.

   

1. Choose **Next** to proceed.

## Step 3: Configure the network settings
<a name="cluster-network-config"></a>

Network configuration defines how your cluster is deployed within your AWS infrastructure. This includes VPC, Availability Zones and subnets, and security groups that control networking, availability, and access.

1. For **Networking**, do the following:

   1. Choose the VPC you want to use for the cluster.

   1. Based on the number of Availability Zones you previously selected, specify the Availability Zones and subnets where brokers will deploy. 

      For Standard brokers in the US West (N. California) Region, you need two subnets in two different Availability Zones. In all other Regions where Amazon MSK is available, you can specify either two or three subnets. Your subnets must all be in different Availability Zones.

      For Express brokers, you need three subnets in three different Availability Zones.

      When you create an MSK Provisioned cluster, MSK distributes the broker nodes evenly over the subnets that you specify.

   1. For **Security groups in Amazon EC2**, choose or create one or more security groups that you want to give access to your cluster. These Amazon EC2 security groups control inbound and outbound traffic to your brokers. For example, the security groups of client machines.

      If you specify security groups that are shared with you, you must ensure that you have permissions to use them. Specifically, you need the `ec2:DescribeSecurityGroups` permission. For more information, see [Connecting to an MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html#public-access).

1. Choose **Next** to proceed.

## Step 4: Configure the security settings
<a name="cluster-security-settings-config"></a>

1. In the **Security settings** section, do the following:

   1. Choose one or more of the following authentication and authorization methods to control client access to your Kafka clusters:
     + **Unauthenticated access**: Allows clients to access the cluster without providing any authentication credentials. This method is a security risk and might not comply with security best practices. For more information, see [msk-unrestricted-access-check](https://docs.aws.amazon.com/config/latest/developerguide/msk-unrestricted-access-check.html).
     + **IAM role-based authentication**: Enables client authentication and authorization using AWS IAM users/roles. This method provides fine-grained control over cluster access through IAM policies. We recommended this method for applications already running in AWS.
     + **SASL/SCRAM authentication**: Requires clients to provide username and password credentials stored in AWS Secrets Manager for authentication. Amazon MSK retrieves these credentials from Secrets Manager and securely authenticates users.

       To set up sign-in credentials regarding authentication for a cluster, first create a Secret resource in Secrets Manager. Then, associate sign-in credentials with that secret. For more information about this access control method, see [Set up SASL/SCRAM authentication for an Amazon MSK clusterConnecting to your cluster with sign-in credentials](msk-password-tutorial.md).
     + **TLS client authentication through AWS Certificate Manager (ACM)**: Enables mutual authentication between clients and brokers using digital certificates. You must configure an AWS Private Certificate Authority (AWS Private CA) either in the same or different AWS account as your cluster.

       We strongly recommend using independent AWS Private CAs for each MSK cluster when implementing mTLS. This ensures that TLS certificates signed by PCAs only authenticate with a single MSK cluster, thereby maintaining strict access control.

1. In **Encryption**, choose the kind of KMS key that you want to use for encrypting data at rest. For more information, see [Amazon MSK encryption at rest](msk-encryption.md#msk-encryption-at-rest).

   Encrypting data at rest protects stored data integrity, while encrypting in transit protects data confidentiality from network monitoring during transfer.

1. Choose **Next** to proceed.

## Step 5: Configure monitoring options
<a name="cluster-monitoring-config"></a>

This procedure describes how to set up your broker metrics, and collect and deliver broker logs. With these settings, you can observe and analyze your cluster's health, performance, and troubleshoot issues. For more information, see [Monitor an Amazon MSK Provisioned cluster](monitoring.md).

1. For **Amazon CloudWatch metrics for this cluster**, choose one of the following monitoring levels. The metrics collected at each monitoring level are integrated with CloudWatch for visualization and alerting.

   1. **Basic monitoring**: Provides a set of essential cluster-level metrics at no additional cost. This level is good for for most use cases with general monitoring needs.

   1. **Enhanced broker-level monitoring**: Provides detailed broker metrics at additional cost. This level includes basic monitoring and more granular broker metrics, such as tiered storage metrics bytes in/out of other brokers, total time for read/write operations. You pay for the metrics in this level, whereas the basic level metrics continue to be free.

   1. **Enhanced topic-level monitoring**: Provides metrics for individual topics at additional cost. Choose this level to obtain a more granular view of topic performance across brokers. This level includes enhanced broker-level monitoring and topic-level metrics, such as tiered storage metrics for a specified topic and number of messages received per second.

   1. **Enhanced partition-level monitoring**: Provides the most granular view of metrics per partition at additional cost. Choose this level to obtain the most detailed monitoring by capturing metrics for each partition within each topic across brokers. This level includes enhanced topic-level monitoring and fine-grained partition-specific metrics, such as offset lag metrics.

   For more information about the metrics available for Standard and Express broker types at each of these monitoring levels, see [CloudWatch metrics for Standard brokers](metrics-details.md) and [CloudWatch metrics for Express brokers](metrics-details-express.md).

1. (Optional) If you want to export metrics in Prometheus format using JMX Exporter, Node Exporter, or both, choose **Enable open monitoring with Prometheus**. For more information about this option, see [Monitor with Prometheus](open-monitoring.md).

1. (Optional) To configure your MSK cluster to deliver broker logs to various AWS services for troubleshooting and auditing, choose one or more of the following options. Amazon MSK doesn't create these destination resources for you if they don't already exist. For more information, see [Broker logs](msk-logging.md#broker-logs).
   + **Deliver to Amazon CloudWatch Logs**: Sends logs to CloudWatch with clustering, searching, and visualization capabilities. You can query and analyze logs without leaving the AWS Management Console.
   + **Deliver to Amazon S3**: Stores logs as files in Amazon S3 buckets for long-term archiving and batch analysis.
   + **Deliver to Amazon Data Firehose**: Send logs to Firehose for automatic delivery to Amazon OpenSearch Service for real-time troubleshooting.

1. (Optional) To help identify, organize, or search for your cluster, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your cluster with the key-value pair of **Load testing** and **Test**.

   For more information about using tags in your clusters, see [Tag an Amazon MSK cluster](msk-tagging.md).

1. Choose **Next** to proceed.

## Step 6: Review the cluster configuration
<a name="review-cluster-custom-create"></a>

1. Review the settings for your cluster. 

   Choose **Edit** or **Previous** to change any of the settings you previously specified or go back to the previous console screen.

1. Choose **Create cluster**.

1. Check the status of this cluster in **Cluster summary** section of the Cluster details page. The status changes from **Creating** to **Active** as Amazon MSK provisions the cluster. When the status is **Active**, you can connect to the cluster. For more information about cluster status, see [Understand MSK Provisioned cluster states](msk-cluster-states.md).