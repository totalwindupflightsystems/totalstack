---
id: "@specs/aws/quicksight/docs/API_DescribeIAMPolicyAssignment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIAMPolicyAssignment"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeIAMPolicyAssignment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeIAMPolicyAssignment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIAMPolicyAssignment
<a name="API_DescribeIAMPolicyAssignment"></a>

Describes an existing IAM policy assignment, as specified by the assignment name.

## Request Syntax
<a name="API_DescribeIAMPolicyAssignment_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/iam-policy-assignments/{{AssignmentName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIAMPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssignmentName](#API_DescribeIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-request-uri-AssignmentName"></a>
The name of the assignment, also called a rule.  
Length Constraints: Minimum length of 1.  
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`   
Required: Yes

 ** [AwsAccountId](#API_DescribeIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the assignment that you want to describe.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DescribeIAMPolicyAssignment_RequestSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-request-uri-Namespace"></a>
The namespace that contains the assignment.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_DescribeIAMPolicyAssignment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIAMPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "IAMPolicyAssignment": { 
      "AssignmentId": "string",
      "AssignmentName": "string",
      "AssignmentStatus": "string",
      "AwsAccountId": "string",
      "Identities": { 
         "string" : [ "string" ]
      },
      "PolicyArn": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeIAMPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [IAMPolicyAssignment](#API_DescribeIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-response-IAMPolicyAssignment"></a>
Information describing the IAM policy assignment.  
Type: [IAMPolicyAssignment](API_IAMPolicyAssignment.md) object

 ** [RequestId](#API_DescribeIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-DescribeIAMPolicyAssignment-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeIAMPolicyAssignment_Errors"></a>

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
<a name="API_DescribeIAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeIAMPolicyAssignment) 