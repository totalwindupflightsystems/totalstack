---
id: "@specs/aws/quicksight/docs/API_ListIAMPolicyAssignmentsForUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIAMPolicyAssignmentsForUser"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListIAMPolicyAssignmentsForUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListIAMPolicyAssignmentsForUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIAMPolicyAssignmentsForUser
<a name="API_ListIAMPolicyAssignmentsForUser"></a>

Lists all of the IAM policy assignments, including the Amazon Resource Names (ARNs), for the IAM policies assigned to the specified user and group, or groups that the user belongs to.

## Request Syntax
<a name="API_ListIAMPolicyAssignmentsForUser_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/users/{{UserName}}/iam-policy-assignments?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIAMPolicyAssignmentsForUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListIAMPolicyAssignmentsForUser_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the assignments.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListIAMPolicyAssignmentsForUser_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Namespace](#API_ListIAMPolicyAssignmentsForUser_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-request-uri-Namespace"></a>
The namespace of the assignment.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [NextToken](#API_ListIAMPolicyAssignmentsForUser_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

 ** [UserName](#API_ListIAMPolicyAssignmentsForUser_RequestSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-request-uri-UserName"></a>
The name of the user.  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+`   
Required: Yes

## Request Body
<a name="API_ListIAMPolicyAssignmentsForUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIAMPolicyAssignmentsForUser_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActiveAssignments": [ 
      { 
         "AssignmentName": "string",
         "PolicyArn": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListIAMPolicyAssignmentsForUser_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListIAMPolicyAssignmentsForUser_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [ActiveAssignments](#API_ListIAMPolicyAssignmentsForUser_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-response-ActiveAssignments"></a>
The active assignments for this user.  
Type: Array of [ActiveIAMPolicyAssignment](API_ActiveIAMPolicyAssignment.md) objects

 ** [NextToken](#API_ListIAMPolicyAssignmentsForUser_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListIAMPolicyAssignmentsForUser_ResponseSyntax) **   <a name="QS-ListIAMPolicyAssignmentsForUser-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListIAMPolicyAssignmentsForUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConcurrentUpdatingException **   
A resource is already in a state that indicates an operation is happening that must complete before a new update can be applied.  
HTTP Status Code: 500

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

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

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
<a name="API_ListIAMPolicyAssignmentsForUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListIAMPolicyAssignmentsForUser) 