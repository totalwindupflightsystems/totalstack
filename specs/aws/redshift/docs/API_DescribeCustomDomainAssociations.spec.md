---
id: "@specs/aws/redshift/docs/API_DescribeCustomDomainAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCustomDomainAssociations"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeCustomDomainAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeCustomDomainAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCustomDomainAssociations
<a name="API_DescribeCustomDomainAssociations"></a>

Contains information about custom domain associations for a cluster.

## Request Parameters
<a name="API_DescribeCustomDomainAssociations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CustomDomainCertificateArn **   
The certificate Amazon Resource Name (ARN) for the custom domain association.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** CustomDomainName **   
The custom domain name for the custom domain association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`   
Required: No

 ** Marker **   
The marker for the custom domain association.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum records setting for the associated custom domain.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeCustomDomainAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **Associations.Association.N**   
The associations for the custom domain.  
Type: Array of [Association](API_Association.md) objects

 ** Marker **   
The marker for the custom domain association.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeCustomDomainAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomDomainAssociationNotFoundFault **   
An error occurred. The custom domain name couldn't be found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeCustomDomainAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeCustomDomainAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeCustomDomainAssociations) 