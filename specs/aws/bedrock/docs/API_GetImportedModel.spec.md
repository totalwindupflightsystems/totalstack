---
id: "@specs/aws/bedrock/docs/API_GetImportedModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetImportedModel"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetImportedModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetImportedModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetImportedModel
<a name="API_GetImportedModel"></a>

Gets properties associated with a customized model you imported. 

## Request Syntax
<a name="API_GetImportedModel_RequestSyntax"></a>

```
GET /imported-models/{{modelIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImportedModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelIdentifier](#API_GetImportedModel_RequestSyntax) **   <a name="bedrock-GetImportedModel-request-uri-modelIdentifier"></a>
Name or Amazon Resource Name (ARN) of the imported model.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12})|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

## Request Body
<a name="API_GetImportedModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImportedModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "customModelUnits": { 
      "customModelUnitsPerModelCopy": number,
      "customModelUnitsVersion": "string"
   },
   "instructSupported": boolean,
   "jobArn": "string",
   "jobName": "string",
   "modelArchitecture": "string",
   "modelArn": "string",
   "modelDataSource": { ... },
   "modelKmsKeyArn": "string",
   "modelName": "string"
}
```

## Response Elements
<a name="API_GetImportedModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-creationTime"></a>
Creation time of the imported model.  
Type: Timestamp

 ** [customModelUnits](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-customModelUnits"></a>
Information about the hardware utilization for a single copy of the model.  
Type: [CustomModelUnits](API_CustomModelUnits.md) object

 ** [instructSupported](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-instructSupported"></a>
Specifies if the imported model supports converse.  
Type: Boolean

 ** [jobArn](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-jobArn"></a>
Job Amazon Resource Name (ARN) associated with the imported model.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12}` 

 ** [jobName](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-jobName"></a>
Job name associated with the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [modelArchitecture](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-modelArchitecture"></a>
The architecture of the imported model.  
Type: String

 ** [modelArn](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-modelArn"></a>
The Amazon Resource Name (ARN) associated with this imported model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12}` 

 ** [modelDataSource](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-modelDataSource"></a>
The data source for this imported model.  
Type: [ModelDataSource](API_ModelDataSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [modelKmsKeyArn](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-modelKmsKeyArn"></a>
The imported model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [modelName](#API_GetImportedModel_ResponseSyntax) **   <a name="bedrock-GetImportedModel-response-modelName"></a>
The name of the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+` 

## Errors
<a name="API_GetImportedModel_Errors"></a>

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

## Examples
<a name="API_GetImportedModel_Examples"></a>

### Get model properties
<a name="API_GetImportedModel_Example_1"></a>

Get the properties associated with a customized model that you imported.

```
GET /imported-models/{modelIdentifier} HTTP/1.1
Content-type: application/json
```

### Example response
<a name="API_GetImportedModel_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
Content-type: application/json

{
    "modelArn": "arn:aws:bedrock:us-east-1:111122223333:imported-model/s4dt0wly5gud",
    "modelName": "SomeImportedModelName",
    "jobName": "importJob-20240713T121942",
    "jobArn": "arn:aws:bedrock:us-east-1:111122223333:model-import-job/dchh9ny8e0dv",
    "modelDataSource": {
        "s3DataSource": {
            "s3Uri": "S3://amzn-s3-demo-bucket/key-name"
        }
    },
    "creationTime": "2024-08-13T19:20:14.058Z",
    "modelArchitecture": "mistral",
     "customModelUnits": {
         "customModelUnitsPerModelCopy": 8,
         "customModelUnitsVersion": "v1.0"
     }
}
```

## See Also
<a name="API_GetImportedModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetImportedModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetImportedModel) 