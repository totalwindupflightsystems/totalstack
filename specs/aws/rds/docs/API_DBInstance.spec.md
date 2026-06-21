---
id: "@specs/aws/rds/docs/API_DBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBInstance
<a name="API_DBInstance"></a>

Contains the details of an Amazon RDS DB instance.

This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.

## Contents
<a name="API_DBInstance_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ActivityStreamEngineNativeAuditFieldsIncluded **   
Indicates whether engine-native audit fields are included in the database activity stream.  
Type: Boolean  
Required: No

 ** ActivityStreamKinesisStreamName **   
The name of the Amazon Kinesis data stream used for the database activity stream.  
Type: String  
Required: No

 ** ActivityStreamKmsKeyId **   
The AWS KMS key identifier used for encrypting messages in the database activity stream. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** ActivityStreamMode **   
The mode of the database activity stream. Database events such as a change or access generate an activity stream event. RDS for Oracle always handles these events asynchronously.  
Type: String  
Valid Values: `sync | async`   
Required: No

 ** ActivityStreamPolicyStatus **   
The status of the policy state of the activity stream.  
Type: String  
Valid Values: `locked | unlocked | locking-policy | unlocking-policy`   
Required: No

 ** ActivityStreamStatus **   
The status of the database activity stream.  
Type: String  
Valid Values: `stopped | starting | started | stopping`   
Required: No

 ** AdditionalStorageVolumes.member.N **   
The additional storage volumes associated with the DB instance. RDS supports additional storage volumes for RDS for Oracle and RDS for SQL Server.  
Type: Array of [AdditionalStorageVolumeOutput](API_AdditionalStorageVolumeOutput.md) objects  
Required: No

 ** AllocatedStorage **   
The amount of storage in gibibytes (GiB) allocated for the DB instance.  
Type: Integer  
Required: No

 ** AssociatedRoles.DBInstanceRole.N **   
The AWS Identity and Access Management (IAM) roles associated with the DB instance.  
Type: Array of [DBInstanceRole](API_DBInstanceRole.md) objects  
Required: No

 ** AutomaticRestartTime **   
The time when a stopped DB instance is restarted automatically.  
Type: Timestamp  
Required: No

 ** AutomationMode **   
The automation mode of the RDS Custom DB instance: `full` or `all paused`. If `full`, the DB instance automates monitoring and instance recovery. If `all paused`, the instance pauses automation for the duration set by `--resume-full-automation-mode-minutes`.  
Type: String  
Valid Values: `full | all-paused`   
Required: No

 ** AutoMinorVersionUpgrade **   
Indicates whether minor version patches are applied automatically.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The name of the Availability Zone where the DB instance is located.  
Type: String  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automatic DB snapshots are retained.  
Type: Integer  
Required: No

 ** BackupTarget **   
The location where automated backups and manual snapshots are stored: Dedicated Local Zones, AWS Outposts or the AWS Region.  
Type: String  
Required: No

 ** CACertificateIdentifier **   
The identifier of the CA certificate for this DB instance.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** CertificateDetails **   
The details of the DB instance's server certificate.  
Type: [CertificateDetails](API_CertificateDetails.md) object  
Required: No

 ** CharacterSetName **   
If present, specifies the name of the character set that this instance is associated with.  
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
Indicates whether tags are copied from the DB instance to snapshots of the DB instance.  
This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see `DBCluster`.  
Type: Boolean  
Required: No

 ** CustomerOwnedIpEnabled **   
Indicates whether a customer-owned IP address (CoIP) is enabled for an RDS on Outposts DB instance.  
A *CoIP *provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.  
For more information about RDS on Outposts, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.  
For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the * AWS Outposts User Guide*.  
Type: Boolean  
Required: No

 ** CustomIamInstanceProfile **   
The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:  
+ The profile must exist in your account.
+ The profile must have an IAM role that Amazon EC2 has permissions to assume.
+ The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom`.
For the list of permissions required for the IAM role, see [ Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.  
Type: String  
Required: No

 ** DatabaseInsightsMode **   
The mode of Database Insights that is enabled for the instance.  
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBClusterIdentifier **   
If the DB instance is a member of a DB cluster, indicates the name of the DB cluster that the DB instance is a member of.  
Type: String  
Required: No

 ** DBInstanceArn **   
The Amazon Resource Name (ARN) for the DB instance.  
Type: String  
Required: No

 ** DBInstanceAutomatedBackupsReplications.DBInstanceAutomatedBackupsReplication.N **   
The list of replicated automated backups associated with the DB instance.  
Type: Array of [DBInstanceAutomatedBackupsReplication](API_DBInstanceAutomatedBackupsReplication.md) objects  
Required: No

 ** DBInstanceClass **   
The name of the compute and memory capacity class of the DB instance.  
Type: String  
Required: No

 ** DBInstanceIdentifier **   
The user-supplied database identifier. This identifier is the unique key that identifies a DB instance.  
Type: String  
Required: No

 ** DbInstancePort **   
The port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.  
Type: Integer  
Required: No

 ** DBInstanceStatus **   
The current state of this database.  
For information about DB instance statuses, see [Viewing DB instance status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/accessing-monitoring.html#Overview.DBInstance.Status) in the *Amazon RDS User Guide.*   
Type: String  
Required: No

 ** DbiResourceId **   
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.  
Type: String  
Required: No

 ** DBName **   
The initial database name that you provided (if required) when you created the DB instance. This name is returned for the life of your DB instance. For an RDS for Oracle CDB instance, the name identifies the PDB rather than the CDB.  
Type: String  
Required: No

 ** DBParameterGroups.DBParameterGroup.N **   
The list of DB parameter groups applied to this DB instance.  
Type: Array of [DBParameterGroupStatus](API_DBParameterGroupStatus.md) objects  
Required: No

 ** DBSecurityGroups.DBSecurityGroup.N **   
A list of DB security group elements containing `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.  
Type: Array of [DBSecurityGroupMembership](API_DBSecurityGroupMembership.md) objects  
Required: No

 ** DBSubnetGroup **   
Information about the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.  
Type: [DBSubnetGroup](API_DBSubnetGroup.md) object  
Required: No

 ** DBSystemId **   
The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is only valid for RDS Custom DB instances.  
Type: String  
Required: No

 ** DedicatedLogVolume **   
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
Type: Boolean  
Required: No

 ** DomainMemberships.DomainMembership.N **   
The Active Directory Domain membership records associated with the DB instance.  
Type: Array of [DomainMembership](API_DomainMembership.md) objects  
Required: No

 ** EnabledCloudwatchLogsExports.member.N **   
A list of log types that this DB instance is configured to export to CloudWatch Logs.  
Log types vary by DB engine. For information about the log types for each DB engine, see [Monitoring Amazon RDS log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html) in the *Amazon RDS User Guide.*   
Type: Array of strings  
Required: No

 ** Endpoint **   
The connection endpoint for the DB instance.  
The endpoint might not be shown for instances with the status of `creating`.
Type: [Endpoint](API_Endpoint.md) object  
Required: No

 ** Engine **   
The database engine used for this DB instance.  
Type: String  
Required: No

 ** EngineLifecycleSupport **   
The lifecycle type for the DB instance.  
For more information, see CreateDBInstance.  
Type: String  
Required: No

 ** EngineVersion **   
The version of the database engine.  
Type: String  
Required: No

 ** EnhancedMonitoringResourceArn **   
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.  
Type: String  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled for the DB instance.  
For a list of engine versions that support IAM database authentication, see [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.IamDatabaseAuthentication.html) in the *Amazon RDS User Guide* and [IAM database authentication in Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.html) in the *Amazon Aurora User Guide*.  
Type: Boolean  
Required: No

 ** InstanceCreateTime **   
The date and time when the DB instance was created.  
Type: Timestamp  
Required: No

 ** Iops **   
The Provisioned IOPS (I/O operations per second) value for the DB instance.  
Type: Integer  
Required: No

 ** IsStorageConfigUpgradeAvailable **   
Indicates whether an upgrade is recommended for the storage file system configuration on the DB instance. To migrate to the preferred configuration, you can either create a blue/green deployment, or create a read replica from the DB instance. For more information, see [Upgrading the storage file system for a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem).  
Type: Boolean  
Required: No

 ** KmsKeyId **   
If `StorageEncrypted` is enabled, the AWS KMS key identifier for the encrypted DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** LatestRestorableTime **   
The latest time to which a database in this DB instance can be restored with point-in-time restore.  
Type: Timestamp  
Required: No

 ** LicenseModel **   
The license model information for this DB instance. This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Type: String  
Required: No

 ** ListenerEndpoint **   
The listener connection endpoint for SQL Server Always On.  
Type: [Endpoint](API_Endpoint.md) object  
Required: No

 ** MasterUsername **   
The master username for the DB instance.  
Type: String  
Required: No

 ** MasterUserSecret **   
The secret managed by RDS in AWS Secrets Manager for the master user password.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Type: [MasterUserSecret](API_MasterUserSecret.md) object  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.  
Type: Integer  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.  
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.  
Type: String  
Required: No

 ** MultiAZ **   
Indicates whether the DB instance is a Multi-AZ deployment. This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** MultiTenant **   
Specifies whether the DB instance is in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).  
Type: Boolean  
Required: No

 ** NcharCharacterSetName **   
The name of the NCHAR character set for the Oracle DB instance. This character set specifies the Unicode encoding for data stored in table columns of type NCHAR, NCLOB, or NVARCHAR2.  
Type: String  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide* and [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*   
Valid Values: `IPV4 | DUAL`   
Type: String  
Required: No

 ** OptionGroupMemberships.OptionGroupMembership.N **   
The list of option group memberships for this DB instance.  
Type: Array of [OptionGroupMembership](API_OptionGroupMembership.md) objects  
Required: No

 ** PendingModifiedValues **   
Information about pending changes to the DB instance. This information is returned only when there are pending changes. Specific changes are identified by subelements.  
Type: [PendingModifiedValues](API_PendingModifiedValues.md) object  
Required: No

 ** PercentProgress **   
The progress of the storage optimization operation as a percentage.  
Type: String  
Required: No

 ** PerformanceInsightsEnabled **   
Indicates whether Performance Insights is enabled for the DB instance.  
Type: Boolean  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data.  
Valid Values:  
+  `7` 
+  *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731` 
Default: `7` days  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.  
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).  
Type: String  
Required: No

 ** ProcessorFeatures.ProcessorFeature.N **   
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.  
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects  
Required: No

 ** PromotionTier **   
The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [ Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide*.  
Type: Integer  
Required: No

 ** PubliclyAccessible **   
Indicates whether the DB instance is publicly accessible.  
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBInstance](API_CreateDBInstance.md).  
Type: Boolean  
Required: No

 ** ReadReplicaDBClusterIdentifiers.ReadReplicaDBClusterIdentifier.N **   
The identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica. For example, when you create an Aurora read replica of an RDS for MySQL DB instance, the Aurora MySQL DB cluster for the Aurora read replica is shown. This output doesn't contain information about cross-Region Aurora read replicas.  
Currently, each RDS DB instance can have only one Aurora read replica.
Type: Array of strings  
Required: No

 ** ReadReplicaDBInstanceIdentifiers.ReadReplicaDBInstanceIdentifier.N **   
The identifiers of the read replicas associated with this DB instance.  
Type: Array of strings  
Required: No

 ** ReadReplicaSourceDBClusterIdentifier **   
The identifier of the source DB cluster if this DB instance is a read replica.  
Type: String  
Required: No

 ** ReadReplicaSourceDBInstanceIdentifier **   
The identifier of the source DB instance if this DB instance is a read replica.  
Type: String  
Required: No

 ** ReplicaMode **   
The open mode of a Db2 or an Oracle read replica. The default is `open-read-only`. For more information, see [Working with replicas for Amazon RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html) and [Working with read replicas for Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide*.   
This attribute is only supported in RDS for Db2, RDS for Oracle, and RDS Custom for Oracle.
Type: String  
Valid Values: `open-read-only | mounted`   
Required: No

 ** ResumeFullAutomationModeTime **   
The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.  
Type: Timestamp  
Required: No

 ** SecondaryAvailabilityZone **   
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.  
Type: String  
Required: No

 ** StatusInfos.DBInstanceStatusInfo.N **   
The status of a read replica. If the DB instance isn't a read replica, the value is blank.  
Type: Array of [DBInstanceStatusInfo](API_DBInstanceStatusInfo.md) objects  
Required: No

 ** StorageEncrypted **   
Indicates whether the DB instance is encrypted.  
Type: Boolean  
Required: No

 ** StorageEncryptionType **   
The type of encryption used to protect data at rest in the DB instance. Possible values:  
+  `none` - The DB instance is not encrypted.
+  `sse-rds` - The DB instance is encrypted using an AWS owned KMS key.
+  `sse-kms` - The DB instance is encrypted using a customer managed KMS key or AWS managed KMS key.
Type: String  
Valid Values: `none | sse-kms | sse-rds`   
Required: No

 ** StorageThroughput **   
The storage throughput for the DB instance.  
This setting applies only to the `gp3` storage type.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type associated with the DB instance.  
Type: String  
Required: No

 ** StorageVolumeStatus **   
The detailed status information for storage volumes associated with the DB instance. This information helps identify which specific volume is causing the instance to be in a storage-full state.  
Type: String  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TdeCredentialArn **   
The ARN from the key store with which the instance is associated for TDE encryption.  
Type: String  
Required: No

 ** Timezone **   
The time zone of the DB instance. In most cases, the `Timezone` element is empty. `Timezone` content appears only for RDS for Db2 and RDS for SQL Server DB instances that were created with a time zone specified.  
Type: String  
Required: No

 ** UpgradeRolloutOrder **   
This data type represents the order in which the instances are upgraded.  
+ [first] - Typically used for development or testing environments.
+ [second] - Default order for resources not specifically configured.
+ [last] - Usually reserved for production environments.
Type: String  
Valid Values: `first | second | last`   
Required: No

 ** VpcSecurityGroups.VpcSecurityGroupMembership.N **   
The list of Amazon EC2 VPC security groups that the DB instance belongs to.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects  
Required: No

## See Also
<a name="API_DBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBInstance) 