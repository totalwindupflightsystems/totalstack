---
id: "@specs/aws/redshift/docs/API_DeleteCustomDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomDomainAssociation"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteCustomDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteCustomDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomDomainAssociation
<a name="API_DeleteCustomDomainAssociation"></a>

Contains information about deleting a custom domain association for a cluster.

## Request Parameters
<a name="API_DeleteCustomDomainAssociation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster to delete a custom domain association for.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CustomDomainName **   
The custom domain name for the custom domain association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`   
Required: Yes

## Errors
<a name="API_DeleteCustomDomainAssociation_Errors"></a>

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
<a name="API_DeleteCustomDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteCustomDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteCustomDomainAssociation) 