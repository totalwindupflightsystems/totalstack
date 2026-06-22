---
id: "@specs/aws/kafka/docs/security_iam_id-based-policy-examples-access-one-cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Accessing one Amazon MSK cluster"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Accessing one Amazon MSK cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security_iam_id-based-policy-examples-access-one-cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Accessing one Amazon MSK cluster
<a name="security_iam_id-based-policy-examples-access-one-cluster"></a>

In this example, you want to grant an IAM user in your Amazon Web Services account access to one of your clusters, `purchaseQueriesCluster`. This policy allows the user to describe the cluster, get its bootstrap brokers, list its broker nodes, and update it.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"UpdateCluster",
         "Effect":"Allow",
         "Action":[
            "kafka:Describe*",
            "kafka:Get*",
            "kafka:List*",
            "kafka:Update*"
         ],
         "Resource":"arn:aws:kafka:us-east-1:012345678012:cluster/purchaseQueriesCluster/abcdefab-1234-abcd-5678-cdef0123ab01-2"
      }
   ]
}
```

------