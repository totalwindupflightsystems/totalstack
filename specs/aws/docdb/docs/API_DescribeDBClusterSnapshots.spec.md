---
id: "@specs/aws/docdb/docs/API_DescribeDBClusterSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterSnapshots"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeDBClusterSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeDBClusterSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterSnapshots
<a name="API_DescribeDBClusterSnapshots"></a>

Returns information about cluster snapshots. This API operation supports pagination.

## Request Parameters
<a name="API_DescribeDBClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The ID of the cluster to retrieve the list of cluster snapshots for. This parameter can't be used with the `DBClusterSnapshotIdentifier` parameter. This parameter is not case sensitive.   
Constraints:  
+ If provided, must match the identifier of an existing `DBCluster`.
Type: String  
Required: No

 ** DBClusterSnapshotIdentifier **   
A specific cluster snapshot identifier to describe. This parameter can't be used with the `DBClusterIdentifier` parameter. This value is stored as a lowercase string.   
Constraints:  
+ If provided, must match the identifier of an existing `DBClusterSnapshot`.
+ If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IncludePublic **   
Set to `true` to include manual cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise `false`. The default is `false`.  
Type: Boolean  
Required: No

 ** IncludeShared **   
Set to `true` to include shared manual cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise `false`. The default is `false`.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SnapshotType **   
The type of cluster snapshots to be returned. You can specify one of the following values:  
+  `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
+  `manual` - Return all cluster snapshots that you have manually created for your AWS account.
+  `shared` - Return all manual cluster snapshots that have been shared to your AWS account.
+  `public` - Return all cluster snapshots that have been marked as public.
If you don't specify a `SnapshotType` value, then both automated and manual cluster snapshots are returned. You can include shared cluster snapshots with these results by setting the `IncludeShared` parameter to `true`. You can include public cluster snapshots with these results by setting the`IncludePublic` parameter to `true`.  
The `IncludeShared` and `IncludePublic` parameters don't apply for `SnapshotType` values of `manual` or `automated`. The `IncludePublic` parameter doesn't apply when `SnapshotType` is set to `shared`. The `IncludeShared` parameter doesn't apply when `SnapshotType` is set to `public`.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterSnapshots.DBClusterSnapshot.N**   
Provides a list of cluster snapshots.  
Type: Array of [DBClusterSnapshot](API_DBClusterSnapshot.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterSnapshots) 