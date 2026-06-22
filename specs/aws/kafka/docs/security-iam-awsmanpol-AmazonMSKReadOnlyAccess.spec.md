---
id: "@specs/aws/kafka/docs/security-iam-awsmanpol-AmazonMSKReadOnlyAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managed policy AmazonMSKReadOnlyAccess"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Managed policy AmazonMSKReadOnlyAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security-iam-awsmanpol-AmazonMSKReadOnlyAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policy: AmazonMSKReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonMSKReadOnlyAccess"></a>

This policy grants read-only permissions that allow users to view information in Amazon MSK. Principals with this policy attached can't make any updates or delete exiting resources, nor can they create new Amazon MSK resources. For example, principals with these permissions can view the list of clusters and configurations associated with their account, but cannot change the configuration or settings of any clusters. The permissions in this policy are grouped as follows:
+ **`Amazon MSK` permissions** – allow you to list Amazon MSK resources, describe them, and get information about them.
+ **`Amazon EC2` permissions** – are used to describe the Amazon VPC, subnets, security groups, and ENIs that are associated with a cluster.
+ **`AWS KMS` permission** – is used to describe the key that is associated with the cluster.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "kafka:Describe*",
                "kafka:List*",
                "kafka:Get*",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "kms:DescribeKey"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------