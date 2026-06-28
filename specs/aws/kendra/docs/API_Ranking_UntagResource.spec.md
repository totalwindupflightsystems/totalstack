---
id: "@specs/aws/kendra/docs/API_Ranking_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Ranking_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_Ranking_UntagResource"></a>

Removes a tag from a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` operation.

## Request Syntax
<a name="API_Ranking_UntagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_Ranking_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_Ranking_UntagResource_RequestSyntax) **   <a name="kendra-Ranking_UntagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the rescore execution plan to remove the tag. For example, the ARN of a rescore execution plan is constructed as follows: *arn:aws:kendra-ranking:your-region:your-account-id:rescore-execution-plan/rescore-execution-plan-id* For information, see [Resource types](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendraintelligentranking.html#amazonkendraintelligentranking-resources-for-iam-policies).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

 ** [TagKeys](#API_Ranking_UntagResource_RequestSyntax) **   <a name="kendra-Ranking_UntagResource-request-TagKeys"></a>
A list of tag keys to remove from the rescore execution plan. If a tag key does not exist on the resource, it is ignored.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Elements
<a name="API_Ranking_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_Ranking_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceUnavailableException **   
The resource you want to use is unavailable. Please check you have provided the correct resource information and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_Ranking_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-ranking-2022-10-19/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-ranking-2022-10-19/UntagResource) 