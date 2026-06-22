---
id: "@specs/aws/sesv2/docs/API_ListRecommendations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRecommendations"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListRecommendations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListRecommendations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRecommendations
<a name="API_ListRecommendations"></a>

Lists the recommendations present in your Amazon SES account in the current AWS Region.

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
POST /v2/email/vdm/recommendations HTTP/1.1
Content-type: application/json

{
   "Filter": { 
      "{{string}}" : "{{string}}" 
   },
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_ListRecommendations_RequestSyntax) **   <a name="SES-ListRecommendations-request-Filter"></a>
Filters applied when retrieving recommendations. Can eiter be an individual filter, or combinations of `STATUS` and `IMPACT` or `STATUS` and `TYPE`   
Type: String to string map  
Map Entries: Maximum number of 2 items.  
Valid Keys: `TYPE | IMPACT | STATUS | RESOURCE_ARN`   
Value Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

 ** [NextToken](#API_ListRecommendations_RequestSyntax) **   <a name="SES-ListRecommendations-request-NextToken"></a>
A token returned from a previous call to `ListRecommendations` to indicate the position in the list of recommendations.  
Type: String  
Required: No

 ** [PageSize](#API_ListRecommendations_RequestSyntax) **   <a name="SES-ListRecommendations-request-PageSize"></a>
The number of results to show in a single call to `ListRecommendations`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.  
The value you specify has to be at least 1, and can be no more than 100.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Recommendations": [ 
      { 
         "CreatedTimestamp": number,
         "Description": "string",
         "Impact": "string",
         "LastUpdatedTimestamp": number,
         "ResourceArn": "string",
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="SES-ListRecommendations-response-NextToken"></a>
A string token indicating that there might be additional recommendations available to be listed. Use the token provided in the `ListRecommendationsResponse` to use in the subsequent call to `ListRecommendations` with the same parameters to retrieve the next page of recommendations.  
Type: String

 ** [Recommendations](#API_ListRecommendations_ResponseSyntax) **   <a name="SES-ListRecommendations-response-Recommendations"></a>
The recommendations applicable to your account.  
Type: Array of [Recommendation](API_Recommendation.md) objects

## Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListRecommendations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListRecommendations) 