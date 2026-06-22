---
id: "@specs/aws/redshift/docs/API_DescribeClusterSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterSnapshots"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterSnapshots
<a name="API_DescribeClusterSnapshots"></a>

Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by your AWS account. No information is returned for snapshots owned by inactive AWS accounts.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.

If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterExists **   
A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows:   
+ If `ClusterExists` is set to `true`, `ClusterIdentifier` is required.
+ If `ClusterExists` is set to `false` and `ClusterIdentifier` isn't specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned. 
+ If `ClusterExists` is set to `false` and `ClusterIdentifier` is specified for a deleted cluster, snapshots associated with that cluster are returned.
+ If `ClusterExists` is set to `false` and `ClusterIdentifier` is specified for an existing cluster, no snapshots are returned. 
Type: Boolean  
Required: No

 ** ClusterIdentifier **   
The identifier of the cluster which generated the requested snapshots.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EndTime **   
A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: `2012-07-16T18:00:00Z`   
Type: Timestamp  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterSnapshots](#API_DescribeClusterSnapshots) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** OwnerAccount **   
The AWS account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS account, or do not specify the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotArn **   
The Amazon Resource Name (ARN) of the snapshot associated with the message to describe cluster snapshots.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotIdentifier **   
The snapshot identifier of the snapshot about which to return information.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotType **   
The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.  
Valid Values: `automated` \| `manual`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **SortingEntities.SnapshotSortingEntity.N**   
  
Type: Array of [SnapshotSortingEntity](API_SnapshotSortingEntity.md) objects  
Required: No

 ** StartTime **   
A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: `2012-07-16T18:00:00Z`   
Type: Timestamp  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **Snapshots.Snapshot.N**   
A list of [Snapshot](API_Snapshot.md) instances.   
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_DescribeClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterSnapshots_Examples"></a>

### Example
<a name="API_DescribeClusterSnapshots_Example_1"></a>

This example illustrates one usage of DescribeClusterSnapshots.

#### Sample Request
<a name="API_DescribeClusterSnapshots_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusterSnapshots
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterSnapshots_Example_1_Response"></a>

```
<DescribeClusterSnapshotsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterSnapshotsResult>
    <Snapshots>
      <Snapshot>
        <SnapshotRetentionStartTime>2019-12-26T22:38:40.158Z</SnapshotRetentionStartTime>
        <ClusterIdentifier>mycluster</ClusterIdentifier>
        <EncryptedWithHSM>false</EncryptedWithHSM>
        <NumberOfNodes>2</NumberOfNodes>
        <OwnerAccount>123456789012</OwnerAccount>
        <AvailabilityZone>us-east-2a</AvailabilityZone>
        <ClusterVersion>1.0</ClusterVersion>
        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
        <TotalBackupSizeInMegaBytes>55.0</TotalBackupSizeInMegaBytes>
        <VpcId>vpc-a1abc1a1</VpcId>
        <BackupProgressInMegaBytes>31.0</BackupProgressInMegaBytes>
        <CurrentBackupRateInMegaBytesPerSecond>25.5354</CurrentBackupRateInMegaBytesPerSecond>
        <ElapsedTimeInSeconds>1</ElapsedTimeInSeconds>
        <ClusterCreateTime>2019-12-26T20:25:38.716Z</ClusterCreateTime>
        <MasterUsername>adminuser</MasterUsername>
        <DBName>dev</DBName>
        <ActualIncrementalBackupSizeInMegaBytes>31.0</ActualIncrementalBackupSizeInMegaBytes>
        <SnapshotType>manual</SnapshotType>
        <EnhancedVpcRouting>false</EnhancedVpcRouting>
        <SnapshotIdentifier>mysnapshotid</SnapshotIdentifier>
        <NodeType>dc2.large</NodeType>
        <Tags/>
        <RestorableNodeTypes>
          <NodeType>dc2.large</NodeType>
        </RestorableNodeTypes>
        <Encrypted>false</Encrypted>
        <EstimatedSecondsToCompletion>0</EstimatedSecondsToCompletion>
        <Port>5439</Port>
        <MaintenanceTrackName>current</MaintenanceTrackName>
        <SnapshotCreateTime>2019-12-26T22:38:38.944Z</SnapshotCreateTime>
        <Status>available</Status>
      </Snapshot>
    </Snapshots>
  </DescribeClusterSnapshotsResult>
  <ResponseMetadata>
    <RequestId>f1fdebc9-2831-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</DescribeClusterSnapshotsResponse>
```

## See Also
<a name="API_DescribeClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterSnapshots) 