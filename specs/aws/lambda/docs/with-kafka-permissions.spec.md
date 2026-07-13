---
id: "@specs/aws/lambda/docs/with-kafka-permissions"
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
> **spec:id:** @specs/aws/lambda/docs/with-kafka-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Lambda execution role permissions
<a name="with-kafka-permissions"></a>

In addition to [accessing your self-managed Kafka cluster](kafka-cluster-auth.md), your Lambda function needs permissions to perform various API actions. You add these permissions to the function's [execution role](lambda-intro-execution-role.md). If your users need access to any API actions, add the required permissions to the identity policy for the AWS Identity and Access Management (IAM) user or role.

**Topics**
+ [Required Lambda function permissions](#smaa-api-actions-required)
+ [Optional Lambda function permissions](#smaa-api-actions-optional)
+ [Adding permissions to your execution role](#smaa-permissions-add-policy)
+ [Granting users access with an IAM policy](#smaa-permissions-add-users)

## Required Lambda function permissions
<a name="smaa-api-actions-required"></a>

To create and store logs in a log group in Amazon CloudWatch Logs, your Lambda function must have the following permissions in its execution role:
+ [logs:CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [logs:CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [logs:PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

## Optional Lambda function permissions
<a name="smaa-api-actions-optional"></a>

Your Lambda function might also need permissions to:
+ Describe your Secrets Manager secret.
+ Access your AWS Key Management Service (AWS KMS) customer managed key.
+ Access your Amazon VPC.
+ Send records of failed invocations to a destination.

### Secrets Manager and AWS KMS permissions
<a name="smaa-api-actions-secrets"></a>

Depending on the type of access control that you're configuring for your Kafka brokers, your Lambda function might need permission to access your Secrets Manager secret or to decrypt your AWS KMS customer managed key. To access these resources, your function's execution role must have the following permissions:
+ [secretsmanager:GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)
+ [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)

### VPC permissions
<a name="smaa-api-actions-vpc"></a>

If only users within a VPC can access your self-managed Apache Kafka cluster, your Lambda function must have permission to access your Amazon VPC resources. These resources include your VPC, subnets, security groups, and network interfaces. To access these resources, your function's execution role must have the following permissions:
+ [ec2:CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [ec2:DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [ec2:DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

## Adding permissions to your execution role
<a name="smaa-permissions-add-policy"></a>

To access other AWS services that your self-managed Apache Kafka cluster uses, Lambda uses the permissions policies that you define in your Lambda function's [execution role](lambda-intro-execution-role.md).

By default, Lambda is not permitted to perform the required or optional actions for a self-managed Apache Kafka cluster. You must create and define these actions in an [IAM trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-trust-policy.html) for your execution role. This example shows how you might create a policy that allows Lambda to access your Amazon VPC resources.

------
#### [ JSON ]

****  

```
{
        "Version":"2012-10-17",		 	 	 
        "Statement":[
           {
              "Effect":"Allow",
              "Action":[
                 "ec2:CreateNetworkInterface",
                 "ec2:DescribeNetworkInterfaces",
                 "ec2:DescribeVpcs",
                 "ec2:DeleteNetworkInterface",
                 "ec2:DescribeSubnets",
                 "ec2:DescribeSecurityGroups"
              ],
              "Resource":"*"
           }
        ]
     }
```

------

## Granting users access with an IAM policy
<a name="smaa-permissions-add-users"></a>

By default, users and roles don't have permission to perform [event source API operations](invocation-eventsourcemapping.md#event-source-mapping-api). To grant access to users in your organization or account, you create or update an identity-based policy. For more information, see [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html) in the *IAM User Guide*.

For troubleshooting authentication and authorization errors, see [Troubleshooting Kafka event source mapping errors](with-kafka-troubleshoot.md).