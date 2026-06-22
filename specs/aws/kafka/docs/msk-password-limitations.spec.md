---
id: "@specs/aws/kafka/docs/msk-password-limitations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Limitations when using SCRAM secrets"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Limitations when using SCRAM secrets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-password-limitations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Limitations when using SCRAM secrets
<a name="msk-password-limitations"></a>

Note the following limitations when using SCRAM secrets:
+ Amazon MSK only supports SCRAM-SHA-512 authentication.
+ An Amazon MSK cluster can have up to 1000 users.
+ You must use an AWS KMS key with your Secret. You cannot use a Secret that uses the default Secrets Manager encryption key with Amazon MSK. For information about creating a KMS key, see [Creating symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk).
+ You can't use an asymmetric KMS key with Secrets Manager.
+ You can associate up to 10 secrets with a cluster at a time using the [ BatchAssociateScramSecret](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#BatchAssociateScramSecret) operation.
+ The name of secrets associated with an Amazon MSK cluster must have the prefix **AmazonMSK\_**.
+ Secrets associated with an Amazon MSK cluster must be in the same Amazon Web Services account and AWS region as the cluster.