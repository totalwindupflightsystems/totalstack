---
id: "@specs/aws/emr/docs/API_CreateStudio"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateStudio"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CreateStudio

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CreateStudio
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateStudio
<a name="API_CreateStudio"></a>

Creates a new Amazon EMR Studio.

## Request Syntax
<a name="API_CreateStudio_RequestSyntax"></a>

```
{
   "AuthMode": "{{string}}",
   "DefaultS3Location": "{{string}}",
   "Description": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "EngineSecurityGroupId": "{{string}}",
   "IdcInstanceArn": "{{string}}",
   "IdcUserAssignment": "{{string}}",
   "IdpAuthUrl": "{{string}}",
   "IdpRelayStateParameterName": "{{string}}",
   "Name": "{{string}}",
   "ServiceRole": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrustedIdentityPropagationEnabled": {{boolean}},
   "UserRole": "{{string}}",
   "VpcId": "{{string}}",
   "WorkspaceSecurityGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateStudio_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthMode](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-AuthMode"></a>
Specifies whether the Studio authenticates users using IAM or IAM Identity Center.  
Type: String  
Valid Values: `SSO | IAM`   
Required: Yes

 ** [DefaultS3Location](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-DefaultS3Location"></a>
The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [Description](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-Description"></a>
A detailed description of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [EncryptionKeyArn](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-EncryptionKeyArn"></a>
The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [EngineSecurityGroupId](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-EngineSecurityGroupId"></a>
The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by `VpcId`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [IdcInstanceArn](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-IdcInstanceArn"></a>
 The ARN of the IAM Identity Center instance to create the Studio application.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [IdcUserAssignment](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-IdcUserAssignment"></a>
 Specifies whether IAM Identity Center user assignment is `REQUIRED` or `OPTIONAL`. If the value is set to `REQUIRED`, users must be explicitly assigned to the Studio application to access the Studio.   
Type: String  
Valid Values: `REQUIRED | OPTIONAL`   
Required: No

 ** [IdpAuthUrl](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-IdpAuthUrl"></a>
The authentication endpoint of your identity provider (IdP). Specify this value when you use IAM authentication and want to let federated users log in to a Studio with the Studio URL and credentials from your IdP. Amazon EMR Studio redirects users to this endpoint to enter credentials.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdpRelayStateParameterName](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-IdpRelayStateParameterName"></a>
The name that your identity provider (IdP) uses for its `RelayState` parameter. For example, `RelayState` or `TargetSource`. Specify this value when you use IAM authentication and want to let federated users log in to a Studio using the Studio URL. The `RelayState` parameter differs by IdP.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [Name](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-Name"></a>
A descriptive name for the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [ServiceRole](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-ServiceRole"></a>
The IAM role that the Amazon EMR Studio assumes. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [SubnetIds](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-SubnetIds"></a>
A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by `VpcId`. Studio users can create a Workspace in any of the specified subnets.  
Type: Array of strings  
Required: Yes

 ** [Tags](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-Tags"></a>
A list of tags to associate with the Amazon EMR Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TrustedIdentityPropagationEnabled](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-TrustedIdentityPropagationEnabled"></a>
 A Boolean indicating whether to enable Trusted identity propagation for the Studio. The default value is `false`.   
Type: Boolean  
Required: No

 ** [UserRole](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-UserRole"></a>
The IAM user role that users and groups assume when logged in to an Amazon EMR Studio. Only specify a `UserRole` when you use IAM Identity Center authentication. The permissions attached to the `UserRole` can be scoped down for each user or group using session policies.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [VpcId](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-VpcId"></a>
The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [WorkspaceSecurityGroupId](#API_CreateStudio_RequestSyntax) **   <a name="EMR-CreateStudio-request-WorkspaceSecurityGroupId"></a>
The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by `VpcId`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_CreateStudio_ResponseSyntax"></a>

```
{
   "StudioId": "string",
   "Url": "string"
}
```

## Response Elements
<a name="API_CreateStudio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StudioId](#API_CreateStudio_ResponseSyntax) **   <a name="EMR-CreateStudio-response-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [Url](#API_CreateStudio_ResponseSyntax) **   <a name="EMR-CreateStudio-response-Url"></a>
The unique Studio access URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

## Errors
<a name="API_CreateStudio_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateStudio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/CreateStudio) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CreateStudio) 