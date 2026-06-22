---
id: "@specs/aws/redshift/docs/API_DeleteClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteClusterSnapshot
<a name="API_DeleteClusterSnapshot"></a>

Deletes the specified manual snapshot. The snapshot must be in the `available` state, with no other users authorized to access the snapshot. 

Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.

## Request Parameters
<a name="API_DeleteClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotIdentifier **   
The unique identifier of the manual snapshot to be deleted.  
Constraints: Must be the name of an existing snapshot that is in the `available`, `failed`, or `cancelled` state.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotClusterIdentifier **   
The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than \* for the cluster name.  
Constraints: Must be the name of valid cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DeleteClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_DeleteClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

## Examples
<a name="API_DeleteClusterSnapshot_Examples"></a>

### Example
<a name="API_DeleteClusterSnapshot_Example_1"></a>

This example illustrates one usage of DeleteClusterSnapshot.

#### Sample Request
<a name="API_DeleteClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteClusterSnapshot
&SnapshotIdentifier=mysnapshotid
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteClusterSnapshot_Example_1_Response"></a>

```
<DeleteClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DeleteClusterSnapshotResult>
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
      <Encrypted>false</Encrypted>
      <Port>5439</Port>
      <EstimatedSecondsToCompletion>0</EstimatedSecondsToCompletion>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <SnapshotCreateTime>2019-12-26T22:38:38.944Z</SnapshotCreateTime>
      <Status>deleted</Status>
    </Snapshot>
  </DeleteClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>08614243-2839-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</DeleteClusterSnapshotResponse>
```

## See Also
<a name="API_DeleteClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteClusterSnapshot) 