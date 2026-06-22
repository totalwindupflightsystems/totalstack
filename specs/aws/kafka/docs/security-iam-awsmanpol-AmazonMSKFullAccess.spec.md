---
id: "@specs/aws/kafka/docs/security-iam-awsmanpol-AmazonMSKFullAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managed policy AmazonMSKFullAccess"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Managed policy AmazonMSKFullAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security-iam-awsmanpol-AmazonMSKFullAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policy: AmazonMSKFullAccess
<a name="security-iam-awsmanpol-AmazonMSKFullAccess"></a>

This policy grants administrative permissions that allow a principal full access to all Amazon MSK actions. The permissions in this policy are grouped as follows:
+ The Amazon MSK permissions allow all Amazon MSK actions.
+ **`Amazon EC2` permissions** – in this policy are required to validate the passed resources in an API request. This is to make sure Amazon MSK is able to successfully use the resources with a cluster. The rest of the Amazon EC2 permissions in this policy allow Amazon MSK to create AWS resources that are needed to make it possible for you to connect to your clusters.
+ **`AWS KMS` permissions** – are used during API calls to validate the passed resources in a request. They are required for Amazon MSK to be able to use the passed key with the Amazon MSK cluster.
+ **`CloudWatch Logs, Amazon S3, and Amazon Data Firehose` permissions** – are required for Amazon MSK to be able to ensure that the log delivery destinations are reachable, and that they are valid for broker log use.
+ **`IAM` permissions** – are required for Amazon MSK to be able to a create service-linked role in your account and to allow you to pass a service execution role to Amazon MSK.

------
#### [ JSON ]

****  

```
    {
    	"Version":"2012-10-17",		 	 	 
    	"Statement": [{
    			"Effect": "Allow",
    			"Action": [
    				"kafka:*",
    				"ec2:DescribeSubnets",
    				"ec2:DescribeVpcs",
    				"ec2:DescribeSecurityGroups",
    				"ec2:DescribeRouteTables",
    				"ec2:DescribeVpcEndpoints",
    				"ec2:DescribeVpcAttribute",
    				"kms:DescribeKey",
    				"kms:CreateGrant",
    				"logs:CreateLogDelivery",
    				"logs:GetLogDelivery",
    				"logs:UpdateLogDelivery",
    				"logs:DeleteLogDelivery",
    				"logs:ListLogDeliveries",
    				"logs:PutResourcePolicy",
    				"logs:DescribeResourcePolicies",
    				"logs:DescribeLogGroups",
    				"S3:GetBucketPolicy",
    				"firehose:TagDeliveryStream"
    			],
    			"Resource": "*"
    		},
    		{
    			"Effect": "Allow",
    			"Action": [
    				"ec2:CreateVpcEndpoint"
    			],
    			"Resource": [
    				"arn:*:ec2:*:*:vpc/*",
    				"arn:*:ec2:*:*:subnet/*",
    				"arn:*:ec2:*:*:security-group/*"
    			]
    		},
    		{
    			"Effect": "Allow",
    			"Action": [
    				"ec2:CreateVpcEndpoint"
    			],
    			"Resource": [
    				"arn:*:ec2:*:*:vpc-endpoint/*"
    			],
    			"Condition": {
    				"StringEquals": {
    					"aws:RequestTag/AWSMSKManaged": "true"
    				},
    				"StringLike": {
    					"aws:RequestTag/ClusterArn": "*"
    				}
    			}
    		},
    		{
    			"Effect": "Allow",
    			"Action": [
    				"ec2:CreateTags"
    			],
    			"Resource": "arn:*:ec2:*:*:vpc-endpoint/*",
    			"Condition": {
    				"StringEquals": {
    					"ec2:CreateAction": "CreateVpcEndpoint"
    				}
    			}
    		},
    		{
    			"Effect": "Allow",
    			"Action": [
    				"ec2:DeleteVpcEndpoints"
    			],
    			"Resource": "arn:*:ec2:*:*:vpc-endpoint/*",
    			"Condition": {
    				"StringEquals": {
    					"ec2:ResourceTag/AWSMSKManaged": "true"
    				},
    				"StringLike": {
    					"ec2:ResourceTag/ClusterArn": "*"
    				}
    			}
    		},
    		{
    			"Effect": "Allow",
    			"Action": "iam:PassRole",
    			"Resource": "*",
    			"Condition": {
    				"StringEquals": {
    					"iam:PassedToService": "kafka.amazonaws.com"
    				}
    			}
    		},
    		{
    			"Effect": "Allow",
    			"Action": "iam:CreateServiceLinkedRole",
    			"Resource": "arn:aws:iam::*:role/aws-service-role/kafka.amazonaws.com/AWSServiceRoleForKafka*",
    			"Condition": {
    				"StringLike": {
    					"iam:AWSServiceName": "kafka.amazonaws.com"
    				}
    			}
    		},
    		{
    			"Effect": "Allow",
    			"Action": [
    				"iam:AttachRolePolicy",
    				"iam:PutRolePolicy"
    			],
    			"Resource": "arn:aws:iam::*:role/aws-service-role/kafka.amazonaws.com/AWSServiceRoleForKafka*"
    		},
    		{
    			"Effect": "Allow",
    			"Action": "iam:CreateServiceLinkedRole",
    			"Resource": "arn:aws:iam::*:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery*",
    			"Condition": {
    				"StringLike": {
    					"iam:AWSServiceName": "delivery.logs.amazonaws.com"
    				}
    			}
    		}

    	]
    }
```

------