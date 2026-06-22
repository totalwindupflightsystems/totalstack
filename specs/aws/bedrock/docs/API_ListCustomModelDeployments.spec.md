---
id: "@specs/aws/bedrock/docs/API_ListCustomModelDeployments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomModelDeployments"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListCustomModelDeployments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListCustomModelDeployments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomModelDeployments
<a name="API_ListCustomModelDeployments"></a>

Lists custom model deployments in your account. You can filter the results by creation time, name, status, and associated model. Use this operation to manage and monitor your custom model deployments.

We recommend using pagination to ensure that the operation returns quickly and successfully.

The following actions are related to the `ListCustomModelDeployments` operation:
+  [CreateCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html) 
+  [GetCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html) 
+  [DeleteCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html) 

## Request Syntax
<a name="API_ListCustomModelDeployments_RequestSyntax"></a>

```
GET /model-customization/custom-model-deployments?createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&maxResults={{maxResults}}&modelArnEquals={{modelArnEquals}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomModelDeployments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [createdAfter](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-createdAfter"></a>
Filters deployments created after the specified date and time.

 ** [createdBefore](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-createdBefore"></a>
Filters deployments created before the specified date and time.

 ** [maxResults](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-maxResults"></a>
The maximum number of results to return in a single call.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [modelArnEquals](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-modelArnEquals"></a>
Filters deployments by the Amazon Resource Name (ARN) of the associated custom model.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}` 

 ** [nameContains](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-nameContains"></a>
Filters deployments whose names contain the specified string.   
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [nextToken](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-nextToken"></a>
The token for the next set of results. Use this token to retrieve additional results when the response is truncated.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-sortBy"></a>
The field to sort the results by. The only supported value is `CreationTime`.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-sortOrder"></a>
The sort order for the results. Valid values are `Ascending` and `Descending`. Default is `Descending`.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListCustomModelDeployments_RequestSyntax) **   <a name="bedrock-ListCustomModelDeployments-request-uri-statusEquals"></a>
Filters deployments by status. Valid values are `CREATING`, `ACTIVE`, and `FAILED`.  
Valid Values: `Creating | Active | Failed` 

## Request Body
<a name="API_ListCustomModelDeployments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomModelDeployments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelDeploymentSummaries": [ 
      { 
         "createdAt": "string",
         "customModelDeploymentArn": "string",
         "customModelDeploymentName": "string",
         "failureMessage": "string",
         "lastUpdatedAt": "string",
         "modelArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomModelDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelDeploymentSummaries](#API_ListCustomModelDeployments_ResponseSyntax) **   <a name="bedrock-ListCustomModelDeployments-response-modelDeploymentSummaries"></a>
A list of custom model deployment summaries.  
Type: Array of [CustomModelDeploymentSummary](API_CustomModelDeploymentSummary.md) objects

 ** [nextToken](#API_ListCustomModelDeployments_ResponseSyntax) **   <a name="bedrock-ListCustomModelDeployments-response-nextToken"></a>
The token for the next set of results. This value is null when there are no more results to return.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListCustomModelDeployments_Errors"></a>

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
<a name="API_ListCustomModelDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListCustomModelDeployments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListCustomModelDeployments) 