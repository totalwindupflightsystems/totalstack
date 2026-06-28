---
id: "@specs/aws/amp/docs/API_ListWorkspaces"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListWorkspaces"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ListWorkspaces

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ListWorkspaces
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListWorkspaces
<a name="API_ListWorkspaces"></a>

Lists all of the Amazon Managed Service for Prometheus workspaces in your account. This includes workspaces being created or deleted. 

## Request Syntax
<a name="API_ListWorkspaces_RequestSyntax"></a>

```
GET /workspaces?alias={{alias}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkspaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [alias](#API_ListWorkspaces_RequestSyntax) **   <a name="prometheus-ListWorkspaces-request-uri-alias"></a>
If this is included, it filters the results to only the workspaces with names that start with the value that you specify here.  
Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.  
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [maxResults](#API_ListWorkspaces_RequestSyntax) **   <a name="prometheus-ListWorkspaces-request-uri-maxResults"></a>
The maximum number of workspaces to return per request. The default is 100.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListWorkspaces_RequestSyntax) **   <a name="prometheus-ListWorkspaces-request-uri-nextToken"></a>
The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.  
For example, if your initial request has `maxResults` of 10, and there are 12 workspaces to return, then your initial request will return 10 and a `nextToken`. Using the next token in a subsequent call will return the remaining 2 workspaces.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_ListWorkspaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkspaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workspaces": [ 
      { 
         "alias": "string",
         "arn": "string",
         "createdAt": number,
         "kmsKeyArn": "string",
         "status": { 
            "statusCode": "string"
         },
         "tags": { 
            "string" : "string" 
         },
         "workspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkspaces_ResponseSyntax) **   <a name="prometheus-ListWorkspaces-response-nextToken"></a>
A token indicating that there are more results to retrieve. You can use this token as part of your next `ListWorkspaces` request to retrieve those results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [workspaces](#API_ListWorkspaces_ResponseSyntax) **   <a name="prometheus-ListWorkspaces-response-workspaces"></a>
An array of `WorkspaceSummary` structures containing information about the workspaces requested.  
Type: Array of [WorkspaceSummary](API_WorkspaceSummary.md) objects

## Errors
<a name="API_ListWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** message **   
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **   
An unexpected error occurred during the processing of the request.    
 ** message **   
Description of the error.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** message **   
Description of the error.  
 ** quotaCode **   
Service quotas code for the originating quota.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.  
 ** serviceCode **   
Service quotas code for the originating service.
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by an AWS service.    
 ** fieldList **   
The field that caused the error, if applicable.  
 ** message **   
Description of the error.  
 ** reason **   
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/ListWorkspaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ListWorkspaces) 