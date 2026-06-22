---
id: "@specs/aws/bedrock/docs/API_DeleteImportedModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteImportedModel"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteImportedModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_DeleteImportedModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteImportedModel
<a name="API_DeleteImportedModel"></a>

Deletes a custom model that you imported earlier. For more information, see [Import a customized model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html). 

## Request Syntax
<a name="API_DeleteImportedModel_RequestSyntax"></a>

```
DELETE /imported-models/{{modelIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteImportedModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelIdentifier](#API_DeleteImportedModel_RequestSyntax) **   <a name="bedrock-DeleteImportedModel-request-uri-modelIdentifier"></a>
Name of the imported model to delete.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12})|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

## Request Body
<a name="API_DeleteImportedModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteImportedModel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteImportedModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteImportedModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

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
<a name="API_DeleteImportedModel_Examples"></a>

### Delete an imported model
<a name="API_DeleteImportedModel_Example_1"></a>

Deletes a model that you have previously imported.

```
DELETE /imported-models/{modelIdentifier} HTTP/1.1
Content-type: application/json
```

### Example response
<a name="API_DeleteImportedModel_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
```

## See Also
<a name="API_DeleteImportedModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteImportedModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteImportedModel) 