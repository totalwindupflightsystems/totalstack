---
id: "@specs/aws/quicksight/docs/API_CreateGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateGroup"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateGroup
<a name="API_CreateGroup"></a>

Use the `CreateGroup` operation to create a group in Quick Sight. You can create up to 10,000 groups in a namespace. If you want to create more than 10,000 groups in a namespace, contact AWS Support.

The permissions resource is `arn:aws:quicksight:<your-region>:<relevant-aws-account-id>:group/default/<group-name> `.

The response is a group object.

## Request Syntax
<a name="API_CreateGroup_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/groups HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "GroupName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateGroup_RequestSyntax) **   <a name="QS-CreateGroup-request-uri-AwsAccountId"></a>
The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_CreateGroup_RequestSyntax) **   <a name="QS-CreateGroup-request-uri-Namespace"></a>
The namespace that you want the group to be a part of.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_CreateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GroupName](#API_CreateGroup_RequestSyntax) **   <a name="QS-CreateGroup-request-GroupName"></a>
A name for the group that you want to create.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+`   
Required: Yes

 ** [Description](#API_CreateGroup_RequestSyntax) **   <a name="QS-CreateGroup-request-Description"></a>
A description for the group that you want to create.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

## Response Syntax
<a name="API_CreateGroup_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Group": { 
      "Arn": "string",
      "Description": "string",
      "GroupName": "string",
      "PrincipalId": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateGroup_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateGroup_ResponseSyntax) **   <a name="QS-CreateGroup-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Group](#API_CreateGroup_ResponseSyntax) **   <a name="QS-CreateGroup-response-Group"></a>
The name of the group.  
Type: [Group](API_Group.md) object

 ** [RequestId](#API_CreateGroup_ResponseSyntax) **   <a name="QS-CreateGroup-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateGroup_Errors"></a>

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

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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
<a name="API_CreateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateGroup) 