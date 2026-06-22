---
id: "@specs/aws/kafka/docs/mkc-security-iam-awsmanpol"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS managed policies"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# AWS managed policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mkc-security-iam-awsmanpol
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policies for MSK Connect
<a name="mkc-security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonMSKConnectReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonMSKConnectReadOnlyAccess"></a>

This policy grants the user the permissions that are needed to list and describe MSK Connect resources.

You can attach the `AmazonMSKConnectReadOnlyAccess` policy to your IAM identities.

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
                "kafkaconnect:ListConnectors",
                "kafkaconnect:ListCustomPlugins",
                "kafkaconnect:ListWorkerConfigurations"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kafkaconnect:DescribeConnector"
            ],
            "Resource": [
                "arn:aws:kafkaconnect:*:*:connector/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kafkaconnect:DescribeCustomPlugin"
            ],
            "Resource": [
                "arn:aws:kafkaconnect:*:*:custom-plugin/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kafkaconnect:DescribeWorkerConfiguration"
            ],
            "Resource": [
                "arn:aws:kafkaconnect:*:*:worker-configuration/*"
            ]
        }
    ]
}
```

------

## AWS managed policy: KafkaConnectServiceRolePolicy
<a name="security-iam-awsmanpol-KafkaConnectServiceRolePolicy"></a>

This policy grants the MSK Connect service the permissions that are needed to create and manage network interfaces that have the tag `AmazonMSKConnectManaged:true`. These network interfaces give MSK Connect network access to resources in your Amazon VPC, such as an Apache Kafka cluster or a source or a sink.

You can't attach KafkaConnectServiceRolePolicy to your IAM entities. This policy is attached to a service-linked role that allows MSK Connect to perform actions on your behalf.

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
				"ec2:CreateNetworkInterface"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"aws:RequestTag/AmazonMSKConnectManaged": "true"
				},
				"ForAllValues:StringEquals": {
					"aws:TagKeys": "AmazonMSKConnectManaged"
				}
			}
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateNetworkInterface"
			],
			"Resource": [
				"arn:aws:ec2:*:*:subnet/*",
				"arn:aws:ec2:*:*:security-group/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:CreateTags"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"ec2:CreateAction": "CreateNetworkInterface"
				}
			}
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:DescribeNetworkInterfaces",
				"ec2:CreateNetworkInterfacePermission",
				"ec2:AttachNetworkInterface",
				"ec2:DetachNetworkInterface",
				"ec2:DeleteNetworkInterface"
			],
			"Resource": "arn:aws:ec2:*:*:network-interface/*",
			"Condition": {
				"StringEquals": {
					"ec2:ResourceTag/AmazonMSKConnectManaged": "true"
				}
			}
		}
	]
}
```

------

## MSK Connect updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for MSK Connect since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| MSK Connect updated read-only policy | MSK Connect updated the AmazonMSKConnectReadOnlyAccess policy to remove the restrictions on listing operations. | October 13, 2021 | 
| MSK Connect started tracking changes | MSK Connect started tracking changes for its AWS managed policies. | September 14, 2021 | 