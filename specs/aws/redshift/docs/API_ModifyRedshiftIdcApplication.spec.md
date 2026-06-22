---
id: "@specs/aws/redshift/docs/API_ModifyRedshiftIdcApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyRedshiftIdcApplication"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyRedshiftIdcApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyRedshiftIdcApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyRedshiftIdcApplication
<a name="API_ModifyRedshiftIdcApplication"></a>

Changes an existing Amazon Redshift IAM Identity Center application.

## Request Parameters
<a name="API_ModifyRedshiftIdcApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** RedshiftIdcApplicationArn **   
The ARN for the Redshift application that integrates with IAM Identity Center.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **AuthorizedTokenIssuerList.member.N**   
The authorized token issuer list for the Amazon Redshift IAM Identity Center application to change.  
Type: Array of [AuthorizedTokenIssuer](API_AuthorizedTokenIssuer.md) objects  
Required: No

 ** IamRoleArn **   
The IAM role ARN associated with the Amazon Redshift IAM Identity Center application to change. It has the required permissions to be assumed and invoke the IDC Identity Center API.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** IdcDisplayName **   
The display name for the Amazon Redshift IAM Identity Center application to change. It appears on the console.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Pattern: `[\w+=,.@-]+`   
Required: No

 ** IdentityNamespace **   
The namespace for the Amazon Redshift IAM Identity Center application to change. It determines which managed application verifies the connection token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Pattern: `^[a-zA-Z0-9_+.#@$-]+$`   
Required: No

 **ServiceIntegrations.member.N**   
A collection of service integrations associated with the application.  
Type: Array of [ServiceIntegrationsUnion](API_ServiceIntegrationsUnion.md) objects  
Required: No

## Response Elements
<a name="API_ModifyRedshiftIdcApplication_ResponseElements"></a>

The following element is returned by the service.

 ** RedshiftIdcApplication **   
Contains properties for the Redshift IDC application.  
Type: [RedshiftIdcApplication](API_RedshiftIdcApplication.md) object

## Errors
<a name="API_ModifyRedshiftIdcApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceAccessDenied **   
A dependent service denied access for the integration.  
HTTP Status Code: 403

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** RedshiftIdcApplicationNotExists **   
The application you attempted to find doesn't exist.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyRedshiftIdcApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyRedshiftIdcApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyRedshiftIdcApplication) 