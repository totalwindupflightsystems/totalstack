---
id: "@specs/aws/amp/docs/API_ListRuleGroupsNamespaces"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRuleGroupsNamespaces"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ListRuleGroupsNamespaces

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ListRuleGroupsNamespaces
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRuleGroupsNamespaces
<a name="API_ListRuleGroupsNamespaces"></a>

Returns a list of rule groups namespaces in a workspace.

## Request Syntax
<a name="API_ListRuleGroupsNamespaces_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/rulegroupsnamespaces?maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRuleGroupsNamespaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRuleGroupsNamespaces_RequestSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-request-uri-maxResults"></a>
The maximum number of results to return. The default is 100.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [name](#API_ListRuleGroupsNamespaces_RequestSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-request-uri-name"></a>
Use this parameter to filter the rule groups namespaces that are returned. Only the namespaces with names that begin with the value that you specify are returned.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*` 

 ** [nextToken](#API_ListRuleGroupsNamespaces_RequestSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-request-uri-nextToken"></a>
The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.  
For example, if your initial request has `maxResults` of 10, and there are 12 rule groups namespaces to return, then your initial request will return 10 and a `nextToken`. Using the next token in a subsequent call will return the remaining 2 namespaces.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [workspaceId](#API_ListRuleGroupsNamespaces_RequestSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-request-uri-workspaceId"></a>
The ID of the workspace containing the rule groups namespaces.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_ListRuleGroupsNamespaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRuleGroupsNamespaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "ruleGroupsNamespaces": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "modifiedAt": number,
         "name": "string",
         "status": { 
            "statusCode": "string",
            "statusReason": "string"
         },
         "tags": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRuleGroupsNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRuleGroupsNamespaces_ResponseSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-response-nextToken"></a>
A token indicating that there are more results to retrieve. You can use this token as part of your next `ListRuleGroupsNamespaces` request to retrieve those results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [ruleGroupsNamespaces](#API_ListRuleGroupsNamespaces_ResponseSyntax) **   <a name="prometheus-ListRuleGroupsNamespaces-response-ruleGroupsNamespaces"></a>
The returned list of rule groups namespaces.  
Type: Array of [RuleGroupsNamespaceSummary](API_RuleGroupsNamespaceSummary.md) objects

## Errors
<a name="API_ListRuleGroupsNamespaces_Errors"></a>

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

 ** ResourceNotFoundException **   
The request references a resources that doesn't exist.    
 ** message **   
Description of the error.  
 ** resourceId **   
Identifier of the resource affected.  
 ** resourceType **   
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_ListRuleGroupsNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/ListRuleGroupsNamespaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ListRuleGroupsNamespaces) 