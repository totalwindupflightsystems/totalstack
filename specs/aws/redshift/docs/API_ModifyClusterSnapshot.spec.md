---
id: "@specs/aws/redshift/docs/API_ModifyClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterSnapshot
<a name="API_ModifyClusterSnapshot"></a>

Modifies the settings for a snapshot.

This exanmple modifies the manual retention period setting for a cluster snapshot.

## Request Parameters
<a name="API_ModifyClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotIdentifier **   
The identifier of the snapshot whose setting you want to modify.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Force **   
A Boolean option to override an exception if the retention period has already passed.  
Type: Boolean  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.  
If the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.  
The value must be either -1 or an integer between 1 and 3,653.  
Type: Integer  
Required: No

## Response Elements
<a name="API_ModifyClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_ModifyClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyClusterSnapshot_Examples"></a>

### Example
<a name="API_ModifyClusterSnapshot_Example_1"></a>

This example illustrates one usage of ModifyClusterSnapshot.

#### Sample Request
<a name="API_ModifyClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyClusterSnapshot
&ClusterIdentifier=mycluster
&SnapshotIdentifier=mysnapshotid
&ManualSnapshotRetentionPeriod=10
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyClusterSnapshot_Example_1_Response"></a>

```
<ModifyClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyClusterSnapshotResult>
    <Snapshot>
      <SnapshotRetentionStartTime>2019-12-27T18:19:14.966Z</SnapshotRetentionStartTime>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <EncryptedWithHSM>false</EncryptedWithHSM>
      <NumberOfNodes>1</NumberOfNodes>
      <OwnerAccount>123456789012</OwnerAccount>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>10</ManualSnapshotRetentionPeriod>
      <TotalBackupSizeInMegaBytes>62758.0</TotalBackupSizeInMegaBytes>
      <VpcId>vpc-a1abc1a1</VpcId>
      <BackupProgressInMegaBytes>15.0</BackupProgressInMegaBytes>
      <CurrentBackupRateInMegaBytesPerSecond>5.4506</CurrentBackupRateInMegaBytesPerSecond>
      <ClusterCreateTime>2019-12-23T23:21:27.977Z</ClusterCreateTime>
      <ElapsedTimeInSeconds>2</ElapsedTimeInSeconds>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <ActualIncrementalBackupSizeInMegaBytes>15.0</ActualIncrementalBackupSizeInMegaBytes>
      <SnapshotType>manual</SnapshotType>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <ManualSnapshotRemainingDays>9</ManualSnapshotRemainingDays>
      <SnapshotIdentifier>mysnapshotid</SnapshotIdentifier>
      <NodeType>dc2.large</NodeType>
      <Tags/>
      <Encrypted>false</Encrypted>
      <Port>5439</Port>
      <EstimatedSecondsToCompletion>0</EstimatedSecondsToCompletion>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <SnapshotCreateTime>2019-12-27T18:19:12.214Z</SnapshotCreateTime>
      <Status>available</Status>
    </Snapshot>
  </ModifyClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>f377d8a2-28e9-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</ModifyClusterSnapshotResponse>
```

## See Also
<a name="API_ModifyClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterSnapshot) 