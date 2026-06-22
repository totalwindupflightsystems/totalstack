---
id: "@specs/aws/codepipeline/docs/API_OverrideStageCondition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OverrideStageCondition"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# OverrideStageCondition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_OverrideStageCondition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OverrideStageCondition
<a name="API_OverrideStageCondition"></a>

Used to override a stage condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).

## Request Syntax
<a name="API_OverrideStageCondition_RequestSyntax"></a>

```
{
   "conditionType": "{{string}}",
   "pipelineExecutionId": "{{string}}",
   "pipelineName": "{{string}}",
   "stageName": "{{string}}"
}
```

## Request Parameters
<a name="API_OverrideStageCondition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [conditionType](#API_OverrideStageCondition_RequestSyntax) **   <a name="CodePipeline-OverrideStageCondition-request-conditionType"></a>
The type of condition to override for the stage, such as entry conditions, failure conditions, or success conditions.  
Type: String  
Valid Values: `BEFORE_ENTRY | ON_SUCCESS`   
Required: Yes

 ** [pipelineExecutionId](#API_OverrideStageCondition_RequestSyntax) **   <a name="CodePipeline-OverrideStageCondition-request-pipelineExecutionId"></a>
The ID of the pipeline execution for the override.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [pipelineName](#API_OverrideStageCondition_RequestSyntax) **   <a name="CodePipeline-OverrideStageCondition-request-pipelineName"></a>
The name of the pipeline with the stage that will override the condition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [stageName](#API_OverrideStageCondition_RequestSyntax) **   <a name="CodePipeline-OverrideStageCondition-request-stageName"></a>
The name of the stage for the override.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Elements
<a name="API_OverrideStageCondition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_OverrideStageCondition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentPipelineExecutionsLimitExceededException **   
The pipeline has reached the limit for concurrent pipeline executions.  
HTTP Status Code: 400

 ** ConditionNotOverridableException **   
Unable to override because the condition does not allow overrides.  
HTTP Status Code: 400

 ** ConflictException **   
Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.  
HTTP Status Code: 400

 ** NotLatestPipelineExecutionException **   
The stage has failed in a later run of the pipeline and the `pipelineExecutionId` associated with the request is out of date.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** StageNotFoundException **   
The stage was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_OverrideStageCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/OverrideStageCondition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/OverrideStageCondition) 