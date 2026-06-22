---
id: "@specs/aws/kafka/docs/msk-autoexpand-setup-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up auto scaling using CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up auto scaling using CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-autoexpand-setup-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up automatic scaling using the CLI
<a name="msk-autoexpand-setup-cli"></a>

This process describes how to use the Amazon MSK CLI to implement automatic scaling for storage.

1. Use the [ RegisterScalableTarget](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/#available-commands) command to register a storage utilization target.

1. Use the [ PutScalingPolicy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/#available-commands) command to create an auto-expansion policy.