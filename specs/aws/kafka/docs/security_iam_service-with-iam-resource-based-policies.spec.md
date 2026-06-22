---
id: "@specs/aws/kafka/docs/security_iam_service-with-iam-resource-based-policies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon MSK resource-based policies"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Amazon MSK resource-based policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security_iam_service-with-iam-resource-based-policies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Amazon MSK supports a cluster policy (also known as a resource-based policy) for use with Amazon MSK clusters. You can use a cluster policy to define which IAM principals have cross-account permissions to set up private connectivity to your Amazon MSK cluster. When used with IAM client authentication, you can also use the cluster policy to granularly define Kafka data plane permissions for the connecting clients.

The maximum size supported for a cluster policy is 20 KB.

To view an example of how to configure a cluster policy, refer to [Step 2: Attach a cluster policy to the MSK cluster](mvpc-cluster-owner-action-policy.md). 