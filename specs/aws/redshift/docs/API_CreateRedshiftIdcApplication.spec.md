---
id: "@specs/aws/redshift/docs/API_CreateRedshiftIdcApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRedshiftIdcApplication"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateRedshiftIdcApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateRedshiftIdcApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRedshiftIdcApplication
<a name="API_CreateRedshiftIdcApplication"></a>

Creates an Amazon Redshift application for use with IAM Identity Center.

## Request Parameters
<a name="API_CreateRedshiftIdcApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IamRoleArn **   
The IAM role ARN for the Amazon Redshift IAM Identity Center application instance. It has the required permissions to be assumed and invoke the IDC Identity Center API.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** IdcDisplayName **   
The display name for the Amazon Redshift IAM Identity Center application instance. It appears in the console.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Pattern: `[\w+=,.@-]+`   
Required: Yes

 ** IdcInstanceArn **   
The Amazon resource name (ARN) of the IAM Identity Center instance where Amazon Redshift creates a new managed application.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** RedshiftIdcApplicationName **   
The name of the Redshift application in IAM Identity Center.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`   
Required: Yes

 ** ApplicationType **   
The type of application being created. Valid values are `None` or `Lakehouse`. Use `Lakehouse` to enable Amazon Redshift federated permissions on cluster.  
Type: String  
Valid Values: `None | Lakehouse`   
Required: No

 **AuthorizedTokenIssuerList.member.N**   
The token issuer list for the Amazon Redshift IAM Identity Center application instance.  
Type: Array of [AuthorizedTokenIssuer](API_AuthorizedTokenIssuer.md) objects  
Required: No

 ** IdentityNamespace **   
The namespace for the Amazon Redshift IAM Identity Center application instance. It determines which managed application verifies the connection token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Pattern: `^[a-zA-Z0-9_+.#@$-]+$`   
Required: No

 **ServiceIntegrations.member.N**   
A collection of service integrations for the Redshift IAM Identity Center application.  
Type: Array of [ServiceIntegrationsUnion](API_ServiceIntegrationsUnion.md) objects  
Required: No

 **SsoTagKeys.TagKey.N**   
A list of tags keys that Redshift Identity Center applications copy to IAM Identity Center. For each input key, the tag corresponding to the key-value pair is propagated.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **Tags.Tag.N**   
A list of tags.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateRedshiftIdcApplication_ResponseElements"></a>

The following element is returned by the service.

 ** RedshiftIdcApplication **   
Contains properties for the Redshift IDC application.  
Type: [RedshiftIdcApplication](API_RedshiftIdcApplication.md) object

## Errors
<a name="API_CreateRedshiftIdcApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceAccessDenied **   
A dependent service denied access for the integration.  
HTTP Status Code: 403

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** RedshiftIdcApplicationAlreadyExists **   
The application you attempted to add already exists.  
HTTP Status Code: 400

 ** RedshiftIdcApplicationQuotaExceeded **   
The maximum number of Redshift IAM Identity Center applications was exceeded.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_CreateRedshiftIdcApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateRedshiftIdcApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateRedshiftIdcApplication) 