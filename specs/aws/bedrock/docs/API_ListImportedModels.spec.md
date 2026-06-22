---
id: "@specs/aws/bedrock/docs/API_ListImportedModels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListImportedModels"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListImportedModels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListImportedModels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListImportedModels
<a name="API_ListImportedModels"></a>

Returns a list of models you've imported. You can filter the results to return based on one or more criteria. For more information, see [Import a customized model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListImportedModels_RequestSyntax"></a>

```
GET /imported-models?creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListImportedModels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [creationTimeAfter](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-creationTimeAfter"></a>
Return imported models that were created after the specified time.

 ** [creationTimeBefore](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-creationTimeBefore"></a>
Return imported models that created before the specified time.

 ** [maxResults](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nameContains](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-nameContains"></a>
Return imported models only if the model name contains these characters.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+` 

 ** [nextToken](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-sortBy"></a>
The field to sort by in the returned list of imported models.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListImportedModels_RequestSyntax) **   <a name="bedrock-ListImportedModels-request-uri-sortOrder"></a>
Specifies whetehr to sort the results in ascending or descending order.  
Valid Values: `Ascending | Descending` 

## Request Body
<a name="API_ListImportedModels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListImportedModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelSummaries": [ 
      { 
         "creationTime": "string",
         "instructSupported": boolean,
         "modelArchitecture": "string",
         "modelArn": "string",
         "modelName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImportedModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelSummaries](#API_ListImportedModels_ResponseSyntax) **   <a name="bedrock-ListImportedModels-response-modelSummaries"></a>
Model summaries.  
Type: Array of [ImportedModelSummary](API_ImportedModelSummary.md) objects

 ** [nextToken](#API_ListImportedModels_ResponseSyntax) **   <a name="bedrock-ListImportedModels-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListImportedModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_ListImportedModels_Examples"></a>

### List the imported models
<a name="API_ListImportedModels_Example_1"></a>

Lists the models that you have imported. 

```
GET /imported-models/ HTTP/1.1
Content-type: application/json
```

### Example response
<a name="API_ListImportedModels_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
Content-type: application/json

{
    "modelSummaries": [
        {
            "modelArn": "arn:aws:bedrock:us-east-1:111122223333:imported-model/s4dt0wly5gud",
            "modelName": "SomeImportedModelName",
            "creationTime": "2024-08-13T19:20:14.058Z"
        }
    ]
}
```

## See Also
<a name="API_ListImportedModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListImportedModels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListImportedModels) 