---
id: "@specs/aws/redshift/docs/API_CreateCustomDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomDomainAssociation"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateCustomDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateCustomDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomDomainAssociation
<a name="API_CreateCustomDomainAssociation"></a>

Used to create a custom domain name for a cluster. Properties include the custom domain name, the cluster the custom domain is associated with, and the certificate Amazon Resource Name (ARN).

## Request Parameters
<a name="API_CreateCustomDomainAssociation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The cluster identifier that the custom domain is associated with.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CustomDomainCertificateArn **   
The certificate Amazon Resource Name (ARN) for the custom domain name association.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** CustomDomainName **   
The custom domain name for a custom domain association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`   
Required: Yes

## Response Elements
<a name="API_CreateCustomDomainAssociation_ResponseElements"></a>

The following elements are returned by the service.

 ** ClusterIdentifier **   
The identifier of the cluster that the custom domain is associated with.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** CustomDomainCertExpiryTime **   
The expiration time for the certificate for the custom domain.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** CustomDomainCertificateArn **   
The Amazon Resource Name (ARN) for the certificate associated with the custom domain name.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*` 

 ** CustomDomainName **   
The custom domain name for the association result.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$` 

## Errors
<a name="API_CreateCustomDomainAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** CustomCnameAssociationFault **   
An error occurred when an attempt was made to change the custom domain association.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_CreateCustomDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateCustomDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateCustomDomainAssociation) 