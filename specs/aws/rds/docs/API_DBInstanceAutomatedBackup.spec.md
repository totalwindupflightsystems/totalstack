---
id: "@specs/aws/rds/docs/API_DBInstanceAutomatedBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBInstanceAutomatedBackup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBInstanceAutomatedBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBInstanceAutomatedBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBInstanceAutomatedBackup
<a name="API_DBInstanceAutomatedBackup"></a>

An automated backup of a DB instance. It consists of system backups, transaction logs, and the database instance properties that existed at the time you deleted the source instance.

## Contents
<a name="API_DBInstanceAutomatedBackup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AdditionalStorageVolumes.member.N **   
The additional storage volumes associated with the automated backup.  
Valid Values: `GP3 | IO2`   
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The allocated storage size for the automated backup in gibibytes (GiB).  
Type: Integer  
Required: No

 ** AvailabilityZone **   
The Availability Zone that the automated backup was created in. For information on AWS Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).  
Type: String  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The retention period for the automated backups.  
Type: Integer  
Required: No

 ** BackupTarget **   
The location where automated backups are stored: Dedicated Local Zones, AWS Outposts or the AWS Region.  
Type: String  
Required: No

 ** DBInstanceArn **   
The Amazon Resource Name (ARN) for the automated backups.  
Type: String  
Required: No

 ** DBInstanceAutomatedBackupsArn **   
The Amazon Resource Name (ARN) for the replicated automated backups.  
Type: String  
Required: No

 ** DBInstanceAutomatedBackupsReplications.DBInstanceAutomatedBackupsReplication.N **   
The list of replications to different AWS Regions associated with the automated backup.  
Type: Array of [DBInstanceAutomatedBackupsReplication](API_DBInstanceAutomatedBackupsReplication.md) objects  
Required: No

 ** DBInstanceIdentifier **   
The identifier for the source DB instance, which can't be changed and which is unique to an AWS Region.  
Type: String  
Required: No

 ** DbiResourceId **   
The resource ID for the source DB instance, which can't be changed and which is unique to an AWS Region.  
Type: String  
Required: No

 ** DedicatedLogVolume **   
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.  
Type: Boolean  
Required: No

 ** Encrypted **   
Indicates whether the automated backup is encrypted.  
Type: Boolean  
Required: No

 ** Engine **   
The name of the database engine for this automated backup.  
Type: String  
Required: No

 ** EngineVersion **   
The version of the database engine for the automated backup.  
Type: String  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.  
Type: Boolean  
Required: No

 ** InstanceCreateTime **   
The date and time when the DB instance was created.  
Type: Timestamp  
Required: No

 ** Iops **   
The IOPS (I/O operations per second) value for the automated backup.  
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key ID for an automated backup.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** LicenseModel **   
The license model information for the automated backup.  
Type: String  
Required: No

 ** MasterUsername **   
The master user name of an automated backup.  
Type: String  
Required: No

 ** MultiTenant **   
Specifies whether the automatic backup is for a DB instance in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).   
Type: Boolean  
Required: No

 ** OptionGroupName **   
The option group the automated backup is associated with. If omitted, the default option group for the engine specified is used.  
Type: String  
Required: No

 ** Port **   
The port number that the automated backup used for connections.  
Default: Inherits from the source DB instance  
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
The earliest and latest time a DB instance can be restored to.  
Type: [RestoreWindow](API_RestoreWindow.md) object  
Required: No

 ** Status **   
A list of status information for an automated backup:  
+  `active` - Automated backups for current instances.
+  `retained` - Automated backups for deleted instances.
+  `creating` - Automated backups that are waiting for the first automated snapshot to be available.
Type: String  
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
The storage throughput for the automated backup.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type associated with the automated backup.  
Type: String  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TdeCredentialArn **   
The ARN from the key store with which the automated backup is associated for TDE encryption.  
Type: String  
Required: No

 ** Timezone **   
The time zone of the automated backup. In most cases, the `Timezone` element is empty. `Timezone` content appears only for Microsoft SQL Server DB instances that were created with a time zone specified.  
Type: String  
Required: No

 ** VpcId **   
The VPC ID associated with the DB instance.  
Type: String  
Required: No

## See Also
<a name="API_DBInstanceAutomatedBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBInstanceAutomatedBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBInstanceAutomatedBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBInstanceAutomatedBackup) 