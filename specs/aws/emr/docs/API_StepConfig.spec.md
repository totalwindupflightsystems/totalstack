---
id: "@specs/aws/emr/docs/API_StepConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepConfig
<a name="API_StepConfig"></a>

Specification for a cluster (job flow) step.

## Contents
<a name="API_StepConfig_Contents"></a>

 ** HadoopJarStep **   <a name="EMR-Type-StepConfig-HadoopJarStep"></a>
The JAR file used for the step.  
Type: [HadoopJarStepConfig](API_HadoopJarStepConfig.md) object  
Required: Yes

 ** Name **   <a name="EMR-Type-StepConfig-Name"></a>
The name of the step.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** ActionOnFailure **   <a name="EMR-Type-StepConfig-ActionOnFailure"></a>
The action to take when the step fails. Use one of the following values:  
+  `TERMINATE_CLUSTER` - Shuts down the cluster.
+  `CANCEL_AND_WAIT` - Cancels any pending steps and returns the cluster to the `WAITING` state.
+  `CONTINUE` - Continues to the next step in the queue.
+  `TERMINATE_JOB_FLOW` - Shuts down the cluster. `TERMINATE_JOB_FLOW` is provided for backward compatibility. We recommend using `TERMINATE_CLUSTER` instead.
If a cluster's `StepConcurrencyLevel` is greater than `1`, do not use `AddJobFlowSteps` to submit a step with this parameter set to `CANCEL_AND_WAIT` or `TERMINATE_CLUSTER`. The step is not submitted and the action fails with a message that the `ActionOnFailure` setting is not valid.  
If you change a cluster's `StepConcurrencyLevel` to be greater than 1 while a step is running, the `ActionOnFailure` parameter may not behave as you expect. In this case, for a step that fails with this parameter set to `CANCEL_AND_WAIT`, pending steps and the running step are not canceled; for a step that fails with this parameter set to `TERMINATE_CLUSTER`, the cluster does not terminate.  
Type: String  
Valid Values: `TERMINATE_JOB_FLOW | TERMINATE_CLUSTER | CANCEL_AND_WAIT | CONTINUE`   
Required: No

 ** StepMonitoringConfiguration **   <a name="EMR-Type-StepConfig-StepMonitoringConfiguration"></a>
Object that holds configuration properties for logging.  
Type: [StepMonitoringConfiguration](API_StepMonitoringConfiguration.md) object  
Required: No

## See Also
<a name="API_StepConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepConfig) 