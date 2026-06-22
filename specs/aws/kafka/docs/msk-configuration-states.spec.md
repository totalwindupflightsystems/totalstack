---
id: "@specs/aws/kafka/docs/msk-configuration-states"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon MSK configuration states"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Amazon MSK configuration states

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-states
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK configuration states
<a name="msk-configuration-states"></a>

An Amazon MSK configuration can be in one of the following states. To perform an operation on a configuration, the configuration must be in the `ACTIVE` or `DELETE_FAILED` state:
+ `ACTIVE`
+ `DELETING`
+ `DELETE_FAILED`