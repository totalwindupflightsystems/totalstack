---
id: "@specs/aws/quicksight/docs/API_CreateIAMPolicyAssignment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateIAMPolicyAssignment"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateIAMPolicyAssignment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateIAMPolicyAssignment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateIAMPolicyAssignment
<a name="API_CreateIAMPolicyAssignment"></a>

Creates an assignment with one specified IAM policy, identified by its Amazon Resource Name (ARN). This policy assignment is attached to the specified groups or users of Amazon Quick Sight. Assignment names are unique per AWS account. To avoid overwriting rules in other namespaces, use assignment names that are unique.

## Request Syntax
<a name="API_CreateIAMPolicyAssignment_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/iam-policy-assignments/ HTTP/1.1
Content-type: application/json

{
   "AssignmentName": "{{string}}",
   "AssignmentStatus": "{{string}}",
   "Identities": { 
      "{{string}}" : [ "{{string}}" ]
   },
   "PolicyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIAMPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-uri-AwsAccountId"></a>
The ID of the AWS account where you want to assign an IAM policy to Amazon Quick Sight users or groups.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-uri-Namespace"></a>
The namespace that contains the assignment.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_CreateIAMPolicyAssignment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssignmentName](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-AssignmentName"></a>
The name of the assignment, also called a rule. The name must be unique within the AWS account.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`   
Required: Yes

 ** [AssignmentStatus](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-AssignmentStatus"></a>
The status of the assignment. Possible values are as follows:  
+  `ENABLED` - Anything specified in this assignment is used when creating the data source.
+  `DISABLED` - This assignment isn't used when creating the data source.
+  `DRAFT` - This assignment is an unfinished draft and isn't used when creating the data source.
Type: String  
Valid Values: `ENABLED | DRAFT | DISABLED`   
Required: Yes

 ** [Identities](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-Identities"></a>
The Amazon Quick Sight users, groups, or both that you want to assign the policy to.  
Type: String to array of strings map  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+`   
Required: No

 ** [PolicyArn](#API_CreateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-CreateIAMPolicyAssignment-request-PolicyArn"></a>
The ARN for the IAM policy to apply to the Amazon Quick Sight users and groups specified in this assignment.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreateIAMPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AssignmentId": "string",
   "AssignmentName": "string",
   "AssignmentStatus": "string",
   "Identities": { 
      "string" : [ "string" ]
   },
   "PolicyArn": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateIAMPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AssignmentId](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-AssignmentId"></a>
The ID for the assignment.  
Type: String

 ** [AssignmentName](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-AssignmentName"></a>
The name of the assignment. The name must be unique within the AWS account.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$` 

 ** [AssignmentStatus](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-AssignmentStatus"></a>
The status of the assignment. Possible values are as follows:  
+  `ENABLED` - Anything specified in this assignment is used when creating the data source.
+  `DISABLED` - This assignment isn't used when creating the data source.
+  `DRAFT` - This assignment is an unfinished draft and isn't used when creating the data source.
Type: String  
Valid Values: `ENABLED | DRAFT | DISABLED` 

 ** [Identities](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-Identities"></a>
The Amazon Quick Sight users, groups, or both that the IAM policy is assigned to.  
Type: String to array of strings map  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+` 

 ** [PolicyArn](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-PolicyArn"></a>
The ARN for the IAM policy that is applied to the Amazon Quick Sight users and groups specified in this assignment.  
Type: String

 ** [RequestId](#API_CreateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-CreateIAMPolicyAssignment-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateIAMPolicyAssignment_Errors"></a>

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
<a name="API_CreateIAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateIAMPolicyAssignment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateIAMPolicyAssignment) 