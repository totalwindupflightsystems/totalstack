---
id: "@specs/aws/bedrock/docs/API_ListProvisionedModelThroughputs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListProvisionedModelThroughputs"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListProvisionedModelThroughputs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListProvisionedModelThroughputs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListProvisionedModelThroughputs
<a name="API_ListProvisionedModelThroughputs"></a>

Lists the Provisioned Throughputs in the account. For more information, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListProvisionedModelThroughputs_RequestSyntax"></a>

```
GET /provisioned-model-throughputs?creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&modelArnEquals={{modelArnEquals}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProvisionedModelThroughputs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [creationTimeAfter](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-creationTimeAfter"></a>
A filter that returns Provisioned Throughputs created after the specified time. 

 ** [creationTimeBefore](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-creationTimeBefore"></a>
A filter that returns Provisioned Throughputs created before the specified time. 

 ** [maxResults](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-maxResults"></a>
THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a `nextToken` value. To see the next batch of results, send the `nextToken` value in another list request.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [modelArnEquals](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-modelArnEquals"></a>
A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [nameContains](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-nameContains"></a>
A filter that returns Provisioned Throughputs if their name contains the expression that you specify.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+` 

 ** [nextToken](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-nextToken"></a>
If there are more results than the number you specified in the `maxResults` field, the response returns a `nextToken` value. To see the next batch of results, specify the `nextToken` value in this field.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-sortBy"></a>
The field by which to sort the returned list of Provisioned Throughputs.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-sortOrder"></a>
The sort order of the results.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListProvisionedModelThroughputs_RequestSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-request-uri-statusEquals"></a>
A filter that returns Provisioned Throughputs if their statuses matches the value that you specify.  
Valid Values: `Creating | InService | Updating | Failed` 

## Request Body
<a name="API_ListProvisionedModelThroughputs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProvisionedModelThroughputs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "provisionedModelSummaries": [ 
      { 
         "commitmentDuration": "string",
         "commitmentExpirationTime": "string",
         "creationTime": "string",
         "desiredModelArn": "string",
         "desiredModelUnits": number,
         "foundationModelArn": "string",
         "lastModifiedTime": "string",
         "modelArn": "string",
         "modelUnits": number,
         "provisionedModelArn": "string",
         "provisionedModelName": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProvisionedModelThroughputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProvisionedModelThroughputs_ResponseSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-response-nextToken"></a>
If there are more results than the number you specified in the `maxResults` field, this value is returned. To see the next batch of results, include this value in the `nextToken` field in another list request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [provisionedModelSummaries](#API_ListProvisionedModelThroughputs_ResponseSyntax) **   <a name="bedrock-ListProvisionedModelThroughputs-response-provisionedModelSummaries"></a>
A list of summaries, one for each Provisioned Throughput in the response.  
Type: Array of [ProvisionedModelSummary](API_ProvisionedModelSummary.md) objects

## Errors
<a name="API_ListProvisionedModelThroughputs_Errors"></a>

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
<a name="API_ListProvisionedModelThroughputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListProvisionedModelThroughputs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListProvisionedModelThroughputs) 