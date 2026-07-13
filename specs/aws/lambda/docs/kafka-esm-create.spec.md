---
id: "@specs/aws/lambda/docs/kafka-esm-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event source mapping"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Event source mapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-esm-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a Lambda event source mapping for a self-managed Apache Kafka event source
<a name="kafka-esm-create"></a>

To create an event source mapping, you can use the Lambda console, the [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), or an [AWS SDK](https://aws.amazon.com/getting-started/tools-sdks/).

The following console steps add a self-managed Apache Kafka cluster as a trigger for your Lambda function. Under the hood, this creates an event source mapping resource.

## Prerequisites
<a name="kafka-esm-prereqs"></a>
+ A self-managed Apache Kafka cluster. Lambda supports Apache Kafka version 0.10.1.0 and later.
+ An [execution role](lambda-intro-execution-role.md) with permission to access the AWS resources that your self-managed Kafka cluster uses.

## Adding a self-managed Kafka cluster (console)
<a name="kafka-esm-console"></a>

Follow these steps to add your self-managed Apache Kafka cluster and a Kafka topic as a trigger for your Lambda function.

**To add an Apache Kafka trigger to your Lambda function (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your Lambda function.

1. Under **Function overview**, choose **Add trigger**.

1. Under **Trigger configuration**, do the following:

   1. Choose the **Apache Kafka** trigger type.

   1. For **Bootstrap servers**, enter the host and port pair address of a Kafka broker in your cluster, and then choose **Add**. Repeat for each Kafka broker in the cluster.

   1. For **Topic name**, enter the name of the Kafka topic used to store records in the cluster.

   1. If you configure provisioned mode, enter a value for **Minimum event pollers**, a value for **Maximum event pollers**, and an optional value for PollerGroupName to specify grouping of multiple ESMs within the same event source VPC.

   1. (Optional) For **Batch size**, enter the maximum number of records to receive in a single batch.

   1. For **Batch window**, enter the maximum amount of seconds that Lambda spends gathering records before invoking the function.

   1. (Optional) For **Consumer group ID**, enter the ID of a Kafka consumer group to join.

   1. (Optional) For **Starting position**, choose **Latest** to start reading the stream from the latest record, **Trim horizon** to start at the earliest available record, or **At timestamp** to specify a timestamp to start reading from.

   1. (Optional) For **VPC**, choose the Amazon VPC for your Kafka cluster. Then, choose the **VPC subnets** and **VPC security groups**.

      This setting is required if only users within your VPC access your brokers.

      

   1. (Optional) For **Authentication**, choose **Add**, and then do the following:

      1. Choose the access or authentication protocol of the Kafka brokers in your cluster.
         + If your Kafka broker uses SASL/PLAIN authentication, choose **BASIC\_AUTH**.
         + If your broker uses SASL/SCRAM authentication, choose one of the **SASL\_SCRAM** protocols.
         + If you're configuring mTLS authentication, choose the **CLIENT\_CERTIFICATE\_TLS\_AUTH** protocol.

      1. For SASL/SCRAM or mTLS authentication, choose the Secrets Manager secret key that contains the credentials for your Kafka cluster.

   1. (Optional) For **Encryption**, choose the Secrets Manager secret containing the root CA certificate that your Kafka brokers use for TLS encryption, if your Kafka brokers use certificates signed by a private CA.

      This setting applies to TLS encryption for SASL/SCRAM or SASL/PLAIN, and to mTLS authentication.

   1. To create the trigger in a disabled state for testing (recommended), clear **Enable trigger**. Or, to enable the trigger immediately, select **Enable trigger**.

1. To create the trigger, choose **Add**.

## Adding a self-managed Kafka cluster (AWS CLI)
<a name="kafka-esm-cli"></a>

Use the following example AWS CLI commands to create and view a self-managed Apache Kafka trigger for your Lambda function.

### Using SASL/SCRAM
<a name="kafka-esm-cli-create"></a>

If Kafka users access your Kafka brokers over the internet, specify the Secrets Manager secret that you created for SASL/SCRAM authentication. The following example uses the [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html) AWS CLI command to map a Lambda function named `my-kafka-function` to a Kafka topic named `AWSKafkaTopic`.

```
aws lambda create-event-source-mapping \ 
  --topics {{AWSKafkaTopic}} \
  --source-access-configuration Type=SASL_SCRAM_512_AUTH,URI=arn:aws:secretsmanager:us-east-1:{{111122223333}}:secret:{{MyBrokerSecretName}} \
  --function-name arn:aws:lambda:us-east-1:{{111122223333}}:function:{{my-kafka-function}} \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["{{abc3.xyz.com:9092}}", "{{abc2.xyz.com:9092}}"]}}'
```

### Using a VPC
<a name="kafka-esm-cli-create-vpc"></a>

If only Kafka users within your VPC access your Kafka brokers, you must specify your VPC, subnets, and VPC security group. The following example uses the [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html) AWS CLI command to map a Lambda function named `my-kafka-function` to a Kafka topic named `AWSKafkaTopic`.

```
aws lambda create-event-source-mapping \ 
  --topics {{AWSKafkaTopic}} \
  --source-access-configuration '[{"Type": "VPC_SUBNET", "URI": "subnet:subnet-0011001100"}, {"Type": "VPC_SUBNET", "URI": "subnet:subnet-0022002200"}, {"Type": "VPC_SECURITY_GROUP", "URI": "security_group:sg-0123456789"}]' \
  --function-name arn:aws:lambda:us-east-1:{{111122223333}}:function:{{my-kafka-function}} \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["{{abc3.xyz.com:9092}}", "{{abc2.xyz.com:9092}}"]}}'
```

### Viewing the status using the AWS CLI
<a name="kafka-esm-cli-view"></a>

The following example uses the [get-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html) AWS CLI command to describe the status of the event source mapping that you created.

```
aws lambda get-event-source-mapping
              --uuid {{dh38738e-992b-343a-1077-3478934hjkfd7}}
```