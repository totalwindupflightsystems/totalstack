---
id: "@specs/aws/bedrock-agent/docs/API_ListInferenceProfiles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInferenceProfiles"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListInferenceProfiles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListInferenceProfiles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInferenceProfiles
<a name="API_ListInferenceProfiles"></a>

Returns a list of inference profiles that you can use. For more information, see [Increase throughput and resilience with cross-region inference in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_ListInferenceProfiles_RequestSyntax"></a>

```
GET /inference-profiles?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{typeEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInferenceProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListInferenceProfiles_RequestSyntax) **   <a name="bedrock-ListInferenceProfiles-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListInferenceProfiles_RequestSyntax) **   <a name="bedrock-ListInferenceProfiles-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [typeEquals](#API_ListInferenceProfiles_RequestSyntax) **   <a name="bedrock-ListInferenceProfiles-request-uri-typeEquals"></a>
Filters for inference profiles that match the type you specify.  
+  `SYSTEM_DEFINED` – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.
+  `APPLICATION` – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.
Valid Values: `SYSTEM_DEFINED | APPLICATION` 

## Request Body
<a name="API_ListInferenceProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInferenceProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "inferenceProfileSummaries": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "inferenceProfileArn": "string",
         "inferenceProfileId": "string",
         "inferenceProfileName": "string",
         "models": [ 
            { 
               "modelArn": "string"
            }
         ],
         "status": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [inferenceProfileSummaries](#API_ListInferenceProfiles_ResponseSyntax) **   <a name="bedrock-ListInferenceProfiles-response-inferenceProfileSummaries"></a>
A list of information about each inference profile that you can use.  
Type: Array of [InferenceProfileSummary](API_InferenceProfileSummary.md) objects

 ** [nextToken](#API_ListInferenceProfiles_ResponseSyntax) **   <a name="bedrock-ListInferenceProfiles-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListInferenceProfiles_Errors"></a>

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
<a name="API_ListInferenceProfiles_Examples"></a>

### List information about inference profiles in your Region
<a name="API_ListInferenceProfiles_Example_1"></a>

Run the following example to list information for up to 5 inference profiles in your region:

#### Sample Request
<a name="API_ListInferenceProfiles_Example_1_Request"></a>

```
GET /inference-profiles?maxResults=5 HTTP/1.1
```

## See Also
<a name="API_ListInferenceProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListInferenceProfiles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListInferenceProfiles) 