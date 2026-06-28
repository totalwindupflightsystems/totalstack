---
id: "@specs/aws/amp/docs/API_DescribeRuleGroupsNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeRuleGroupsNamespace"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# DescribeRuleGroupsNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_DescribeRuleGroupsNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeRuleGroupsNamespace
<a name="API_DescribeRuleGroupsNamespace"></a>

Returns complete information about one rule groups namespace. To retrieve a list of rule groups namespaces, use `ListRuleGroupsNamespaces`.

## Request Syntax
<a name="API_DescribeRuleGroupsNamespace_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/rulegroupsnamespaces/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRuleGroupsNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-DescribeRuleGroupsNamespace-request-uri-name"></a>
The name of the rule groups namespace that you want information for.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

 ** [workspaceId](#API_DescribeRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-DescribeRuleGroupsNamespace-request-uri-workspaceId"></a>
The ID of the workspace containing the rule groups namespace.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_DescribeRuleGroupsNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRuleGroupsNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ruleGroupsNamespace": { 
      "arn": "string",
      "createdAt": number,
      "data": blob,
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
}
```

## Response Elements
<a name="API_DescribeRuleGroupsNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ruleGroupsNamespace](#API_DescribeRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-DescribeRuleGroupsNamespace-response-ruleGroupsNamespace"></a>
The information about the rule groups namespace.  
Type: [RuleGroupsNamespaceDescription](API_RuleGroupsNamespaceDescription.md) object

## Errors
<a name="API_DescribeRuleGroupsNamespace_Errors"></a>

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
<a name="API_DescribeRuleGroupsNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/DescribeRuleGroupsNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/DescribeRuleGroupsNamespace) 