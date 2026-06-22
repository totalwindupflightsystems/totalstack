---
id: "@specs/aws/bedrock/docs/API_GetProvisionedModelThroughput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetProvisionedModelThroughput"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetProvisionedModelThroughput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetProvisionedModelThroughput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetProvisionedModelThroughput
<a name="API_GetProvisionedModelThroughput"></a>

Returns details for a Provisioned Throughput. For more information, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_GetProvisionedModelThroughput_RequestSyntax"></a>

```
GET /provisioned-model-throughput/{{provisionedModelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProvisionedModelThroughput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [provisionedModelId](#API_GetProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-request-uri-provisionedModelId"></a>
The Amazon Resource Name (ARN) or ID of the Provisioned Throughput.  
Pattern: `((([0-9a-zA-Z][_-]?)+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))`   
Required: Yes

## Request Body
<a name="API_GetProvisionedModelThroughput_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProvisionedModelThroughput_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commitmentDuration": "string",
   "commitmentExpirationTime": "string",
   "creationTime": "string",
   "desiredModelArn": "string",
   "desiredModelUnits": number,
   "failureMessage": "string",
   "foundationModelArn": "string",
   "lastModifiedTime": "string",
   "modelArn": "string",
   "modelUnits": number,
   "provisionedModelArn": "string",
   "provisionedModelName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetProvisionedModelThroughput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commitmentDuration](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-commitmentDuration"></a>
Commitment duration of the Provisioned Throughput.  
Type: String  
Valid Values: `OneMonth | SixMonths` 

 ** [commitmentExpirationTime](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-commitmentExpirationTime"></a>
The timestamp for when the commitment term for the Provisioned Throughput expires.  
Type: Timestamp

 ** [creationTime](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-creationTime"></a>
The timestamp of the creation time for this Provisioned Throughput.   
Type: Timestamp

 ** [desiredModelArn](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-desiredModelArn"></a>
The Amazon Resource Name (ARN) of the model requested to be associated to this Provisioned Throughput. This value differs from the `modelArn` if updating hasn't completed.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [desiredModelUnits](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-desiredModelUnits"></a>
The number of model units that was requested for this Provisioned Throughput.  
Type: Integer  
Valid Range: Minimum value of 1.

 ** [failureMessage](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-failureMessage"></a>
A failure message for any issues that occurred during creation, updating, or deletion of the Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [foundationModelArn](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-foundationModelArn"></a>
The Amazon Resource Name (ARN) of the base model for which the Provisioned Throughput was created, or of the base model that the custom model for which the Provisioned Throughput was created was customized.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}` 

 ** [lastModifiedTime](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-lastModifiedTime"></a>
The timestamp of the last time that this Provisioned Throughput was modified.   
Type: Timestamp

 ** [modelArn](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-modelArn"></a>
The Amazon Resource Name (ARN) of the model associated with this Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [modelUnits](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-modelUnits"></a>
The number of model units allocated to this Provisioned Throughput.  
Type: Integer  
Valid Range: Minimum value of 1.

 ** [provisionedModelArn](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-provisionedModelArn"></a>
The Amazon Resource Name (ARN) of the Provisioned Throughput.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}` 

 ** [provisionedModelName](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-provisionedModelName"></a>
The name of the Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+` 

 ** [status](#API_GetProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-GetProvisionedModelThroughput-response-status"></a>
The status of the Provisioned Throughput.   
Type: String  
Valid Values: `Creating | InService | Updating | Failed` 

## Errors
<a name="API_GetProvisionedModelThroughput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_GetProvisionedModelThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetProvisionedModelThroughput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetProvisionedModelThroughput) 