---
id: "@specs/aws/rds/docs/API_DBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterSnapshot
<a name="API_DBClusterSnapshot"></a>

Contains the details for an Amazon RDS DB cluster snapshot

This data type is used as a response element in the `DescribeDBClusterSnapshots` action.

## Contents
<a name="API_DBClusterSnapshot_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllocatedStorage **   
The allocated storage size of the DB cluster snapshot in gibibytes (GiB).  
Type: Integer  
Required: No

 ** AvailabilityZones.AvailabilityZone.N **   
The list of Availability Zones (AZs) where instances in the DB cluster snapshot can be restored.  
Type: Array of strings  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automatic DB snapshots are retained.  
Type: Integer  
Required: No

 ** ClusterCreateTime **   
The time when the DB cluster was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.  
Type: String  
Required: No

 ** DbClusterResourceId **   
The resource ID of the DB cluster that this DB cluster snapshot was created from.  
Type: String  
Required: No

 ** DBClusterSnapshotArn **   
The Amazon Resource Name (ARN) for the DB cluster snapshot.  
Type: String  
Required: No

 ** DBClusterSnapshotIdentifier **   
The identifier for the DB cluster snapshot.  
Type: String  
Required: No

 ** DBSystemId **   
Reserved for future use.  
Type: String  
Required: No

 ** Engine **   
The name of the database engine for this DB cluster snapshot.  
Type: String  
Required: No

 ** EngineMode **   
The engine mode of the database engine for this DB cluster snapshot.  
Type: String  
Required: No

 ** EngineVersion **   
The version of the database engine for this DB cluster snapshot.  
Type: String  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.  
Type: Boolean  
Required: No

 ** KmsKeyId **   
If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** LicenseModel **   
The license model information for this DB cluster snapshot.  
Type: String  
Required: No

 ** MasterUsername **   
The master username for this DB cluster snapshot.  
Type: String  
Required: No

 ** PercentProgress **   
The percentage of the estimated data that has been transferred.  
Type: Integer  
Required: No

 ** Port **   
The port that the DB cluster was listening on at the time of the snapshot.  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.  
Type: String  
Required: No

 ** SnapshotCreateTime **   
The time when the snapshot was taken, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** SnapshotType **   
The type of the DB cluster snapshot.  
Type: String  
Required: No

 ** SourceDBClusterSnapshotArn **   
If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.  
Type: String  
Required: No

 ** Status **   
The status of this DB cluster snapshot. Valid statuses are the following:  
+  `available` 
+  `copying` 
+  `creating` 
Type: String  
Required: No

 ** StorageEncrypted **   
Indicates whether the DB cluster snapshot is encrypted.  
Type: Boolean  
Required: No

 ** StorageEncryptionType **   
The type of encryption used to protect data at rest in the DB cluster snapshot. Possible values:  
+  `none` - The DB cluster snapshot is not encrypted.
+  `sse-rds` - The DB cluster snapshot is encrypted using an AWS owned KMS key.
+  `sse-kms` - The DB cluster snapshot is encrypted using a customer managed KMS key or AWS managed KMS key.
Type: String  
Valid Values: `none | sse-kms | sse-rds`   
Required: No

 ** StorageThroughput **   
The storage throughput for the DB cluster snapshot. The throughput is automatically set based on the IOPS that you provision, and is not configurable.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type associated with the DB cluster snapshot.  
This setting is only for Aurora DB clusters.  
Type: String  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** VpcId **   
The VPC ID associated with the DB cluster snapshot.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterSnapshot) 