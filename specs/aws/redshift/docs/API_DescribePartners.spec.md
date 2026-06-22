---
id: "@specs/aws/redshift/docs/API_DescribePartners"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribePartners"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribePartners

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribePartners
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribePartners
<a name="API_DescribePartners"></a>

Returns information about the partner integrations defined for a cluster.

## Request Parameters
<a name="API_DescribePartners_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccountId **   
The AWS account ID that owns the cluster.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]+$`   
Required: Yes

 ** ClusterIdentifier **   
The cluster identifier of the cluster whose partner integration is being described.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: Yes

 ** DatabaseName **   
The name of the database whose partner integration is being described. If database name is not specified, then all databases in the cluster are described.  
Type: String  
Length Constraints: Maximum length of 127.  
Pattern: `^[\p{L}_][\p{L}\p{N}@$#_]+$`   
Required: No

 ** PartnerName **   
The name of the partner that is being described. If partner name is not specified, then all partner integrations are described.  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^[a-zA-Z0-9\-_]+$`   
Required: No

## Response Elements
<a name="API_DescribePartners_ResponseElements"></a>

The following element is returned by the service.

 **PartnerIntegrationInfoList.PartnerIntegrationInfo.N**   
A list of partner integrations.  
Type: Array of [PartnerIntegrationInfo](API_PartnerIntegrationInfo.md) objects

## Errors
<a name="API_DescribePartners_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** UnauthorizedPartnerIntegration **   
The partner integration is not authorized.  
HTTP Status Code: 401

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribePartners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribePartners) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribePartners) 