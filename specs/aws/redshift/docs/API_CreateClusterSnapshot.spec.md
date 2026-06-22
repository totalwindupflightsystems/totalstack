---
id: "@specs/aws/redshift/docs/API_CreateClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateClusterSnapshot
<a name="API_CreateClusterSnapshot"></a>

Creates a manual snapshot of the specified cluster. The cluster must be in the `available` state. 

 For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CreateClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The cluster identifier for which you want a snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotIdentifier **   
A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.  
Constraints:  
+ Cannot be null, empty, or blank
+ Must contain from 1 to 255 alphanumeric characters or hyphens
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Example: `my-snapshot-id`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ManualSnapshotRetentionPeriod **   
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.   
The value must be either -1 or an integer between 1 and 3,653.  
The default value is -1.  
Type: Integer  
Required: No

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CreateClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotAlreadyExists **   
The value specified as a snapshot identifier is already used by an existing snapshot.  
HTTP Status Code: 400

 ** ClusterSnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of cluster snapshots.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateClusterSnapshot_Examples"></a>

### Example
<a name="API_CreateClusterSnapshot_Example_1"></a>

This example illustrates one usage of CreateClusterSnapshot.

#### Sample Request
<a name="API_CreateClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateClusterSnapshot
&SnapshotIdentifier=mysnapshotid
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateClusterSnapshot_Example_1_Response"></a>

```
<CreateClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateClusterSnapshotResult>
    <Snapshot>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <EncryptedWithHSM>false</EncryptedWithHSM>
      <NumberOfNodes>2</NumberOfNodes>
      <OwnerAccount>123456789012</OwnerAccount>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <TotalBackupSizeInMegaBytes>-1.0</TotalBackupSizeInMegaBytes>
      <VpcId>vpc-a1abc1a1</VpcId>
      <BackupProgressInMegaBytes>0.0</BackupProgressInMegaBytes>
      <CurrentBackupRateInMegaBytesPerSecond>0.0</CurrentBackupRateInMegaBytesPerSecond>
      <ElapsedTimeInSeconds>0</ElapsedTimeInSeconds>
      <ClusterCreateTime>2019-12-26T20:25:38.716Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <ActualIncrementalBackupSizeInMegaBytes>-1.0</ActualIncrementalBackupSizeInMegaBytes>
      <SnapshotType>manual</SnapshotType>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <SnapshotIdentifier>mysnapshotid</SnapshotIdentifier>
      <NodeType>dc2.large</NodeType>
      <Tags/>
      <Encrypted>false</Encrypted>
      <EstimatedSecondsToCompletion>-1</EstimatedSecondsToCompletion>
      <Port>5439</Port>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <SnapshotCreateTime>2019-12-26T22:38:18.854Z</SnapshotCreateTime>
      <Status>creating</Status>
    </Snapshot>
  </CreateClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>69dec674-2830-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</CreateClusterSnapshotResponse>
```

## See Also
<a name="API_CreateClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateClusterSnapshot) 