---
id: "@specs/aws/kafka/docs/slr-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Service-linked role permissions"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Service-linked role permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/slr-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Service-linked role permissions for Amazon MSK
<a name="slr-permissions"></a>

Amazon MSK uses the service-linked role named **AWSServiceRoleForKafka**. Amazon MSK uses this role to access your resources and perform operations such as:
+ `*NetworkInterface` – create and manage network interfaces in the customer account that make cluster brokers accessible to clients in the customer VPC.
+ `*VpcEndpoints` – manage VPC endpoints in the customer account that make cluster brokers accessible to clients in the customer VPC using AWS PrivateLink. Amazon MSK uses permissions to `DescribeVpcEndpoints`, `ModifyVpcEndpoint` and `DeleteVpcEndpoints`.
+ `secretsmanager` – manage client credentials with AWS Secrets Manager.
+ `GetCertificateAuthorityCertificate` – retrieve the certificate for your private certificate authority.
+ `*Ipv6Addresses` – assign and unassign IPv6 addresses to network interfaces in customer account to enable IPv6 connectivity for MSK clusters.
+ `ModifyNetworkInterfaceAttribute` – modify network interface attributes in customer account to configure IPv6 settings for MSK cluster connectivity.

This service-linked role is attached to the following managed policy: `KafkaServiceRolePolicy`. For updates to this policy, see [KafkaServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/KafkaServiceRolePolicy.html).

The AWSServiceRoleForKafka service-linked role trusts the following services to assume the role:
+ `kafka.amazonaws.com`

The role permissions policy allows Amazon MSK to complete the following actions on resources.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.