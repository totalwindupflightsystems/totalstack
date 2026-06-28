---
id: "@specs/aws/quicksight/docs/API_DescribeUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeUser"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeUser
<a name="API_DescribeUser"></a>

Returns information about a user, given the user name. 

## Request Syntax
<a name="API_DescribeUser_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/users/{{UserName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeUser_RequestSyntax) **   <a name="QS-DescribeUser-request-uri-AwsAccountId"></a>
The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DescribeUser_RequestSyntax) **   <a name="QS-DescribeUser-request-uri-Namespace"></a>
The namespace. Currently, you should set this to `default`.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [UserName](#API_DescribeUser_RequestSyntax) **   <a name="QS-DescribeUser-request-uri-UserName"></a>
The name of the user that you want to describe.  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+`   
Required: Yes

## Request Body
<a name="API_DescribeUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeUser_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "User": { 
      "Active": boolean,
      "Arn": "string",
      "CustomPermissionsName": "string",
      "Email": "string",
      "ExternalLoginFederationProviderType": "string",
      "ExternalLoginFederationProviderUrl": "string",
      "ExternalLoginId": "string",
      "IdentityType": "string",
      "PrincipalId": "string",
      "Role": "string",
      "UserName": "string"
   }
}
```

## Response Elements
<a name="API_DescribeUser_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeUser_ResponseSyntax) **   <a name="QS-DescribeUser-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DescribeUser_ResponseSyntax) **   <a name="QS-DescribeUser-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [User](#API_DescribeUser_ResponseSyntax) **   <a name="QS-DescribeUser-response-User"></a>
The user name.  
Type: [User](API_User.md) object

## Errors
<a name="API_DescribeUser_Errors"></a>

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
<a name="API_DescribeUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeUser) 