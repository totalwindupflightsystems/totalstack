---
id: "@specs/aws/emr/docs/API_Studio"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Studio"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Studio

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Studio
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Studio
<a name="API_Studio"></a>

Details for an Amazon EMR Studio including ID, creation time, name, and so on.

## Contents
<a name="API_Studio_Contents"></a>

 ** AuthMode **   <a name="EMR-Type-Studio-AuthMode"></a>
Specifies whether the Amazon EMR Studio authenticates users with IAM or IAM Identity Center.  
Type: String  
Valid Values: `SSO | IAM`   
Required: No

 ** CreationTime **   <a name="EMR-Type-Studio-CreationTime"></a>
The time the Amazon EMR Studio was created.  
Type: Timestamp  
Required: No

 ** DefaultS3Location **   <a name="EMR-Type-Studio-DefaultS3Location"></a>
The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Description **   <a name="EMR-Type-Studio-Description"></a>
The detailed description of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EncryptionKeyArn **   <a name="EMR-Type-Studio-EncryptionKeyArn"></a>
The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EngineSecurityGroupId **   <a name="EMR-Type-Studio-EngineSecurityGroupId"></a>
The ID of the Engine security group associated with the Amazon EMR Studio. The Engine security group allows inbound network traffic from resources in the Workspace security group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** IdcInstanceArn **   <a name="EMR-Type-Studio-IdcInstanceArn"></a>
 The ARN of the IAM Identity Center instance the Studio application belongs to.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** IdcUserAssignment **   <a name="EMR-Type-Studio-IdcUserAssignment"></a>
 Indicates whether the Studio has `REQUIRED` or `OPTIONAL` IAM Identity Center user assignment. If the value is set to `REQUIRED`, users must be explicitly assigned to the Studio application to access the Studio.   
Type: String  
Valid Values: `REQUIRED | OPTIONAL`   
Required: No

 ** IdpAuthUrl **   <a name="EMR-Type-Studio-IdpAuthUrl"></a>
Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** IdpRelayStateParameterName **   <a name="EMR-Type-Studio-IdpRelayStateParameterName"></a>
The name of your identity provider's `RelayState` parameter.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Name **   <a name="EMR-Type-Studio-Name"></a>
The name of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ServiceRole **   <a name="EMR-Type-Studio-ServiceRole"></a>
The name of the IAM role assumed by the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StudioArn **   <a name="EMR-Type-Studio-StudioArn"></a>
The Amazon Resource Name (ARN) of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StudioId **   <a name="EMR-Type-Studio-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** SubnetIds **   <a name="EMR-Type-Studio-SubnetIds"></a>
The list of IDs of the subnets associated with the Amazon EMR Studio.  
Type: Array of strings  
Required: No

 ** Tags **   <a name="EMR-Type-Studio-Tags"></a>
A list of tags associated with the Amazon EMR Studio.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TrustedIdentityPropagationEnabled **   <a name="EMR-Type-Studio-TrustedIdentityPropagationEnabled"></a>
 Indicates whether the Studio has Trusted identity propagation enabled. The default value is `false`.   
Type: Boolean  
Required: No

 ** Url **   <a name="EMR-Type-Studio-Url"></a>
The unique access URL of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** UserRole **   <a name="EMR-Type-Studio-UserRole"></a>
The name of the IAM role assumed by users logged in to the Amazon EMR Studio. A Studio only requires a `UserRole` when you use IAM authentication.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** VpcId **   <a name="EMR-Type-Studio-VpcId"></a>
The ID of the VPC associated with the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** WorkspaceSecurityGroupId **   <a name="EMR-Type-Studio-WorkspaceSecurityGroupId"></a>
The ID of the Workspace security group associated with the Amazon EMR Studio. The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_Studio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Studio) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Studio) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Studio) 