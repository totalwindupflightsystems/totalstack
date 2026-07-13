---
id: "@specs/aws/lambda/docs/with-msk-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure permissions"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Configure permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-msk-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Lambda permissions for Amazon MSK event source mappings
<a name="with-msk-permissions"></a>

To access the Amazon MSK cluster, your function and event source mapping need permissions to perform various Amazon MSK API actions. Add these permissions to the function's [execution role](lambda-intro-execution-role.md). If your users need access, add the required permissions to the identity policy for the user or role.

The [AWSLambdaMSKExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.html) managed policy contains the minimum required permissions for Amazon MSK Lambda event source mappings. To simplify the permissions process, you can:
+ Attach the [AWSLambdaMSKExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.html) managed policy to your execution role.
+ Let the Lambda console generate the permissions for you. When you [create an Amazon MSK event source mapping in the console](msk-esm-create.md#msk-console), Lambda evaluates your execution role and alerts you if any permissions are missing. Choose **Generate permissions** to automatically update your execution role. This doesn't work if you manually created or modified your execution role policies, or if the policies are attached to multiple roles. Note that additional permissions may still be required in your execution role when using advanced features such as [On-Failure Destination](kafka-on-failure.md) or [AWS Glue Schema Registry](services-consume-kafka-events.md).

**Topics**
+ [Required permissions](#msk-required-permissions)
+ [Optional permissions](#msk-optional-permissions)

## Required permissions
<a name="msk-required-permissions"></a>

Your Lambda function execution role must have the following required permissions for Amazon MSK event source mappings. These permissions are included in the [AWSLambdaMSKExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.html) managed policy.

### CloudWatch Logs permissions
<a name="msk-basic-permissions"></a>

The following permissions allow Lambda to create and store logs in Amazon CloudWatch Logs.
+ [logs:CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [logs:CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [logs:PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

### MSK cluster permissions
<a name="msk-cluster-permissions"></a>

The following permissions allow Lambda to access your Amazon MSK cluster on your behalf:
+ [kafka:DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html)
+ [kafka:DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html)
+ [kafka:GetBootstrapBrokers](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html)

We recommend using [kafka:DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html) instead of [kafka:DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html). The v2 permission works with both provisioned and serverless Amazon MSK clusters. You only need one of these permissions in your policy.

### VPC permissions
<a name="msk-vpc-permissions"></a>

The following permissions allow Lambda to create and manage network interfaces when connecting to your Amazon MSK cluster:
+ [ec2:CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [ec2:DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [ec2:DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

## Optional permissions
<a name="msk-optional-permissions"></a>

 Your Lambda function might also need permissions to: 
+ Access cross-account Amazon MSK clusters. For cross-account event source mappings, you need [kafka:DescribeVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection-arn.html) in the execution role. An IAM principal creating a cross-account event source mapping needs [kafka:ListVpcConnections](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections.html).
+ Access your SCRAM secret, if you're using [SASL/SCRAM authentication](msk-cluster-auth.md#msk-sasl-scram). This lets your function use a username and password to connect to Kafka.
+ Describe your Secrets Manager secret, if you're using SASL/SCRAM or [mTLS authentication](msk-cluster-auth.md#msk-mtls). This allows your function to retrieve the credentials or certificates needed for secure connections.
+ Access your AWS KMS customer managed key, if your AWS Secrets Manager secret is encrypted with an AWS KMS customer managed key.
+ Access your schema registry secrets, if you're using a schema registry with authentication:
  + For AWS Glue Schema Registry: Your function needs `glue:GetRegistry` and `glue:GetSchemaVersion` permissions. These allow your function to look up and use the message format rules stored in AWS Glue.
  + For [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/security/index.html) with `BASIC_AUTH` or `CLIENT_CERTIFICATE_TLS_AUTH`: Your function needs `secretsmanager:GetSecretValue` permission for the secret containing the authentication credentials. This lets your function retrieve the username/password or certificates needed to access the Confluent Schema Registry.
  + For private CA certificates: Your function needs secretsmanager:GetSecretValue permission for the secret containing the certificate. This allows your function to verify the identity of schema registries that use custom certificates.
+ Access Kafka cluster consumer groups and poll messages from the topic, if you're using IAM authentication for the event source mapping.

 These correspond to the following required permissions: 
+ [kafka:ListScramSecrets](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html) - Allows listing of SCRAM secrets for Kafka authentication
+ [secretsmanager:GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) - Enables retrieval of secrets from Secrets Manager
+ [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) - Permits decryption of encrypted data using AWS KMS
+ [glue:GetRegistry](https://docs.aws.amazon.com/glue/latest/webapi/API_GetRegistry.html) - Allows access to AWS Glue Schema Registry
+ [glue:GetSchemaVersion](https://docs.aws.amazon.com/glue/latest/webapi/API_GetSchemaVersion.html) - Enables retrieval of specific schema versions from AWS Glue Schema Registry
+ [kafka-cluster:Connect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html) - Grants permission to connect and authenticate to the cluster
+ [kafka-cluster:AlterGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html) - Grants permission to join groups on a cluster, equivalent to Apache Kafka's READ GROUP ACL
+ [kafka-cluster:DescribeGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html) - Grants permission to describe groups on a cluster, equivalent to Apache Kafka's DESCRIBE GROUP ACL
+ [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html) - Grants permission to describe topics on a cluster, equivalent to Apache Kafka's DESCRIBE TOPIC ACL
+ [kafka-cluster:ReadData](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html) - Grants permission to read data from topics on a cluster, equivalent to Apache Kafka's READ TOPIC ACL

 Additionally, if you want to send records of failed invocations to an on-failure destination, you'll need the following permissions depending on the destination type: 
+ For Amazon SQS destinations: [sqs:SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) - Allows sending messages to an Amazon SQS queue
+ For Amazon SNS destinations: [sns:Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) - Permits publishing messages to an Amazon SNS topic
+ For Amazon S3 bucket destinations: [s3:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) and [s3:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucket.html) - Enables writing and listing objects in an Amazon S3 bucket

For troubleshooting authentication and authorization errors, see [Troubleshooting Kafka event source mapping errors](with-kafka-troubleshoot.md).