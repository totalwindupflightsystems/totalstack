---
id: "@specs/aws/transcribe/docs/API_DeleteCallAnalyticsCategory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCallAnalyticsCategory"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# DeleteCallAnalyticsCategory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_DeleteCallAnalyticsCategory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCallAnalyticsCategory
<a name="API_DeleteCallAnalyticsCategory"></a>

Deletes a Call Analytics category. To use this operation, specify the name of the category you want to delete using `CategoryName`. Category names are case sensitive.

## Request Syntax
<a name="API_DeleteCallAnalyticsCategory_RequestSyntax"></a>

```
{
   "CategoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCallAnalyticsCategory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CategoryName](#API_DeleteCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-DeleteCallAnalyticsCategory-request-CategoryName"></a>
The name of the Call Analytics category you want to delete. Category names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Elements
<a name="API_DeleteCallAnalyticsCategory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCallAnalyticsCategory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCallAnalyticsCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/DeleteCallAnalyticsCategory) 