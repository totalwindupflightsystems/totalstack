---
id: "@specs/aws/kafka/docs/edit-slr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Edit a service-linked role"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Edit a service-linked role

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/edit-slr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Edit a service-linked role for Amazon MSK
<a name="edit-slr"></a>

Amazon MSK does not allow you to edit the AWSServiceRoleForKafka service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.