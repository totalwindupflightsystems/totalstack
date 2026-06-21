---
id: "@specs/aws/rds/docs/API_RestoreDBInstanceFromS3"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreDBInstanceFromS3"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RestoreDBInstanceFromS3

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RestoreDBInstanceFromS3
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreDBInstanceFromS3
<a name="API_RestoreDBInstanceFromS3"></a>

Amazon Relational Database Service (Amazon RDS) supports importing MySQL databases by using backup files. You can create a backup of your on-premises database, store it on Amazon Simple Storage Service (Amazon S3), and then restore the backup file onto a new Amazon RDS DB instance running MySQL. For more information, see [Restoring a backup into an Amazon RDS for MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html) in the *Amazon RDS User Guide.* 

This operation doesn't apply to RDS Custom.

## Request Parameters
<a name="API_RestoreDBInstanceFromS3_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceClass **   
The compute and memory capacity of the DB instance, for example db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide.*   
Importing from Amazon S3 isn't supported on the db.t2.micro DB instance class.  
Type: String  
Required: Yes

 ** DBInstanceIdentifier **   
The DB instance identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`   
Type: String  
Required: Yes

 ** Engine **   
The name of the database engine to be used for this instance.  
Valid Values: `mysql`   
Type: String  
Required: Yes

 ** S3BucketName **   
The name of your Amazon S3 bucket that contains your database backup file.  
Type: String  
Required: Yes

 ** S3IngestionRoleArn **   
An AWS Identity and Access Management (IAM) role with a trust policy and a permissions policy that allows Amazon RDS to access your Amazon S3 bucket. For information about this role, see [ Creating an IAM role manually](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html#MySQL.Procedural.Importing.Enabling.IAM) in the *Amazon RDS User Guide.*   
Type: String  
Required: Yes

 ** SourceEngine **   
The name of the engine of your source database.  
Valid Values: `mysql`   
Type: String  
Required: Yes

 ** SourceEngineVersion **   
The version of the database that the backup files were created from.  
MySQL versions 5.6 and 5.7 are supported.  
Example: `5.6.40`   
Type: String  
Required: Yes

 **AdditionalStorageVolumes.member.N**   
A list of additional storage volumes to modify or delete for the DB instance. You can modify or delete up to three additional storage volumes using the names `rdsdbdata2`, `rdsdbdata3`, and `rdsdbdata4`. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.  
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The amount of storage (in gibibytes) to allocate initially for the DB instance. Follow the allocation rules specified in `CreateDBInstance`.  
This setting isn't valid for RDS for SQL Server.  
Be sure to allocate enough storage for your new DB instance so that the restore operation can succeed. You can also allocate additional storage for future growth.
Type: Integer  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether to automatically apply minor engine upgrades to the DB instance during the maintenance window. By default, minor engine upgrades are not applied automatically.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The Availability Zone that the DB instance is created in. For information about AWS Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) in the *Amazon RDS User Guide.*   
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.  
Example: `us-east-1d`   
Constraint: The `AvailabilityZone` parameter can't be specified if the DB instance is a Multi-AZ deployment. The specified Availability Zone must be in the same AWS Region as the current endpoint.  
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. For more information, see `CreateDBInstance`.  
Type: Integer  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the DB instance's server certificate.  
This setting doesn't apply to RDS Custom DB instances.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.  
Type: Boolean  
Required: No

 ** DatabaseInsightsMode **   
Specifies the mode of Database Insights to enable for the DB instance.  
Aurora DB instances inherit this value from the DB cluster, so you can't change this value.
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBName **   
The name of the database to create when the DB instance is created. Follow the naming rules specified in `CreateDBInstance`.  
Type: String  
Required: No

 ** DBParameterGroupName **   
The name of the DB parameter group to associate with this DB instance.  
If you do not specify a value for `DBParameterGroupName`, then the default `DBParameterGroup` for the specified DB engine is used.  
Type: String  
Required: No

 **DBSecurityGroups.DBSecurityGroupName.N**   
A list of DB security groups to associate with this DB instance.  
Default: The default DB security group for the database engine.  
Type: Array of strings  
Required: No

 ** DBSubnetGroupName **   
A DB subnet group to associate with this DB instance.  
Constraints: If supplied, must match the name of an existing DBSubnetGroup.  
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DedicatedLogVolume **   
Specifies whether to enable a dedicated log volume (DLV) for the DB instance.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether to enable deletion protection for the DB instance. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
Type: Boolean  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
The list of logs that the restored DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
Type: Array of strings  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
For more information about IAM database authentication, see [ IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*   
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to enable Performance Insights for the DB instance.  
For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.  
Type: Boolean  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this DB instance.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, RDS automatically upgrades your restored DB instance to a higher engine version, if the major engine version is past its end of standard support date.
You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide*.  
This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the life cycle type is managed by the DB cluster.  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine to use. Choose the latest minor version of your database engine. For information about engine versions, see `CreateDBInstance`, or call `DescribeDBEngineVersions`.  
Type: String  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to allocate initially for the DB instance. For information about valid IOPS values, see [Amazon RDS Provisioned IOPS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide.*   
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
If the `StorageEncrypted` parameter is enabled, and you do not specify a value for the `KmsKeyId` parameter, then Amazon RDS will use your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** LicenseModel **   
The license model for this DB instance. Use `general-public-license`.  
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
Type: Boolean  
Required: No

 ** MasterUsername **   
The name for the master user.  
Constraints:  
+ Must be 1 to 16 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
Type: String  
Required: No

 ** MasterUserPassword **   
The password for the master user.  
Constraints:  
+ Can't be specified if `ManageMasterUserPassword` is turned on.
+ Can include any printable ASCII character except "/", """, or "@". For RDS for Oracle, can't include the "&" (ampersand) or the "'" (single quotes) character.
Length Constraints:  
+ RDS for Db2 - Must contain from 8 to 128 characters.
+ RDS for MariaDB - Must contain from 8 to 41 characters.
+ RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.
+ RDS for MySQL - Must contain from 8 to 41 characters.
+ RDS for Oracle - Must contain from 8 to 30 characters.
+ RDS for PostgreSQL - Must contain from 8 to 128 characters.
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.  
For more information about this setting, including limitations that apply to it, see [ Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.  
Type: Integer  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0.  
If `MonitoringRoleArn` is specified, then you must also set `MonitoringInterval` to a value other than 0.  
Valid Values: 0, 1, 5, 10, 15, 30, 60  
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [Setting Up and Enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide.*   
If `MonitoringInterval` is set to a value other than 0, then you must supply a `MonitoringRoleArn` value.  
Type: String  
Required: No

 ** MultiAZ **   
Specifies whether the DB instance is a Multi-AZ deployment. If the DB instance is a Multi-AZ deployment, you can't set the `AvailabilityZone` parameter.  
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
Valid Values:  
+  `IPV4` 
+  `DUAL` 
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*   
Type: String  
Required: No

 ** OptionGroupName **   
The name of the option group to associate with this DB instance. If this argument is omitted, the default option group for the specified engine is used.  
Type: String  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you do not specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data. The default is 7 days. The following values are valid:  
+ 7
+  *month* \* 31, where *month* is a number of months from 1-23
+ 731
For example, the following values are valid:  
+ 93 (3 months \* 31)
+ 341 (11 months \* 31)
+ 589 (19 months \* 31)
+ 731
If you specify a retention period such as 94, which isn't a valid value, RDS issues an error.  
Type: Integer  
Required: No

 ** Port **   
The port number on which the database accepts connections.  
Type: Integer  
Valid Values: `1150`-`65535`   
Default: `3306`   
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The time range each day during which automated backups are created if automated backups are enabled. For more information, see [Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide.*   
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC). For more information, see [Amazon RDS Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) in the *Amazon RDS User Guide.*   
Constraints:  
+ Must be in the format `ddd:hh24:mi-ddd:hh24:mi`.
+ Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred backup window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 **ProcessorFeatures.ProcessorFeature.N**   
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.  
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB instance is publicly accessible.  
When the DB instance is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB instance's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB instance's VPC. Access to the DB instance is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB instance doesn't permit it.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBInstance](API_CreateDBInstance.md).  
Type: Boolean  
Required: No

 ** S3Prefix **   
The prefix of your Amazon S3 bucket.  
Type: String  
Required: No

 ** StorageEncrypted **   
Specifies whether the new DB instance is encrypted or not.  
Type: Boolean  
Required: No

 ** StorageThroughput **   
Specifies the storage throughput value for the DB instance.  
This setting doesn't apply to RDS Custom or Amazon Aurora.  
Type: Integer  
Required: No

 ** StorageType **   
Specifies the storage type to be associated with the DB instance.  
Valid Values: `gp2 | gp3 | io1 | io2 | standard`   
If you specify `io1`, `io2`, or `gp3`, you must also include a value for the `Iops` parameter.  
Default: `io1` if the `Iops` parameter is specified; otherwise `gp2`   
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags to associate with this DB instance. For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide.*   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB instance.  
Valid Values:   
+  `auto-backup` - The DB instance's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

 ** UseDefaultProcessorFeatures **   
Specifies whether the DB instance class of the DB instance uses its default processor features.  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of VPC security groups to associate with this DB instance.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_RestoreDBInstanceFromS3_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_RestoreDBInstanceFromS3_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **   
The specified CIDR IP range or Amazon EC2 security group might not be authorized for the specified DB security group.  
Or, RDS might not be authorized to perform necessary actions using IAM on your behalf.  
HTTP Status Code: 404

 ** BackupPolicyNotFoundFault **   
 *This error has been deprecated.*   
  
HTTP Status Code: 404

 ** CertificateNotFound **   
 `CertificateIdentifier` doesn't refer to an existing certificate.  
HTTP Status Code: 404

 ** DBInstanceAlreadyExists **   
The user already has a DB instance with the given identifier.  
HTTP Status Code: 400

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** InstanceQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB instances.  
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidS3BucketFault **   
The specified Amazon S3 bucket name can't be found or Amazon RDS isn't authorized to access the specified Amazon S3 bucket. Verify the **SourceS3BucketName** and **S3IngestionRoleArn** values and try again.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The DB subnet group doesn't cover all Availability Zones after it's created because of users' change.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** NetworkTypeNotSupported **   
The network type is invalid for the DB instance. Valid nework type values are `IPV4` and `DUAL`.  
HTTP Status Code: 400

 ** OptionGroupNotFoundFault **   
The specified option group could not be found.  
HTTP Status Code: 404

 ** ProvisionedIopsNotAvailableInAZFault **   
Provisioned IOPS not available in the specified Availability Zone.  
HTTP Status Code: 400

 ** StorageQuotaExceeded **   
The request would result in the user exceeding the allowed amount of storage available across all DB instances.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## See Also
<a name="API_RestoreDBInstanceFromS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RestoreDBInstanceFromS3) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RestoreDBInstanceFromS3) 