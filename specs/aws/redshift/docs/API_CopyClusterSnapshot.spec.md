---
id: "@specs/aws/redshift/docs/API_CopyClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CopyClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CopyClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyClusterSnapshot
<a name="API_CopyClusterSnapshot"></a>

Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.

When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.

 For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CopyClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceSnapshotIdentifier **   
The identifier for the source snapshot.  
Constraints:  
+ Must be the identifier for a valid automated snapshot whose state is `available`.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** TargetSnapshotIdentifier **   
The identifier given to the new manual snapshot.  
Constraints:  
+ Cannot be null, empty, or blank.
+ Must contain from 1 to 255 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique for the AWS account that is making the request.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ManualSnapshotRetentionPeriod **   
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.   
The value must be either -1 or an integer between 1 and 3,653.  
The default value is -1.  
Type: Integer  
Required: No

 ** SourceSnapshotClusterIdentifier **   
The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than \* for the cluster name.  
Constraints:  
+ Must be the identifier for a valid cluster.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_CopyClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CopyClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotAlreadyExists **   
The value specified as a snapshot identifier is already used by an existing snapshot.  
HTTP Status Code: 400

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** ClusterSnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of cluster snapshots.  
HTTP Status Code: 400

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

## Examples
<a name="API_CopyClusterSnapshot_Examples"></a>

### Example
<a name="API_CopyClusterSnapshot_Example_1"></a>

This example illustrates one usage of CopyClusterSnapshot.

#### Sample Request
<a name="API_CopyClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CopyClusterSnapshot
&SourceSnapshotIdentifier=mysnapshotid1
&TargetSnapshotIdentifier=mysnapshotid2
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CopyClusterSnapshot_Example_1_Response"></a>

```
<CopyClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CopyClusterSnapshotResult>
    <Snapshot>
      <SnapshotRetentionStartTime>2019-12-26T19:15:49.354Z</SnapshotRetentionStartTime>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <EncryptedWithHSM>false</EncryptedWithHSM>
      <NumberOfNodes>1</NumberOfNodes>
      <OwnerAccount>123456789012</OwnerAccount>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <TotalBackupSizeInMegaBytes>41.0</TotalBackupSizeInMegaBytes>
      <VpcId>vpc-a1abc1a1</VpcId>
      <BackupProgressInMegaBytes>14.0</BackupProgressInMegaBytes>
      <CurrentBackupRateInMegaBytesPerSecond>0.0</CurrentBackupRateInMegaBytesPerSecond>
      <ElapsedTimeInSeconds>0</ElapsedTimeInSeconds>
      <ClusterCreateTime>2019-12-25T11:21:49.458Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <ActualIncrementalBackupSizeInMegaBytes>14.0</ActualIncrementalBackupSizeInMegaBytes>
      <SnapshotType>manual</SnapshotType>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <SnapshotIdentifier>mysnapshotid2</SnapshotIdentifier>
      <NodeType>dc2.large</NodeType>
      <Tags/>
      <Encrypted>true</Encrypted>
      <EstimatedSecondsToCompletion>-1</EstimatedSecondsToCompletion>
      <Port>5439</Port>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <SnapshotCreateTime>2019-12-26T19:15:48.359Z</SnapshotCreateTime>
      <KmsKeyId>arn:aws:kms:us-east-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY</KmsKeyId>
      <Status>available</Status>
    </Snapshot>
  </CopyClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>45c7d545-2820-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</CopyClusterSnapshotResponse>
```

## See Also
<a name="API_CopyClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CopyClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CopyClusterSnapshot) 