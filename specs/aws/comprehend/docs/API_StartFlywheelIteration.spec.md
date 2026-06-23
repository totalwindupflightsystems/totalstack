---
id: "@specs/aws/comprehend/docs/API_StartFlywheelIteration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartFlywheelIteration"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# StartFlywheelIteration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_StartFlywheelIteration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartFlywheelIteration
<a name="API_StartFlywheelIteration"></a>

Start the flywheel iteration.This operation uses any new datasets to train a new model version. For more information about flywheels, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_StartFlywheelIteration_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FlywheelArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartFlywheelIteration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartFlywheelIteration_RequestSyntax) **   <a name="comprehend-StartFlywheelIteration-request-ClientRequestToken"></a>
A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [FlywheelArn](#API_StartFlywheelIteration_RequestSyntax) **   <a name="comprehend-StartFlywheelIteration-request-FlywheelArn"></a>
The ARN of the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

## Response Syntax
<a name="API_StartFlywheelIteration_ResponseSyntax"></a>

```
{
   "FlywheelArn": "string",
   "FlywheelIterationId": "string"
}
```

## Response Elements
<a name="API_StartFlywheelIteration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlywheelArn](#API_StartFlywheelIteration_ResponseSyntax) **   <a name="comprehend-StartFlywheelIteration-response-FlywheelArn"></a>
  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*` 

 ** [FlywheelIterationId](#API_StartFlywheelIteration_ResponseSyntax) **   <a name="comprehend-StartFlywheelIteration-response-FlywheelIterationId"></a>
  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `[0-9]{8}T[0-9]{6}Z` 

## Errors
<a name="API_StartFlywheelIteration_Errors"></a>

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

 ** ResourceLimitExceededException **   
The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_StartFlywheelIteration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/StartFlywheelIteration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/StartFlywheelIteration) 