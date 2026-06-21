---
id: "@specs/aws/rds/docs/API_DescribeDBShardGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBShardGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBShardGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBShardGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBShardGroups
<a name="API_DescribeDBShardGroups"></a>

Describes existing Aurora Limitless Database DB shard groups.

## Request Parameters
<a name="API_DescribeDBShardGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBShardGroupIdentifier **   
The user-supplied DB shard group identifier. If this parameter is specified, information for only the specific DB shard group is returned. This parameter isn't case-sensitive.  
Constraints:  
+ If supplied, must match an existing DB shard group identifier.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more DB shard groups to describe.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBShardGroups` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100  
Type: Integer  
Valid Range: Minimum value of 20. Maximum value of 100.  
Required: No

## Response Elements
<a name="API_DescribeDBShardGroups_ResponseElements"></a>

The following elements are returned by the service.

 **DBShardGroups.DBShardGroup.N**   
Contains a list of DB shard groups for the user.  
Type: Array of [DBShardGroup](API_DBShardGroup.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeDBClusters` request.  
Type: String

## Errors
<a name="API_DescribeDBShardGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBShardGroupNotFound **   
The specified DB shard group name wasn't found.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBShardGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBShardGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBShardGroups) 