---
id: "@specs/aws/emr/docs/API_StepDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepDetail
<a name="API_StepDetail"></a>

Combines the execution state and configuration of a step.

## Contents
<a name="API_StepDetail_Contents"></a>

 ** ExecutionStatusDetail **   <a name="EMR-Type-StepDetail-ExecutionStatusDetail"></a>
The description of the step status.  
Type: [StepExecutionStatusDetail](API_StepExecutionStatusDetail.md) object  
Required: Yes

 ** StepConfig **   <a name="EMR-Type-StepDetail-StepConfig"></a>
The step configuration.  
Type: [StepConfig](API_StepConfig.md) object  
Required: Yes

## See Also
<a name="API_StepDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepDetail) 