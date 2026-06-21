---
id: "@specs/aws/rds/docs/API_CopyDBSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDBSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CopyDBSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CopyDBSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDBSnapshot
<a name="API_CopyDBSnapshot"></a>

Copies the specified DB snapshot. The source DB snapshot must be in the `available` state.

You can copy a snapshot from one AWS Region to another. In that case, the AWS Region where you call the `CopyDBSnapshot` operation is the destination AWS Region for the DB snapshot copy.

This command doesn't apply to RDS Custom.

For more information about copying snapshots, see [Copying a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopyDBSnapshot) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_CopyDBSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBSnapshotIdentifier **   
The identifier for the source DB snapshot.  
If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier. For example, you might specify `rds:mysql-instance1-snapshot-20130805`.  
If you are copying from a shared manual DB snapshot, this parameter must be the Amazon Resource Name (ARN) of the shared DB snapshot.  
If the source snapshot is in a different AWS Region than the copy, specify a valid DB snapshot ARN. You can also specify an ARN of a snapshot that is in a different account and a different AWS Region. For example, you might specify `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805`.  
Constraints:  
+ Must specify a valid source snapshot in the "available" state.
Example: `rds:mydb-2012-04-02-00-01`   
Example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805`   
Type: String  
Required: Yes

 ** TargetDBSnapshotIdentifier **   
The identifier for the copy of the snapshot.  
Constraints:  
+ Can't be null, empty, or blank
+ Must contain from 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `my-db-snapshot`   
Type: String  
Required: Yes

 ** CopyOptionGroup **   
Specifies whether to copy the DB option group associated with the source DB snapshot to the target AWS account and associate with the target DB snapshot. The associated option group can be copied only with cross-account snapshot copy calls.  
Type: Boolean  
Required: No

 ** CopyTags **   
Specifies whether to copy all tags from the source DB snapshot to the target DB snapshot. By default, tags aren't copied.  
Type: Boolean  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted DB snapshot. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you copy an encrypted DB snapshot from your AWS account, you can specify a value for this parameter to encrypt the copy with a new KMS key. If you don't specify a value for this parameter, then the copy of the DB snapshot is encrypted with the same AWS KMS key as the source DB snapshot.  
If you copy an encrypted DB snapshot that is shared from another AWS account, then you must specify a value for this parameter.  
If you specify this parameter when you copy an unencrypted snapshot, the copy is encrypted.  
If you copy an encrypted snapshot to a different AWS Region, then you must specify an AWS KMS key identifier for the destination AWS Region. KMS keys are specific to the AWS Region that they are created in, and you can't use KMS keys from one AWS Region in another AWS Region.  
Type: String  
Required: No

 ** OptionGroupName **   
The name of an option group to associate with the copy of the snapshot.  
Specify this option if you are copying a snapshot from one AWS Region to another, and your DB instance uses a nondefault option group. If your source DB instance uses Transparent Data Encryption for Oracle or Microsoft SQL Server, you must specify this option when copying across AWS Regions. For more information, see [Option group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopySnapshot.Options) in the *Amazon RDS User Guide*.  
Type: String  
Required: No

 ** PreSignedUrl **   
When you are copying a snapshot from one AWS GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the `CopyDBSnapshot` API operation in the source AWS Region that contains the source DB snapshot to copy.  
This setting applies only to AWS GovCloud (US) Regions. It's ignored in other AWS Regions.  
You must specify this parameter when you copy an encrypted DB snapshot from another AWS Region by using the Amazon RDS API. Don't specify `PreSignedUrl` when you are copying an encrypted DB snapshot in the same AWS Region.  
The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API operation that can run in the source AWS Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:  
+  `DestinationRegion` - The AWS Region that the encrypted DB snapshot is copied to. This AWS Region is the same one where the `CopyDBSnapshot` operation is called that contains this presigned URL.

  For example, if you copy an encrypted DB snapshot from the us-west-2 AWS Region to the us-east-1 AWS Region, then you call the `CopyDBSnapshot` operation in the us-east-1 AWS Region and provide a presigned URL that contains a call to the `CopyDBSnapshot` operation in the us-west-2 AWS Region. For this example, the `DestinationRegion` in the presigned URL must be set to the us-east-1 AWS Region.
+  `KmsKeyId` - The AWS KMS key identifier for the KMS key to use to encrypt the copy of the DB snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBSnapshot` operation that is called in the destination AWS Region, and the operation contained in the presigned URL.
+  `SourceDBSnapshotIdentifier` - The DB snapshot identifier for the encrypted snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB snapshot from the us-west-2 AWS Region, then your `SourceDBSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20161115`.
To learn how to generate a Signature Version 4 signed request, see [Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source AWS Region.
Type: String  
Required: No

 ** SnapshotAvailabilityZone **   
Specifies the name of the Availability Zone where RDS stores the DB snapshot. This value is valid only for snapshots that RDS stores on a Dedicated Local Zone.  
Type: String  
Required: No

 ** SnapshotTarget **   
Configures the location where RDS will store copied snapshots.  
Valid Values:  
+  `local` (Dedicated Local Zone)
+  `outposts` (AWS Outposts)
+  `region` (AWS Region)
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TargetCustomAvailabilityZone **   
The external custom Availability Zone (CAZ) identifier for the target CAZ.  
Example: `rds-caz-aiqhTgQv`.  
Type: String  
Required: No

## Response Elements
<a name="API_CopyDBSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBSnapshot **   
Contains the details of an Amazon RDS DB snapshot.  
This data type is used as a response element in the `DescribeDBSnapshots` action.  
Type: [DBSnapshot](API_DBSnapshot.md) object

## Errors
<a name="API_CopyDBSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomAvailabilityZoneNotFound **   
 `CustomAvailabilityZoneId` doesn't refer to an existing custom Availability Zone identifier.  
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **   
 `DBSnapshotIdentifier` is already used by an existing snapshot.  
HTTP Status Code: 400

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** InvalidDBSnapshotState **   
The state of the DB snapshot doesn't allow deletion.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB snapshots.  
HTTP Status Code: 400

## Examples
<a name="API_CopyDBSnapshot_Examples"></a>

### Example
<a name="API_CopyDBSnapshot_Example_1"></a>

This example illustrates one usage of CopyDBSnapshot.

#### Sample Request
<a name="API_CopyDBSnapshot_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CopyDBSnapshot
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBSnapshotIdentifier=arn%3Aaws%3Ards%3Aus-east-1%3A123456789012%3Asnapshot%3Ards%3Amysqldb-2021-04-27-08-16
   &TargetDBSnapshotIdentifier=mysqldb-copy
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140429/us-east-1/rds/aws4_request
   &X-Amz-Date=20210629T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```

#### Sample Response
<a name="API_CopyDBSnapshot_Example_1_Response"></a>

```
<CopyDBSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CopyDBSnapshotResult>
    <DBSnapshot>
      <Port>3306</Port>
      <OptionGroupName>default:mysql-5-6</OptionGroupName>
      <Engine>mysql</Engine>
      <Status>available</Status>
      <SnapshotType>manual</SnapshotType>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.44</EngineVersion>
      <DBInstanceIdentifier>mysqldb</DBInstanceIdentifier>
      <DBSnapshotIdentifier>mysqldb-copy</DBSnapshotIdentifier>
      <SnapshotCreateTime>2021-05-11T06:02:03.422Z</SnapshotCreateTime>
      <OriginalSnapshotCreateTime>2021-04-27T08:16:05.356Z</OriginalSnapshotCreateTime>
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <InstanceCreateTime>2021-04-21T22:24:26.573Z</InstanceCreateTime>
      <PercentProgress>100</PercentProgress>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>admin</MasterUsername>
    </DBSnapshot>
  </CopyDBSnapshotResult>
  <ResponseMetadata>
    <RequestId>2928d60e-beb6-11d3-8e5c-3ccda5460c46</RequestId>
  </ResponseMetadata>
</CopyDBSnapshotResponse>
```

## See Also
<a name="API_CopyDBSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CopyDBSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CopyDBSnapshot) 