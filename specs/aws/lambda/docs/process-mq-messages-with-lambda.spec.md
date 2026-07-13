---
id: "@specs/aws/lambda/docs/process-mq-messages-with-lambda"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure event source"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Configure event source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/process-mq-messages-with-lambda
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Amazon MQ event source for Lambda
<a name="process-mq-messages-with-lambda"></a>

**Topics**
+ [Configure network security](#process-mq-messages-with-lambda-networkconfiguration)
+ [Create the event source mapping](#services-mq-eventsourcemapping)

## Configure network security
<a name="process-mq-messages-with-lambda-networkconfiguration"></a>

To give Lambda full access to Amazon MQ through your event source mapping, either your broker must use a public endpoint (public IP address), or you must provide access to the Amazon VPC you created the broker in.

When you use Amazon MQ with Lambda, create [AWS PrivateLink VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) that provide your function access to the resources in your Amazon VPC.

**Note**  
AWS PrivateLink VPC endpoints are required for functions with event source mappings that use the default (on-demand) mode for event pollers. If your event source mapping uses [ provisioned mode](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode), you don't need to configure AWS PrivateLink VPC endpoints.

Create an endpoint to provide access to the following resources:
+  Lambda — Create an endpoint for the Lambda service principal. 
+  AWS STS — Create an endpoint for the AWS STS in order for a service principal to assume a role on your behalf. 
+  Secrets Manager — If your broker uses Secrets Manager to store credentials, create an endpoint for Secrets Manager. 

Alternatively, configure a NAT gateway on each public subnet in the Amazon VPC. For more information, see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md).

When you create an event source mapping for Amazon MQ, Lambda checks whether Elastic Network Interfaces (ENIs) are already present for the subnets and security groups configured for your Amazon VPC. If Lambda finds existing ENIs, it attempts to re-use them. Otherwise, Lambda creates new ENIs to connect to the event source and invoke your function.

**Note**  
Lambda functions always run inside VPCs owned by the Lambda service. Your function's VPC configuration does not affect the event source mapping. Only the networking configuration of the event source's determines how Lambda connects to your event source.

Configure the security groups for the Amazon VPC containing your broker. By default, Amazon MQ uses the following ports: `61617` (Amazon MQ for ActiveMQ), and `5671` (Amazon MQ for RabbitMQ).
+ Inbound rules – Allow all traffic on the default broker port for the security group associated with your event source. Alternatively, you can use a self-referencing security group rule to allow access from instances within the same security group.
+ Outbound rules – Allow all traffic on port `443` for external destinations if your function needs to communicate with AWS services. Alternatively, you can also use a self-referencing security group rule to limit access to the broker if you don't need to communicate with other AWS services.
+ Amazon VPC endpoint inbound rules — If you are using an Amazon VPC endpoint, the security group associated with your Amazon VPC endpoint must allow inbound traffic on port `443` from the broker security group.

If your broker uses authentication, you can also restrict the endpoint policy for the Secrets Manager endpoint. To call the Secrets Manager API, Lambda uses your function role, not the Lambda service principal.

**Example VPC endpoint policy — Secrets Manager endpoint**  

```
{
      "Statement": [
          {
              "Action": "secretsmanager:GetSecretValue",
              "Effect": "Allow",
              "Principal": {
                  "AWS": [
                      "arn:aws::iam::123456789012:role/{{my-role}}"
                  ]
              },
              "Resource": "arn:aws::secretsmanager:{{us-west-2}}:123456789012:secret:{{my-secret}}"
          }
      ]
  }
```

When you use Amazon VPC endpoints, AWS routes your API calls to invoke your function using the endpoint's Elastic Network Interface (ENI). The Lambda service principal needs to call `lambda:InvokeFunction` on any roles and functions that use those ENIs.

By default, Amazon VPC endpoints have open IAM policies that allow broad access to resources. Best practice is to restrict these policies to perform the needed actions using that endpoint. To ensure that your event source mapping is able to invoke your Lambda function, the VPC endpoint policy must allow the Lambda service principal to call `sts:AssumeRole` and `lambda:InvokeFunction`. Restricting your VPC endpoint policies to allow only API calls originating within your organization prevents the event source mapping from functioning properly, so `"Resource": "*"` is required in these policies.

The following example VPC endpoint policies show how to grant the required access to the Lambda service principal for the AWS STS and Lambda endpoints.

**Example VPC Endpoint policy — AWS STS endpoint**  

```
{
      "Statement": [
          {
              "Action": "sts:AssumeRole",
              "Effect": "Allow",
              "Principal": {
                  "Service": [
                      "lambda.amazonaws.com"
                  ]
              },
              "Resource": "*"
          }
      ]
    }
```

**Example VPC Endpoint policy — Lambda endpoint**  

```
{
      "Statement": [
          {
              "Action": "lambda:InvokeFunction",
              "Effect": "Allow",
              "Principal": {
                  "Service": [
                      "lambda.amazonaws.com"
                  ]
              },
              "Resource": "*"
          }
      ]
  }
```

## Create the event source mapping
<a name="services-mq-eventsourcemapping"></a>

Create an [event source mapping](invocation-eventsourcemapping.md) to tell Lambda to send records from an Amazon MQ broker to a Lambda function. You can create multiple event source mappings to process the same data with multiple functions, or to process items from multiple sources with a single function.

To configure your function to read from Amazon MQ, add the required permissions and create an **MQ** trigger in the Lambda console.

To read records from an Amazon MQ broker, your Lambda function needs the following permissions. You grant Lambda permission to interact with your Amazon MQ broker and its underlying resouces by adding permission statements to your function [execution role](lambda-intro-execution-role.md):
+ [mq:DescribeBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#brokers-broker-id-http-methods)
+ [secretsmanager:GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)
+ [ec2:CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [ec2:DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)
+ [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [ec2:DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [logs:CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [logs:CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [logs:PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

**Note**  
When using an encrypted customer managed key, add the `[kms:Decrypt](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#clusters-clusterarn-bootstrap-brokersget)` permission as well.

**To add permissions and create a trigger**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. Choose the **Configuration** tab, and then choose **Permissions**.

1. Under **Role name**, choose the link to your execution role. This link opens the role in the IAM console.  
![Link to execution role](http://docs.aws.amazon.com/lambda/latest/dg/images/execution-role.png)

1. Choose **Add permissions**, and then choose **Create inline policy**.  
![Create inline policy in IAM console](http://docs.aws.amazon.com/lambda/latest/dg/images/inline-policy.png)

1. In the **Policy editor**, choose **JSON**. Enter the following policy. Your function needs these permissions to read from an Amazon MQ broker.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "mq:DescribeBroker",
             "secretsmanager:GetSecretValue",
             "ec2:CreateNetworkInterface",
             "ec2:DeleteNetworkInterface",
             "ec2:DescribeNetworkInterfaces", 
             "ec2:DescribeSecurityGroups",
             "ec2:DescribeSubnets",
             "ec2:DescribeVpcs",
             "logs:CreateLogGroup",
             "logs:CreateLogStream", 
             "logs:PutLogEvents"		
           ],
           "Resource": "*"
         }
       ]
     }
   ```

------
**Note**  
When using an encrypted customer managed key, you must also add the `kms:Decrypt` permission.

1. Choose **Next**. Enter a policy name and then choose **Create policy**.

1. Go back to your function in the Lambda console. Under **Function overview**, choose **Add trigger**.  
![Function overview section of the Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/add-trigger.png)

1. Choose the **MQ** trigger type.

1. Configure the required options, and then choose **Add**.

Lambda supports the following options for Amazon MQ event sources:
+ **MQ broker** – Select an Amazon MQ broker.
+ **Batch size** – Set the maximum number of messages to retrieve in a single batch.
+ **Queue name** – Enter the Amazon MQ queue to consume.
+ **Source access configuration** – Enter virtual host information and the Secrets Manager secret that stores your broker credentials.
+ **Enable trigger** – Disable the trigger to stop processing records.

To enable or disable the trigger (or delete it), choose the **MQ** trigger in the designer. To reconfigure the trigger, use the event source mapping API operations.