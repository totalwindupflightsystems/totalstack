---
id: "@specs/aws/redshift/docs/API_ModifyCustomDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyCustomDomainAssociation"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyCustomDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyCustomDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyCustomDomainAssociation
<a name="API_ModifyCustomDomainAssociation"></a>

Contains information for changing a custom domain association.

## Request Parameters
<a name="API_ModifyCustomDomainAssociation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster to change a custom domain association for.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CustomDomainCertificateArn **   
The certificate Amazon Resource Name (ARN) for the changed custom domain association.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** CustomDomainName **   
The custom domain name for a changed custom domain association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`   
Required: Yes

## Response Elements
<a name="API_ModifyCustomDomainAssociation_ResponseElements"></a>

The following elements are returned by the service.

 ** ClusterIdentifier **   
The identifier of the cluster associated with the result for the changed custom domain association.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** CustomDomainCertExpiryTime **   
The certificate expiration time associated with the result for the changed custom domain association.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** CustomDomainCertificateArn **   
The certificate Amazon Resource Name (ARN) associated with the result for the changed custom domain association.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*` 

 ** CustomDomainName **   
The custom domain name associated with the result for the changed custom domain association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$` 

## Errors
<a name="API_ModifyCustomDomainAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** CustomCnameAssociationFault **   
An error occurred when an attempt was made to change the custom domain association.  
HTTP Status Code: 400

 ** CustomDomainAssociationNotFoundFault **   
An error occurred. The custom domain name couldn't be found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyCustomDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyCustomDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyCustomDomainAssociation) 