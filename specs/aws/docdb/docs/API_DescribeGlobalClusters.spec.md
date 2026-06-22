---
id: "@specs/aws/docdb/docs/API_DescribeGlobalClusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeGlobalClusters"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeGlobalClusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeGlobalClusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeGlobalClusters
<a name="API_DescribeGlobalClusters"></a>

Returns information about Amazon DocumentDB global clusters. This API supports pagination.

**Note**  
This action only applies to Amazon DocumentDB clusters.

## Request Parameters
<a name="API_DescribeGlobalClusters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more global DB clusters to describe.  
Supported filters: `db-cluster-id` accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list will only include information about the clusters identified by these ARNs.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** GlobalClusterIdentifier **   
The user-supplied cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case-sensitive.  
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
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeGlobalClusters_ResponseElements"></a>

The following elements are returned by the service.

 **GlobalClusters.GlobalClusterMember.N**   
  
Type: Array of [GlobalCluster](API_GlobalCluster.md) objects

 ** Marker **   
  
Type: String

## Errors
<a name="API_DescribeGlobalClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeGlobalClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeGlobalClusters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeGlobalClusters) 