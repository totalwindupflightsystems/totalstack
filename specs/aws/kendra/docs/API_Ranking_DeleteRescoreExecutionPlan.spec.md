---
id: "@specs/aws/kendra/docs/API_Ranking_DeleteRescoreExecutionPlan"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteRescoreExecutionPlan"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DeleteRescoreExecutionPlan

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Ranking_DeleteRescoreExecutionPlan
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteRescoreExecutionPlan
<a name="API_Ranking_DeleteRescoreExecutionPlan"></a>

Deletes a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API.

## Request Syntax
<a name="API_Ranking_DeleteRescoreExecutionPlan_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_Ranking_DeleteRescoreExecutionPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_Ranking_DeleteRescoreExecutionPlan_RequestSyntax) **   <a name="kendra-Ranking_DeleteRescoreExecutionPlan-request-Id"></a>
The identifier of the rescore execution plan that you want to delete.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

## Response Elements
<a name="API_Ranking_DeleteRescoreExecutionPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_Ranking_DeleteRescoreExecutionPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** ConflictException **   
A conflict occurred with the request. Please fix any inconsistencies with your resources and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn't exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_Ranking_DeleteRescoreExecutionPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-ranking-2022-10-19/DeleteRescoreExecutionPlan) 