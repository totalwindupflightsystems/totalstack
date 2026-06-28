---
id: "@specs/aws/quicksight/docs/API_SearchSpaces"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchSpaces"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchSpaces

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchSpaces
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchSpaces
<a name="API_SearchSpaces"></a>

Searches for Amazon QuickSight spaces that match the specified filters.

## Request Syntax
<a name="API_SearchSpaces_RequestSyntax"></a>

```
POST /v1/accounts/{{AwsAccountId}}/search/spaces HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "name": "{{string}}",
         "operator": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchSpaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchSpaces_RequestSyntax) **   <a name="QS-SearchSpaces-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the spaces.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchSpaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchSpaces_RequestSyntax) **   <a name="QS-SearchSpaces-request-Filters"></a>
The filters to apply to the search.  
Type: Array of [SpaceQuicksightSearchFilter](API_SpaceQuicksightSearchFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** [MaxResults](#API_SearchSpaces_RequestSyntax) **   <a name="QS-SearchSpaces-request-MaxResults"></a>
The maximum number of results to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_SearchSpaces_RequestSyntax) **   <a name="QS-SearchSpaces-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.  
Required: No

## Response Syntax
<a name="API_SearchSpaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "spaceArn": "string",
   "spaceId": "string",
   "SpaceSummaries": [ 
      { 
         "consumedSourceDocCount": number,
         "consumedSourceSize": number,
         "createdAt": number,
         "createdBy": "string",
         "createdByArn": "string",
         "description": "string",
         "name": "string",
         "resourcesCount": number,
         "spaceArn": "string",
         "spaceId": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_SearchSpaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_SearchSpaces_ResponseSyntax) **   <a name="QS-SearchSpaces-response-spaceId"></a>
The ID of the space.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_=.+]+` 

 ** [SpaceSummaries](#API_SearchSpaces_ResponseSyntax) **   <a name="QS-SearchSpaces-response-SpaceSummaries"></a>
A list of space summaries that match the search criteria.  
Type: Array of [SpaceSummary](API_SpaceSummary.md) objects

 ** [NextToken](#API_SearchSpaces_ResponseSyntax) **   <a name="QS-SearchSpaces-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [RequestId](#API_SearchSpaces_ResponseSyntax) **   <a name="QS-SearchSpaces-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [spaceArn](#API_SearchSpaces_ResponseSyntax) **   <a name="QS-SearchSpaces-response-spaceArn"></a>
The ARN of the space.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}` 

## Errors
<a name="API_SearchSpaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_SearchSpaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchSpaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchSpaces) 