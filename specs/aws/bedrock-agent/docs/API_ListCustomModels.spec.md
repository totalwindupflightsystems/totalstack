---
id: "@specs/aws/bedrock-agent/docs/API_ListCustomModels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomModels"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListCustomModels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListCustomModels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomModels
<a name="API_ListCustomModels"></a>

Returns a list of the custom models that you have created with the `CreateModelCustomizationJob` operation.

For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListCustomModels_RequestSyntax"></a>

```
GET /custom-models?baseModelArnEquals={{baseModelArnEquals}}&creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&foundationModelArnEquals={{foundationModelArnEquals}}&isOwned={{isOwned}}&maxResults={{maxResults}}&modelStatus={{modelStatus}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomModels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [baseModelArnEquals](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-baseModelArnEquals"></a>
Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [creationTimeAfter](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-creationTimeAfter"></a>
Return custom models created after the specified time. 

 ** [creationTimeBefore](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-creationTimeBefore"></a>
Return custom models created before the specified time. 

 ** [foundationModelArnEquals](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-foundationModelArnEquals"></a>
Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}` 

 ** [isOwned](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-isOwned"></a>
Return custom models depending on if the current account owns them (`true`) or if they were shared with the current account (`false`).

 ** [maxResults](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [modelStatus](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-modelStatus"></a>
The status of them model to filter results by. Possible values include:  
+  `Creating` - Include only models that are currently being created and validated.
+  `Active` - Include only models that have been successfully created and are ready for use.
+  `Failed` - Include only models where the creation process failed.
If you don't specify a status, the API returns models in all states.  
Valid Values: `Active | Creating | Failed` 

 ** [nameContains](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-nameContains"></a>
Return custom models only if the job name contains these characters.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [nextToken](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-sortBy"></a>
The field to sort by in the returned list of models.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListCustomModels_RequestSyntax) **   <a name="bedrock-ListCustomModels-request-uri-sortOrder"></a>
The sort order of the results.  
Valid Values: `Ascending | Descending` 

## Request Body
<a name="API_ListCustomModels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelSummaries": [ 
      { 
         "baseModelArn": "string",
         "baseModelName": "string",
         "creationTime": "string",
         "customizationType": "string",
         "modelArn": "string",
         "modelName": "string",
         "modelStatus": "string",
         "ownerAccountId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelSummaries](#API_ListCustomModels_ResponseSyntax) **   <a name="bedrock-ListCustomModels-response-modelSummaries"></a>
Model summaries.  
Type: Array of [CustomModelSummary](API_CustomModelSummary.md) objects

 ** [nextToken](#API_ListCustomModels_ResponseSyntax) **   <a name="bedrock-ListCustomModels-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListCustomModels_Errors"></a>

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

## See Also
<a name="API_ListCustomModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListCustomModels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListCustomModels) 