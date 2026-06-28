---
id: "@specs/aws/quicksight/docs/API_DeleteIAMPolicyAssignment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteIAMPolicyAssignment"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteIAMPolicyAssignment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteIAMPolicyAssignment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteIAMPolicyAssignment
<a name="API_DeleteIAMPolicyAssignment"></a>

Deletes an existing IAM policy assignment.

## Request Syntax
<a name="API_DeleteIAMPolicyAssignment_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/namespace/{{Namespace}}/iam-policy-assignments/{{AssignmentName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteIAMPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssignmentName](#API_DeleteIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-request-uri-AssignmentName"></a>
The name of the assignment.   
Length Constraints: Minimum length of 1.  
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`   
Required: Yes

 ** [AwsAccountId](#API_DeleteIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-request-uri-AwsAccountId"></a>
The AWS account ID where you want to delete the IAM policy assignment.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DeleteIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-request-uri-Namespace"></a>
The namespace that contains the assignment.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_DeleteIAMPolicyAssignment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteIAMPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AssignmentName": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteIAMPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AssignmentName](#API_DeleteIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-response-AssignmentName"></a>
The name of the assignment.   
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$` 

 ** [RequestId](#API_DeleteIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DeleteIAMPolicyAssignment-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteIAMPolicyAssignment_Errors"></a>

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
<a name="API_DeleteIAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteIAMPolicyAssignment) 