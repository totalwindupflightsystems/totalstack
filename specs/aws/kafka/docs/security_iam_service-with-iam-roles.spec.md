---
id: "@specs/aws/kafka/docs/security_iam_service-with-iam-roles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon MSK IAM roles"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Amazon MSK IAM roles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/security_iam_service-with-iam-roles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your Amazon Web Services account that has specific permissions.

## Using temporary credentials with Amazon MSK
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

Amazon MSK supports using temporary credentials. 

## Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow Amazon Web Services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An administrator can view but not edit the permissions for service-linked roles.

Amazon MSK supports service-linked roles. For details about creating or managing Amazon MSK service-linked roles, [Service-linked roles for Amazon MSK](using-service-linked-roles.md).