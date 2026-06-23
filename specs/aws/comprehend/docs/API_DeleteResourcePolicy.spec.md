---
id: "@specs/aws/comprehend/docs/API_DeleteResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteResourcePolicy"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DeleteResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DeleteResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes a resource-based policy that is attached to a custom model.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
{
   "PolicyRevisionId": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyRevisionId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="comprehend-DeleteResourcePolicy-request-PolicyRevisionId"></a>
The revision ID of the policy to delete.  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[0-9A-Fa-f]+`   
Required: No

 ** [ResourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="comprehend-DeleteResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the custom model version that has the policy to delete.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: Yes

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DeleteResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DeleteResourcePolicy) 