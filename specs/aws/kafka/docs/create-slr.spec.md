---
id: "@specs/aws/kafka/docs/create-slr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a service-linked role"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a service-linked role

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-slr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a service-linked role for Amazon MSK
<a name="create-slr"></a>

You don't need to create a service-linked role manually. When you create an Amazon MSK cluster in the AWS Management Console, the AWS CLI, or the AWS API, Amazon MSK creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create an Amazon MSK cluster, Amazon MSK creates the service-linked role for you again. 