---
id: "@specs/aws/quicksight/docs/API_DescribeRoleCustomPermission"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeRoleCustomPermission"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeRoleCustomPermission

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeRoleCustomPermission
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeRoleCustomPermission
<a name="API_DescribeRoleCustomPermission"></a>

Describes all custom permissions that are mapped to a role.

## Request Syntax
<a name="API_DescribeRoleCustomPermission_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/roles/{{Role}}/custom-permission HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRoleCustomPermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeRoleCustomPermission_RequestSyntax) **   <a name="QS-DescribeRoleCustomPermission-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to create a group in. The AWS account ID that you provide must be the same AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DescribeRoleCustomPermission_RequestSyntax) **   <a name="QS-DescribeRoleCustomPermission-request-uri-Namespace"></a>
The namespace that contains the role.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [Role](#API_DescribeRoleCustomPermission_RequestSyntax) **   <a name="QS-DescribeRoleCustomPermission-request-uri-Role"></a>
The name of the role whose permissions you want described.  
Valid Values: `ADMIN | AUTHOR | READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`   
Required: Yes

## Request Body
<a name="API_DescribeRoleCustomPermission_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRoleCustomPermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomPermissionsName": "string",
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_DescribeRoleCustomPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomPermissionsName](#API_DescribeRoleCustomPermission_ResponseSyntax) **   <a name="QS-DescribeRoleCustomPermission-response-CustomPermissionsName"></a>
The name of the custom permission that is described.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9+=,.@_-]+$` 

 ** [RequestId](#API_DescribeRoleCustomPermission_ResponseSyntax) **   <a name="QS-DescribeRoleCustomPermission-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Status](#API_DescribeRoleCustomPermission_ResponseSyntax) **   <a name="QS-DescribeRoleCustomPermission-response-Status"></a>
The HTTP status of the request.  
Type: Integer

## Errors
<a name="API_DescribeRoleCustomPermission_Errors"></a>

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

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeRoleCustomPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeRoleCustomPermission) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeRoleCustomPermission) 