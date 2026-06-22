---
id: "@specs/aws/kafka/docs/security-iam-awsmanpol-KafkaServiceRolePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managed policy KafkaServiceRolePolicy"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Managed policy KafkaServiceRolePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security-iam-awsmanpol-KafkaServiceRolePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policy: KafkaServiceRolePolicy
<a name="security-iam-awsmanpol-KafkaServiceRolePolicy"></a>

You can't attach KafkaServiceRolePolicy to your IAM entities. This policy is attached to a service-linked role that allows Amazon MSK to perform actions such as managing VPC endpoints (connectors) on MSK clusters, managing network interfaces, and managing cluster credentials with AWS Secrets Manager. For more information, see [Service-linked roles for Amazon MSK](using-service-linked-roles.md).

The following table describes updates to the KafkaServiceRolePolicy managed policy since Amazon MSK started tracking changes.


| Change | Description | Date | 
| --- | --- | --- | 
|  [IPv6 connectivity support added to KafkaServiceRolePolicy](#security-iam-awsmanpol-KafkaServiceRolePolicy) – Update to an existing policy  | Amazon MSK added permissions to KafkaServiceRolePolicy to enable IPv6 connectivity for MSK clusters. These permissions allow Amazon MSK to assign and unassign IPv6 addresses to network interfaces and modify network interface attributes in customer account. | November 17, 2025 | 
|  [KafkaServiceRolePolicy](#security-iam-awsmanpol-KafkaServiceRolePolicy) – Update to an existing policy  | Amazon MSK added permissions to support multi-VPC private connectivity. | March 8, 2023 | 
| Amazon MSK started tracking changes | Amazon MSK started tracking changes for KafkaServiceRolePolicy managed policy. | March 8, 2023 | 