---
id: "@specs/aws/emr/docs/API_StepExecutionStatusDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepExecutionStatusDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepExecutionStatusDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepExecutionStatusDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepExecutionStatusDetail
<a name="API_StepExecutionStatusDetail"></a>

The execution state of a step.

## Contents
<a name="API_StepExecutionStatusDetail_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-StepExecutionStatusDetail-CreationDateTime"></a>
The creation date and time of the step.  
Type: Timestamp  
Required: Yes

 ** State **   <a name="EMR-Type-StepExecutionStatusDetail-State"></a>
The state of the step.  
Type: String  
Valid Values: `PENDING | RUNNING | CONTINUE | COMPLETED | CANCELLED | FAILED | INTERRUPTED`   
Required: Yes

 ** EndDateTime **   <a name="EMR-Type-StepExecutionStatusDetail-EndDateTime"></a>
The completion date and time of the step.  
Type: Timestamp  
Required: No

 ** LastStateChangeReason **   <a name="EMR-Type-StepExecutionStatusDetail-LastStateChangeReason"></a>
A description of the step's current state.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StartDateTime **   <a name="EMR-Type-StepExecutionStatusDetail-StartDateTime"></a>
The start date and time of the step.  
Type: Timestamp  
Required: No

## See Also
<a name="API_StepExecutionStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepExecutionStatusDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepExecutionStatusDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepExecutionStatusDetail) 