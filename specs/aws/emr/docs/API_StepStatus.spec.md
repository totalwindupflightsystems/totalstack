---
id: "@specs/aws/emr/docs/API_StepStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepStatus
<a name="API_StepStatus"></a>

The execution status details of the cluster step.

## Contents
<a name="API_StepStatus_Contents"></a>

 ** FailureDetails **   <a name="EMR-Type-StepStatus-FailureDetails"></a>
The details for the step failure including reason, message, and log file path where the root cause was identified.  
Type: [FailureDetails](API_FailureDetails.md) object  
Required: No

 ** State **   <a name="EMR-Type-StepStatus-State"></a>
The execution state of the cluster step.  
Type: String  
Valid Values: `PENDING | CANCEL_PENDING | RUNNING | COMPLETED | CANCELLED | FAILED | INTERRUPTED`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-StepStatus-StateChangeReason"></a>
The reason for the step execution status change.  
Type: [StepStateChangeReason](API_StepStateChangeReason.md) object  
Required: No

 ** Timeline **   <a name="EMR-Type-StepStatus-Timeline"></a>
The timeline of the cluster step status over time.  
Type: [StepTimeline](API_StepTimeline.md) object  
Required: No

## See Also
<a name="API_StepStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepStatus) 