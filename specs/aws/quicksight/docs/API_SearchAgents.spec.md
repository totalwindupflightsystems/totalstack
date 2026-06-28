---
id: "@specs/aws/quicksight/docs/API_SearchAgents"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchAgents"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchAgents

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchAgents
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchAgents
<a name="API_SearchAgents"></a>

Searches for agents based on specified filters.

## Request Syntax
<a name="API_SearchAgents_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/agents?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_SearchAgents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchAgents_RequestSyntax) **   <a name="QS-SearchAgents-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the agents.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_SearchAgents_RequestSyntax) **   <a name="QS-SearchAgents-request-uri-MaxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_SearchAgents_RequestSyntax) **   <a name="QS-SearchAgents-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_SearchAgents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchAgents_RequestSyntax) **   <a name="QS-SearchAgents-request-Filters"></a>
The filters to apply when searching agents.  
Type: Array of [AgentSearchFilter](API_AgentSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_SearchAgents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentSummaries": [ 
      { 
         "AgentId": "string",
         "Arn": "string",
         "CreatedAt": number,
         "Description": "string",
         "IconId": "string",
         "Name": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentSummaries](#API_SearchAgents_ResponseSyntax) **   <a name="QS-SearchAgents-response-AgentSummaries"></a>
A list of agent summaries.  
Type: Array of [AgentSummary](API_AgentSummary.md) objects

 ** [NextToken](#API_SearchAgents_ResponseSyntax) **   <a name="QS-SearchAgents-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_SearchAgents_ResponseSyntax) **   <a name="QS-SearchAgents-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchAgents_Errors"></a>

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_SearchAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchAgents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchAgents) 