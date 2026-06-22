---
id: "@specs/aws/codepipeline/docs/API_ExecutionDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExecutionDetails"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ExecutionDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ExecutionDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExecutionDetails
<a name="API_ExecutionDetails"></a>

The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline.

## Contents
<a name="API_ExecutionDetails_Contents"></a>

 ** externalExecutionId **   <a name="CodePipeline-Type-ExecutionDetails-externalExecutionId"></a>
The system-generated unique ID of this action used to identify this job worker in any external systems, such as CodeDeploy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

 ** percentComplete **   <a name="CodePipeline-Type-ExecutionDetails-percentComplete"></a>
The percentage of work completed on the action, represented on a scale of 0 to 100 percent.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** summary **   <a name="CodePipeline-Type-ExecutionDetails-summary"></a>
The summary of the current status of the actions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ExecutionDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ExecutionDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ExecutionDetails) 