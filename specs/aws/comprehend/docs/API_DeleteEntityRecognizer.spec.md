---
id: "@specs/aws/comprehend/docs/API_DeleteEntityRecognizer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEntityRecognizer"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DeleteEntityRecognizer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DeleteEntityRecognizer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEntityRecognizer
<a name="API_DeleteEntityRecognizer"></a>

Deletes an entity recognizer.

Only those recognizers that are in terminated states (IN\_ERROR, TRAINED) will be deleted. If an active inference job is using the model, a `ResourceInUseException` will be returned.

This is an asynchronous action that puts the recognizer into a DELETING state, and it is then removed by a background job. Once removed, the recognizer disappears from your account and is no longer available for use. 

## Request Syntax
<a name="API_DeleteEntityRecognizer_RequestSyntax"></a>

```
{
   "EntityRecognizerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEntityRecognizer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EntityRecognizerArn](#API_DeleteEntityRecognizer_RequestSyntax) **   <a name="comprehend-DeleteEntityRecognizer-request-EntityRecognizerArn"></a>
The Amazon Resource Name (ARN) that identifies the entity recognizer.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: Yes

## Response Elements
<a name="API_DeleteEntityRecognizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEntityRecognizer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource name is already in use. Use a different name and try your request again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** ResourceUnavailableException **   
The specified resource is not available. Check the resource and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteEntityRecognizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DeleteEntityRecognizer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DeleteEntityRecognizer) 