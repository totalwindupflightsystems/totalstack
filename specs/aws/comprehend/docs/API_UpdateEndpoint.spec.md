---
id: "@specs/aws/comprehend/docs/API_UpdateEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateEndpoint"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# UpdateEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_UpdateEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateEndpoint
<a name="API_UpdateEndpoint"></a>

Updates information about the specified endpoint. For information about endpoints, see [Managing endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html).

## Request Syntax
<a name="API_UpdateEndpoint_RequestSyntax"></a>

```
{
   "DesiredDataAccessRoleArn": "{{string}}",
   "DesiredInferenceUnits": {{number}},
   "DesiredModelArn": "{{string}}",
   "EndpointArn": "{{string}}",
   "FlywheelArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DesiredDataAccessRoleArn](#API_UpdateEndpoint_RequestSyntax) **   <a name="comprehend-UpdateEndpoint-request-DesiredDataAccessRoleArn"></a>
Data access role ARN to use in case the new model is encrypted with a customer CMK.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** [DesiredInferenceUnits](#API_UpdateEndpoint_RequestSyntax) **   <a name="comprehend-UpdateEndpoint-request-DesiredInferenceUnits"></a>
 The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [DesiredModelArn](#API_UpdateEndpoint_RequestSyntax) **   <a name="comprehend-UpdateEndpoint-request-DesiredModelArn"></a>
The ARN of the new model to use when updating an existing endpoint.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** [EndpointArn](#API_UpdateEndpoint_RequestSyntax) **   <a name="comprehend-UpdateEndpoint-request-EndpointArn"></a>
The Amazon Resource Number (ARN) of the endpoint being updated.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier-endpoint|entity-recognizer-endpoint)/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

 ** [FlywheelArn](#API_UpdateEndpoint_RequestSyntax) **   <a name="comprehend-UpdateEndpoint-request-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

## Response Syntax
<a name="API_UpdateEndpoint_ResponseSyntax"></a>

```
{
   "DesiredModelArn": "string"
}
```

## Response Elements
<a name="API_UpdateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DesiredModelArn](#API_UpdateEndpoint_ResponseSyntax) **   <a name="comprehend-UpdateEndpoint-response-DesiredModelArn"></a>
The Amazon Resource Number (ARN) of the new model.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?` 

## Errors
<a name="API_UpdateEndpoint_Errors"></a>

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

 ** ResourceUnavailableException **   
The specified resource is not available. Check the resource and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/UpdateEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/UpdateEndpoint) 