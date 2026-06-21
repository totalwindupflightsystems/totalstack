---
id: "@specs/aws/rds/docs/API_DBClusterAutomatedBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterAutomatedBackup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterAutomatedBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterAutomatedBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterAutomatedBackup
<a name="API_DBClusterAutomatedBackup"></a>

An automated backup of a DB cluster. It consists of system backups, transaction logs, and the database cluster properties that existed at the time you deleted the source cluster.

## Contents
<a name="API_DBClusterAutomatedBackup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllocatedStorage **   
For all database engines except Amazon Aurora, `AllocatedStorage` specifies the allocated storage size in gibibytes (GiB). For Aurora, `AllocatedStorage` always returns 1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.  
Type: Integer  
Required: No

 ** AvailabilityZones.AvailabilityZone.N **   
The Availability Zones where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html).  
Type: Array of strings  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The retention period for the automated backups.  
Type: Integer  
Required: No

 ** ClusterCreateTime **   
The time when the DB cluster was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** DBClusterArn **   
The Amazon Resource Name (ARN) for the source DB cluster.  
Type: String  
Required: No

 ** DBClusterAutomatedBackupsArn **   
The Amazon Resource Name (ARN) for the automated backups.  
Type: String  
Required: No

 ** DBClusterIdentifier **   
The identifier for the source DB cluster, which can't be changed and which is unique to an AWS Region.  
Type: String  
Required: No

 ** DbClusterResourceId **   
The resource ID for the source DB cluster, which can't be changed and which is unique to an AWS Region.  
Type: String  
Required: No

 ** Engine **   
The name of the database engine for this automated backup.  
Type: String  
Required: No

 ** EngineMode **   
The engine mode of the database engine for the automated backup.  
Type: String  
Required: No

 ** EngineVersion **   
The version of the database engine for the automated backup.  
Type: String  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.  
Type: Boolean  
Required: No

 ** Iops **   
The IOPS (I/O operations per second) value for the automated backup.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key ID for an automated backup.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** LicenseModel **   
The license model information for this DB cluster automated backup.  
Type: String  
Required: No

 ** MasterUsername **   
The master user name of the automated backup.  
Type: String  
Required: No

 ** Port **   
The port number that the automated backup used for connections.  
Default: Inherits from the source DB cluster  
Valid Values: `1150-65535`   
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.  
Type: String  
Required: No

 ** Region **   
The AWS Region associated with the automated backup.  
Type: String  
Required: No

 ** RestoreWindow **   
Earliest and latest time an instance can be restored to:  
Type: [RestoreWindow](API_RestoreWindow.md) object  
Required: No

 ** Status **   
A list of status information for an automated backup:  
+  `retained` - Automated backups for deleted clusters.
Type: String  
Required: No

 ** StorageEncrypted **   
Indicates whether the source DB cluster is encrypted.  
Type: Boolean  
Required: No

 ** StorageEncryptionType **   
The type of encryption used to protect data at rest in the automated backup. Possible values:  
+  `none` - The automated backup is not encrypted.
+  `sse-rds` - The automated backup is encrypted using an AWS owned KMS key.
+  `sse-kms` - The automated backup is encrypted using a customer managed KMS key or AWS managed KMS key.
Type: String  
Valid Values: `none | sse-kms | sse-rds`   
Required: No

 ** StorageThroughput **   
The storage throughput for the automated backup. The throughput is automatically set based on the IOPS that you provision, and is not configurable.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type associated with the DB cluster.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: String  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** VpcId **   
The VPC ID associated with the DB cluster.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterAutomatedBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterAutomatedBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterAutomatedBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterAutomatedBackup) 