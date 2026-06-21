---
id: "@specs/aws/rds/docs/API_CopyDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CopyDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CopyDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDBClusterSnapshot
<a name="API_CopyDBClusterSnapshot"></a>

Copies a snapshot of a DB cluster.

To copy a DB cluster snapshot from a shared manual DB cluster snapshot, `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.

You can copy an encrypted DB cluster snapshot from another AWS Region. In that case, the AWS Region where you call the `CopyDBClusterSnapshot` operation is the destination AWS Region for the encrypted DB cluster snapshot to be copied to. To copy an encrypted DB cluster snapshot from another AWS Region, you must provide the following values:
+  `KmsKeyId` - The AWS Key Management System (AWS KMS) key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region.
+  `TargetDBClusterSnapshotIdentifier` - The identifier for the new copy of the DB cluster snapshot in the destination AWS Region.
+  `SourceDBClusterSnapshotIdentifier` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the ARN format for the source AWS Region and is the same value as the `SourceDBClusterSnapshotIdentifier` in the presigned URL.

To cancel the copy operation once it is in progress, delete the target DB cluster snapshot identified by `TargetDBClusterSnapshotIdentifier` while that DB cluster snapshot is in "copying" status.

For more information on copying encrypted Amazon Aurora DB cluster snapshots from one AWS Region to another, see [ Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html) in the *Amazon Aurora User Guide*.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_CopyDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBClusterSnapshotIdentifier **   
The identifier of the DB cluster snapshot to copy. This parameter isn't case-sensitive.  
Constraints:  
+ Must specify a valid source snapshot in the "available" state.
+ If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.
+ If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN. You can also specify an ARN of a snapshot that is in a different account and a different AWS Region. For more information, go to [ Copying Snapshots Across AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html#USER_CopySnapshot.AcrossRegions) in the *Amazon Aurora User Guide*.
Example: `my-cluster-snapshot1`   
Type: String  
Required: Yes

 ** TargetDBClusterSnapshotIdentifier **   
The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter isn't case-sensitive.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster-snapshot2`   
Type: String  
Required: Yes

 ** CopyTags **   
Specifies whether to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot. By default, tags are not copied.  
Type: Boolean  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted DB cluster snapshot. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the AWS KMS key.  
If you copy an encrypted DB cluster snapshot from your AWS account, you can specify a value for `KmsKeyId` to encrypt the copy with a new KMS key. If you don't specify a value for `KmsKeyId`, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.  
If you copy an encrypted DB cluster snapshot that is shared from another AWS account, then you must specify a value for `KmsKeyId`.  
To copy an encrypted DB cluster snapshot to another AWS Region, you must set `KmsKeyId` to the AWS KMS key identifier you want to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. KMS keys are specific to the AWS Region that they are created in, and you can't use KMS keys from one AWS Region in another AWS Region.  
If you copy an unencrypted DB cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.  
Type: String  
Required: No

 ** PreSignedUrl **   
When you are copying a DB cluster snapshot from one AWS GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the `CopyDBClusterSnapshot` API operation in the AWS Region that contains the source DB cluster snapshot to copy. Use the `PreSignedUrl` parameter when copying an encrypted DB cluster snapshot from another AWS Region. Don't specify `PreSignedUrl` when copying an encrypted DB cluster snapshot in the same AWS Region.  
This setting applies only to AWS GovCloud (US) Regions. It's ignored in other AWS Regions.  
The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API operation that can run in the source AWS Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:  
+  `KmsKeyId` - The AWS KMS key identifier for the KMS key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBClusterSnapshot` operation that is called in the destination AWS Region, and the operation contained in the presigned URL.
+  `DestinationRegion` - The name of the AWS Region that the DB cluster snapshot is to be created in.
+  `SourceDBClusterSnapshotIdentifier` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your `SourceDBClusterSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115`.
To learn how to generate a Signature Version 4 signed request, see [ Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [ Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source AWS Region.
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CopyDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Contains the details for an Amazon RDS DB cluster snapshot  
This data type is used as a response element in the `DescribeDBClusterSnapshots` action.  
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CopyDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotAlreadyExistsFault **   
The user already has a DB cluster snapshot with the given identifier.  
HTTP Status Code: 400

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **   
The supplied value isn't a valid DB cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB snapshots.  
HTTP Status Code: 400

## Examples
<a name="API_CopyDBClusterSnapshot_Examples"></a>

### Example
<a name="API_CopyDBClusterSnapshot_Example_1"></a>

This example illustrates one usage of CopyDBClusterSnapshot.

#### Sample Request
<a name="API_CopyDBClusterSnapshot_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=CopyDBClusterSnapshot
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &SourceDBClusterSnapshotIdentifier=rds%3Asample-cluster-2016-09-14-10-38
    &TargetDBClusterSnapshotIdentifier=cluster-snapshot-copy-1
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160914/us-west-2/rds/aws4_request
    &X-Amz-Date=20160914T164919Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=4503d6112f2ab5332d7d1871cba6b97ddcc9748d3d4da0cb2c219ace80cfd384
```

#### Sample Response
<a name="API_CopyDBClusterSnapshot_Example_1_Response"></a>

```
<CopyDBClusterSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CopyDBClusterSnapshotResult>
    <DBClusterSnapshot>
      <MasterUsername>mymasteruser</MasterUsername>
      <AllocatedStorage>1</AllocatedStorage>
      <SnapshotType>manual</SnapshotType>
      <AvailabilityZones>
        <AvailabilityZone>us-west-2a</AvailabilityZone>
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <AvailabilityZone>us-west-2c</AvailabilityZone>
      </AvailabilityZones>
      <StorageEncrypted>false</StorageEncrypted>
      <Engine>aurora</Engine>
      <Port>0</Port>
      <LicenseModel>aurora</LicenseModel>
      <SnapshotCreateTime>2016-09-14T10:38:05.616Z</SnapshotCreateTime>
      <PercentProgress>100</PercentProgress>
      <VpcId>vpc-e97e7d8d</VpcId>
      <DBClusterSnapshotIdentifier>cluster-snapshot-copy-1</DBClusterSnapshotIdentifier>
      <DBClusterSnapshotArn>arn:aws:rds:us-west-2:123456789012:cluster-snapshot:cluster-snapshot-copy-1</DBClusterSnapshotArn>
      <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
      <ClusterCreateTime>2016-09-13T16:57:52.695Z</ClusterCreateTime>
      <Status>available</Status>
    </DBClusterSnapshot>
  </CopyDBClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>2e861f29-7a9b-11e6-94c8-21ac69ee8f8c</RequestId>
  </ResponseMetadata>
</CopyDBClusterSnapshotResponse>
```

## See Also
<a name="API_CopyDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CopyDBClusterSnapshot) 