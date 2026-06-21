---
id: "@specs/aws/rds/docs/API_DescribeDBClusterSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterSnapshots"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterSnapshots
<a name="API_DescribeDBClusterSnapshots"></a>

Returns information about DB cluster snapshots. This API action supports pagination.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DescribeDBClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't be used in conjunction with the `DBClusterSnapshotIdentifier` parameter. This parameter isn't case-sensitive.  
Constraints:  
+ If supplied, must match the identifier of an existing DBCluster.
Type: String  
Required: No

 ** DbClusterResourceId **   
A specific DB cluster resource ID to describe.  
Type: String  
Required: No

 ** DBClusterSnapshotIdentifier **   
A specific DB cluster snapshot identifier to describe. This parameter can't be used in conjunction with the `DBClusterIdentifier` parameter. This value is stored as a lowercase string.  
Constraints:  
+ If supplied, must match the identifier of an existing DBClusterSnapshot.
+ If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more DB cluster snapshots to describe.  
Supported filters:  
+  `db-cluster-id` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).
+  `db-cluster-snapshot-id` - Accepts DB cluster snapshot identifiers.
+  `snapshot-type` - Accepts types of DB cluster snapshots.
+  `engine` - Accepts names of database engines.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IncludePublic **   
Specifies whether to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account. By default, the public snapshots are not included.  
You can share a manual DB cluster snapshot as public by using the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.  
Type: Boolean  
Required: No

 ** IncludeShared **   
Specifies whether to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore. By default, these snapshots are not included.  
You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the `ModifyDBClusterSnapshotAttribute` API action.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterSnapshots` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SnapshotType **   
The type of DB cluster snapshots to be returned. You can specify one of the following values:  
+  `automated` - Return all DB cluster snapshots that have been automatically taken by Amazon RDS for my AWS account.
+  `manual` - Return all DB cluster snapshots that have been taken by my AWS account.
+  `shared` - Return all manual DB cluster snapshots that have been shared to my AWS account.
+  `public` - Return all DB cluster snapshots that have been marked as public.
If you don't specify a `SnapshotType` value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by enabling the `IncludeShared` parameter. You can include public DB cluster snapshots with these results by enabling the `IncludePublic` parameter.  
The `IncludeShared` and `IncludePublic` parameters don't apply for `SnapshotType` values of `manual` or `automated`. The `IncludePublic` parameter doesn't apply when `SnapshotType` is set to `shared`. The `IncludeShared` parameter doesn't apply when `SnapshotType` is set to `public`.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterSnapshots.DBClusterSnapshot.N**   
Provides a list of DB cluster snapshots for the user.  
Type: Array of [DBClusterSnapshot](API_DBClusterSnapshot.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterSnapshots` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBClusterSnapshots_Examples"></a>

### Example
<a name="API_DescribeDBClusterSnapshots_Example_1"></a>

This example illustrates one usage of DescribeDBClusterSnapshots.

#### Sample Request
<a name="API_DescribeDBClusterSnapshots_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=DescribeDBClusterSnapshots
    &IncludePublic=false
    &IncludeShared=true
    &MaxRecords=40
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20230218/us-east-1/rds/aws4_request
    &X-Amz-Date=20230218T204210Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=913f0ec1dfc684ff9c6ef3eab5885258dbb22017c47b1bcd4fed4680e35aef4b
```

#### Sample Response
<a name="API_DescribeDBClusterSnapshots_Example_1_Response"></a>

```
<DescribeDBClusterSnapshotsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBClusterSnapshotsResult>
    <DBClusterSnapshots>
      <DBClusterSnapshot>
        <Port>0</Port>
        <Status>available</Status>
        <Engine>aurora-mysql</Engine>
        <SnapshotType>manual</SnapshotType>
        <LicenseModel>aurora</LicenseModel>
        <DBClusterSnapshotIdentifier>sample-cluster-snapshot1</DBClusterSnapshotIdentifier>
        <SnapshotCreateTime>2022-10-12T17:42:48.271Z</SnapshotCreateTime>
        <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
        <VpcId>vpc-3fabee54</VpcId>
        <ClusterCreateTime>2023-02-06T22:11:13.826Z</ClusterCreateTime>
        <PercentProgress>100</PercentProgress>
        <AllocatedStorage>1</AllocatedStorage>
        <MasterUsername>awsuser</MasterUsername>
      </DBClusterSnapshot>
      <DBClusterSnapshot>
        <Port>0</Port>
        <Status>creating</Status>
        <Engine>aurora-mysql</Engine>
        <SnapshotType>automated</SnapshotType>
        <LicenseModel>aurora</LicenseModel>
        <DBClusterSnapshotIdentifier>rds:sample2-cluster-2022-10-22-03-12</DBClusterSnapshotIdentifier>
        <SnapshotCreateTime>2022-10-22T03:12:09.445Z</SnapshotCreateTime>
        <DBClusterIdentifier>sample2-cluster</DBClusterIdentifier>
        <VpcId>vpc-3fabee54</VpcId>
        <ClusterCreateTime>2023-02-16T18:44:13.633Z</ClusterCreateTime>
        <PercentProgress>0</PercentProgress>
        <AllocatedStorage>1</AllocatedStorage>
        <MasterUsername>awsuser</MasterUsername>
      </DBClusterSnapshot>
      <DBClusterSnapshot>
        <Port>0</Port>
        <Status>creating</Status>
        <Engine>aurora-mysql</Engine>
        <SnapshotType>automated</SnapshotType>
        <LicenseModel>aurora</LicenseModel>
        <DBClusterSnapshotIdentifier>rds:sample-cluster-2014-10-22-08-27</DBClusterSnapshotIdentifier>
        <SnapshotCreateTime>2014-10-22T08:27:08.435Z</SnapshotCreateTime>
        <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
        <VpcId>vpc-3fabee54</VpcId>
        <ClusterCreateTime>2014-10-16T20:11:04.016Z</ClusterCreateTime>
        <PercentProgress>0</PercentProgress>
        <AllocatedStorage>1</AllocatedStorage>
        <MasterUsername>awsuser</MasterUsername>
      </DBClusterSnapshot>
     </DBClusterSnapshots>
  </DescribeDBClusterSnapshotsResult>
  <ResponseMetadata>
    <RequestId>3ff63be1-ceef-11e4-840b-459216ffcb55</RequestId>
  </ResponseMetadata>
</DescribeDBClusterSnapshotsResponse>
```

## See Also
<a name="API_DescribeDBClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterSnapshots) 