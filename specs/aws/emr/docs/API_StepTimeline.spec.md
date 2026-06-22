---
id: "@specs/aws/emr/docs/API_StepTimeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StepTimeline"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StepTimeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StepTimeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StepTimeline
<a name="API_StepTimeline"></a>

The timeline of the cluster step lifecycle.

## Contents
<a name="API_StepTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-StepTimeline-CreationDateTime"></a>
The date and time when the cluster step was created.  
Type: Timestamp  
Required: No

 ** EndDateTime **   <a name="EMR-Type-StepTimeline-EndDateTime"></a>
The date and time when the cluster step execution completed or failed.  
Type: Timestamp  
Required: No

 ** StartDateTime **   <a name="EMR-Type-StepTimeline-StartDateTime"></a>
The date and time when the cluster step execution started.  
Type: Timestamp  
Required: No

## See Also
<a name="API_StepTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepTimeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepTimeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepTimeline) 