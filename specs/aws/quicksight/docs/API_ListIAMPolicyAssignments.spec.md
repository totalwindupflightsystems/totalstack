---
id: "@specs/aws/quicksight/docs/API_ListIAMPolicyAssignments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIAMPolicyAssignments"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListIAMPolicyAssignments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListIAMPolicyAssignments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIAMPolicyAssignments
<a name="API_ListIAMPolicyAssignments"></a>

Lists the IAM policy assignments in the current Amazon Quick Sight account.

## Request Syntax
<a name="API_ListIAMPolicyAssignments_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/v2/iam-policy-assignments?assignment-status={{AssignmentStatus}}&max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIAMPolicyAssignments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssignmentStatus](#API_ListIAMPolicyAssignments_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignments-request-uri-AssignmentStatus"></a>
The status of the assignments.  
Valid Values: `ENABLED | DRAFT | DISABLED` 

 ** [AwsAccountId](#API_ListIAMPolicyAssignments_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignments-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains these IAM policy assignments.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListIAMPolicyAssignments_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignments-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Namespace](#API_ListIAMPolicyAssignments_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignments-request-uri-Namespace"></a>
The namespace for the assignments.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [NextToken](#API_ListIAMPolicyAssignments_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignments-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListIAMPolicyAssignments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIAMPolicyAssignments_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "IAMPolicyAssignments": [ 
      { 
         "AssignmentName": "string",
         "AssignmentStatus": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListIAMPolicyAssignments_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListIAMPolicyAssignments_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignments-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [IAMPolicyAssignments](#API_ListIAMPolicyAssignments_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignments-response-IAMPolicyAssignments"></a>
Information describing the IAM policy assignments.  
Type: Array of [IAMPolicyAssignmentSummary](API_IAMPolicyAssignmentSummary.md) objects

 ** [NextToken](#API_ListIAMPolicyAssignments_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignments-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListIAMPolicyAssignments_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignments-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListIAMPolicyAssignments_Errors"></a>

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

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

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
<a name="API_ListIAMPolicyAssignments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListIAMPolicyAssignments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListIAMPolicyAssignments) 