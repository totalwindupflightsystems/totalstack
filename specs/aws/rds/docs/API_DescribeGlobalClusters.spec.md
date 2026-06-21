---
id: "@specs/aws/rds/docs/API_DescribeGlobalClusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeGlobalClusters"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeGlobalClusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeGlobalClusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeGlobalClusters
<a name="API_DescribeGlobalClusters"></a>

Returns information about Aurora global database clusters. This API supports pagination.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

**Note**  
This action only applies to Aurora DB clusters.

## Request Parameters
<a name="API_DescribeGlobalClusters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more global database clusters to describe. This parameter is case-sensitive.  
Currently, the only supported filter is `region`.  
If used, the request returns information about any global cluster with at least one member (primary or secondary) in the specified AWS Regions.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** GlobalClusterIdentifier **   
The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn't case-sensitive.  
Constraints:  
+ If supplied, must match an existing DBClusterIdentifier.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeGlobalClusters` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeGlobalClusters_ResponseElements"></a>

The following elements are returned by the service.

 **GlobalClusters.GlobalClusterMember.N**   
The list of global clusters returned by this request.  
Type: Array of [GlobalCluster](API_GlobalCluster.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeGlobalClusters` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeGlobalClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeGlobalClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeGlobalClusters) 