---
id: "@specs/aws/kafka/docs/security_iam_service-with-iam-tags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Authorization based on Amazon MSK tags"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Authorization based on Amazon MSK tags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security_iam_service-with-iam-tags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Authorization based on Amazon MSK tags
<a name="security_iam_service-with-iam-tags"></a>

You can attach tags to Amazon MSK clusters. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `kafka:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For information about tagging Amazon MSK resources, see [Tag an Amazon MSK cluster](msk-tagging.md).

You can only control cluster access with the help of tags. To tag topics and consumer groups, you need to add a separate statement in your policies without tags.

To view example of an identity-based policy for limiting access to a cluster based on the tags on that cluster, see [Accessing Amazon MSK clusters based on tags](security_iam_id-based-policy-examples-view-widget-tags.md).

You can use conditions in your identity-based policy to control access to Amazon MSK resources based on tags. The following example shows a policy that allows a user to describe the cluster, get its bootstrap brokers, list its broker nodes, update it, and delete it. However, this policy grants permission only if the cluster tag `Owner` has the value of that user's `username`. The second statement in the following policy allows access to the topics on the cluster. The first statement in this policy doesn't authorize any topic access.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AccessClusterIfOwner",
      "Effect": "Allow",
      "Action": [
        "kafka:Describe*",
        "kafka:Get*",
        "kafka:List*",
        "kafka:Update*",
        "kafka:Delete*"
      ],
      "Resource": "arn:aws:kafka:us-east-1:123456789012:cluster/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Owner": "${aws:username}"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "kafka-cluster:*Topic*",
        "kafka-cluster:WriteData",
        "kafka-cluster:ReadData"
      ],
      "Resource": [
        "arn:aws:kafka:us-east-1:123456789012:topic/*"
      ]
    }
  ]
}
```

------