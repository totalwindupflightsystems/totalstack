---
id: "@specs/aws/emr/docs/API_Step"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Step

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Step
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step
<a name="API_Step"></a>

This represents a step in a cluster.

## Contents
<a name="API_Step_Contents"></a>

 ** ActionOnFailure **   <a name="EMR-Type-Step-ActionOnFailure"></a>
The action to take when the cluster step fails. Possible values are `TERMINATE_CLUSTER`, `CANCEL_AND_WAIT`, and `CONTINUE`. `TERMINATE_JOB_FLOW` is provided for backward compatibility. We recommend using `TERMINATE_CLUSTER` instead.  
If a cluster's `StepConcurrencyLevel` is greater than `1`, do not use `AddJobFlowSteps` to submit a step with this parameter set to `CANCEL_AND_WAIT` or `TERMINATE_CLUSTER`. The step is not submitted and the action fails with a message that the `ActionOnFailure` setting is not valid.  
If you change a cluster's `StepConcurrencyLevel` to be greater than 1 while a step is running, the `ActionOnFailure` parameter may not behave as you expect. In this case, for a step that fails with this parameter set to `CANCEL_AND_WAIT`, pending steps and the running step are not canceled; for a step that fails with this parameter set to `TERMINATE_CLUSTER`, the cluster does not terminate.  
Type: String  
Valid Values: `TERMINATE_JOB_FLOW | TERMINATE_CLUSTER | CANCEL_AND_WAIT | CONTINUE`   
Required: No

 ** Config **   <a name="EMR-Type-Step-Config"></a>
The Hadoop job configuration of the cluster step.  
Type: [HadoopStepConfig](API_HadoopStepConfig.md) object  
Required: No

 ** EncryptionKeyArn **   <a name="EMR-Type-Step-EncryptionKeyArn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.  
Type: String  
Required: No

 ** ExecutionRoleArn **   <a name="EMR-Type-Step-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: `arn:partition:service:region:account:resource`.   
For example, `arn:aws:IAM::1234567890:role/ReadOnly` is a correctly formatted runtime role ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** Id **   <a name="EMR-Type-Step-Id"></a>
The identifier of the cluster step.  
Type: String  
Required: No

 ** LogUri **   <a name="EMR-Type-Step-LogUri"></a>
The Amazon S3 destination URI for log publishing.  
Type: String  
Required: No

 ** Name **   <a name="EMR-Type-Step-Name"></a>
The name of the cluster step.  
Type: String  
Required: No

 ** Status **   <a name="EMR-Type-Step-Status"></a>
The current execution status details of the cluster step.  
Type: [StepStatus](API_StepStatus.md) object  
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Step) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Step) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Step) 