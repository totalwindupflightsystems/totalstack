---
id: "@specs/aws/emr/docs/API_StepSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepSummary
<a name="API_StepSummary"></a>

The summary of the cluster step.

## Contents
<a name="API_StepSummary_Contents"></a>

 ** ActionOnFailure **   <a name="EMR-Type-StepSummary-ActionOnFailure"></a>
The action to take when the cluster step fails. Possible values are TERMINATE\_CLUSTER, CANCEL\_AND\_WAIT, and CONTINUE. TERMINATE\_JOB\_FLOW is available for backward compatibility.  
Type: String  
Valid Values: `TERMINATE_JOB_FLOW | TERMINATE_CLUSTER | CANCEL_AND_WAIT | CONTINUE`   
Required: No

 ** Config **   <a name="EMR-Type-StepSummary-Config"></a>
The Hadoop job configuration of the cluster step.  
Type: [HadoopStepConfig](API_HadoopStepConfig.md) object  
Required: No

 ** EncryptionKeyArn **   <a name="EMR-Type-StepSummary-EncryptionKeyArn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.  
Type: String  
Required: No

 ** Id **   <a name="EMR-Type-StepSummary-Id"></a>
The identifier of the cluster step.  
Type: String  
Required: No

 ** LogUri **   <a name="EMR-Type-StepSummary-LogUri"></a>
The Amazon S3 destination URI for log publishing.  
Type: String  
Required: No

 ** Name **   <a name="EMR-Type-StepSummary-Name"></a>
The name of the cluster step.  
Type: String  
Required: No

 ** Status **   <a name="EMR-Type-StepSummary-Status"></a>
The current execution status details of the cluster step.  
Type: [StepStatus](API_StepStatus.md) object  
Required: No

## See Also
<a name="API_StepSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepSummary) 