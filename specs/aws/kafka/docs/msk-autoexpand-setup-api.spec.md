---
id: "@specs/aws/kafka/docs/msk-autoexpand-setup-api"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up auto scaling using API"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up auto scaling using API

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-autoexpand-setup-api
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up automatic-scaling for Amazon MSK using the API
<a name="msk-autoexpand-setup-api"></a>

This process describes how to use the Amazon MSK API to implement automatic scaling for storage.

1. Use the [ RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) API to register a storage utilization target.

1. Use the [ PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html) API to create an auto-expansion policy.