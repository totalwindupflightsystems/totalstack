---
id: "@specs/aws/rds/docs/API_RestoreDBInstanceToPointInTime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreDBInstanceToPointInTime"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RestoreDBInstanceToPointInTime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RestoreDBInstanceToPointInTime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreDBInstanceToPointInTime
<a name="API_RestoreDBInstanceToPointInTime"></a>

Restores a DB instance to an arbitrary point in time. You can restore to any point in time before the time identified by the `LatestRestorableTime` property. You can restore to a point up to the number of days specified by the `BackupRetentionPeriod` property.

The target database is created with most of the original configuration, but in a system-selected Availability Zone, with the default security group, the default subnet group, and the default DB parameter group. By default, the new DB instance is created as a single-AZ deployment except when the instance is a SQL Server instance that has an option group that is associated with mirroring; in this case, the instance becomes a mirrored deployment and not a single-AZ deployment.

**Note**  
This operation doesn't apply to Aurora MySQL and Aurora PostgreSQL. For Aurora, use `RestoreDBClusterToPointInTime`.

## Request Parameters
<a name="API_RestoreDBInstanceToPointInTime_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TargetDBInstanceIdentifier **   
The name of the new DB instance to create.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: Yes

 **AdditionalStorageVolumes.member.N**   
A list of additional storage volumes to restore to the DB instance. You can restore up to three additional storage volumes using the names `rdsdbdata2`, `rdsdbdata3`, and `rdsdbdata4`. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.  
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The amount of storage (in gibibytes) to allocate initially for the DB instance. Follow the allocation rules specified in `CreateDBInstance`.  
This setting isn't valid for RDS for SQL Server.  
Be sure to allocate enough storage for your new DB instance so that the restore operation can succeed. You can also allocate additional storage for future growth.
Type: Integer  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window.  
This setting doesn't apply to RDS Custom.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The Availability Zone (AZ) where the DB instance will be created.  
Default: A random, system-chosen Availability Zone.  
Constraints:  
+ You can't specify the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.
Example: `us-east-1a`   
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.  
Enabling and disabling backups can result in a brief I/O suspension that lasts from a few seconds to a few minutes, depending on the size and class of your DB instance.
This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster. For more information, see `ModifyDBCluster`.  
Default: Uses existing setting  
Constraints:  
+ Must be a value from 0 to 35.
+ Can't be set to 0 if the DB instance is a source to read replicas.
+ Can't be set to 0 for an RDS Custom for Oracle DB instance.
Type: Integer  
Required: No

 ** BackupTarget **   
The location for storing automated backups and manual snapshots for the restored DB instance.  
Valid Values:  
+  `local` (Dedicated Local Zone)
+  `outposts` (AWS Outposts)
+  `region` (AWS Region)
Default: `region`   
For more information, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.  
Type: String  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the DB instance's server certificate.  
This setting doesn't apply to RDS Custom DB instances.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the restored DB instance to snapshots of the DB instance. By default, tags are not copied.  
Type: Boolean  
Required: No

 ** CustomIamInstanceProfile **   
The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:  
+ The profile must exist in your account.
+ The profile must have an IAM role that Amazon EC2 has permissions to assume.
+ The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom`.
For the list of permissions required for the IAM role, see [ Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.  
This setting is required for RDS Custom.  
Type: String  
Required: No

 ** DBInstanceClass **   
The compute and memory capacity of the Amazon RDS DB instance, for example db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.  
Default: The same DB instance class as the original DB instance.  
Type: String  
Required: No

 ** DBName **   
The database name for the restored DB instance.  
This parameter doesn't apply to the following DB instances:  
+ RDS Custom
+ RDS for Db2
+ RDS for MariaDB
+ RDS for MySQL
Type: String  
Required: No

 ** DBParameterGroupName **   
The name of the DB parameter group to associate with this DB instance.  
If you do not specify a value for `DBParameterGroupName`, then the default `DBParameterGroup` for the specified DB engine is used.  
This setting doesn't apply to RDS Custom.  
Constraints:  
+ If supplied, must match the name of an existing DB parameter group.
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: No

 ** DBSubnetGroupName **   
The DB subnet group name to use for the new instance.  
Constraints:  
+ If supplied, must match the name of an existing DB subnet group.
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DedicatedLogVolume **   
Specifies whether to enable a dedicated log volume (DLV) for the DB instance.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to restore the DB instance in. Create the domain before running this command. Currently, you can create only the MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.  
This setting doesn't apply to RDS Custom.  
For more information, see [ Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide*.  
Type: String  
Required: No

 ** DomainAuthSecretArn **   
The ARN for the Secrets Manager secret with the credentials for the user joining the domain.  
Constraints:  
+ Can't be longer than 64 characters.
Example: `arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456`   
Type: String  
Required: No

 **DomainDnsIps.member.N**   
The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.  
Constraints:  
+ Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.
Example: `123.124.125.126,234.235.236.237`   
Type: Array of strings  
Required: No

 ** DomainFqdn **   
The fully qualified domain name (FQDN) of an Active Directory domain.  
Constraints:  
+ Can't be longer than 64 characters.
Example: `mymanagedADtest.mymanagedAD.mydomain`   
Type: String  
Required: No

 ** DomainIAMRoleName **   
The name of the IAM role to use when making API calls to the Directory Service.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** DomainOu **   
The Active Directory organizational unit for your DB instance to join.  
Constraints:  
+ Must be in the distinguished name format.
+ Can't be longer than 64 characters.
Example: `OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain`   
Type: String  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
The list of logs that the restored DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom.  
Type: Array of strings  
Required: No

 ** EnableCustomerOwnedIp **   
Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.  
A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.  
This setting doesn't apply to RDS Custom.  
For more information about RDS on Outposts, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.  
For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the * AWS Outposts User Guide*.  
Type: Boolean  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
This setting doesn't apply to RDS Custom.  
For more information about IAM database authentication, see [ IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*   
Type: Boolean  
Required: No

 ** Engine **   
The database engine to use for the new instance.  
This setting doesn't apply to RDS Custom.  
Valid Values:  
+  `db2-ae` 
+  `db2-ce` 
+  `db2-se` 
+  `mariadb` 
+  `mysql` 
+  `oracle-ee` 
+  `oracle-ee-cdb` 
+  `oracle-se2` 
+  `oracle-se2-cdb` 
+  `postgres` 
+  `sqlserver-ee` 
+  `sqlserver-se` 
+  `sqlserver-ex` 
+  `sqlserver-web` 
Default: The same as source  
Constraints:  
+ Must be compatible with the engine of the source.
Type: String  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this DB instance.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, RDS automatically upgrades your restored DB instance to a higher engine version, if the major engine version is past its end of standard support date.
You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide*.  
This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the life cycle type is managed by the DB cluster.  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance.  
This setting doesn't apply to SQL Server.  
Constraints:  
+ Must be an integer greater than 1000.
Type: Integer  
Required: No

 ** LicenseModel **   
The license model information for the restored DB instance.  
License models for RDS for Db2 require additional configuration. The bring your own license (BYOL) model requires a custom parameter group and an AWS License Manager self-managed license. The Db2 license through AWS Marketplace model requires an AWS Marketplace subscription. For more information, see [Amazon RDS for Db2 licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide*.
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Valid Values:  
+ RDS for Db2 - `bring-your-own-license | marketplace-license` 
+ RDS for MariaDB - `general-public-license` 
+ RDS for Microsoft SQL Server - `license-included | bring-your-own-media` 
+ RDS for MySQL - `general-public-license` 
+ RDS for Oracle - `bring-your-own-license | license-included` 
+ RDS for PostgreSQL - `postgresql-license` 
Default: Same as the source.  
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager in the restored DB instance.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide*.  
Constraints:  
+ Applies to RDS for Oracle only.
Type: Boolean  
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
This setting doesn't apply to RDS Custom.  
Type: Integer  
Required: No

 ** MultiAZ **   
Secifies whether the DB instance is a Multi-AZ deployment.  
This setting doesn't apply to RDS Custom.  
Constraints:  
+ You can't specify the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*   
Valid Values:  
+  `IPV4` 
+  `DUAL` 
Type: String  
Required: No

 ** OptionGroupName **   
The name of the option group to use for the restored DB instance.  
Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance after it is associated with a DB instance  
This setting doesn't apply to RDS Custom.  
Type: String  
Required: No

 ** Port **   
The port number on which the database accepts connections.  
Default: The same port as the original DB instance.  
Constraints:  
+ The value must be `1150-65535`.
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` parameter. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information, see [Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide*.  
This setting doesn't apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster. For more information, see `ModifyDBCluster`.  
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 **ProcessorFeatures.ProcessorFeature.N**   
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.  
This setting doesn't apply to RDS Custom.  
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB instance is publicly accessible.  
When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBInstance](API_CreateDBInstance.md).  
Type: Boolean  
Required: No

 ** RestoreTime **   
The date and time to restore from.  
Constraints:  
+ Must be a time in Universal Coordinated Time (UTC) format.
+ Must be before the latest restorable time for the DB instance.
+ Can't be specified if the `UseLatestRestorableTime` parameter is enabled.
Example: `2009-09-07T23:45:00Z`   
Type: Timestamp  
Required: No

 ** SourceDBInstanceAutomatedBackupsArn **   
The Amazon Resource Name (ARN) of the replicated automated backups from which to restore, for example, `arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`.  
This setting doesn't apply to RDS Custom.  
Type: String  
Required: No

 ** SourceDBInstanceIdentifier **   
The identifier of the source DB instance from which to restore.  
Constraints:  
+ Must match the identifier of an existing DB instance.
Type: String  
Required: No

 ** SourceDbiResourceId **   
The resource ID of the source DB instance from which to restore.  
Type: String  
Required: No

 ** StorageThroughput **   
The storage throughput value for the DB instance.  
This setting doesn't apply to RDS Custom or Amazon Aurora.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type to associate with the DB instance.  
Valid Values: `gp2 | gp3 | io1 | io2 | standard`   
Default: `io1`, if the `Iops` parameter is specified. Otherwise, `gp3`.  
Constraints:  
+ If you specify `io1`, `io2`, or `gp3`, you must also include a value for the `Iops` parameter.
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB instance.  
Valid Values:   
+  `auto-backup` - The DB instance's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

 ** TdeCredentialArn **   
The ARN from the key store with which to associate the instance for TDE encryption.  
This setting doesn't apply to RDS Custom.  
Type: String  
Required: No

 ** TdeCredentialPassword **   
The password for the given ARN from the key store in order to access the device.  
This setting doesn't apply to RDS Custom.  
Type: String  
Required: No

 ** UseDefaultProcessorFeatures **   
Specifies whether the DB instance class of the DB instance uses its default processor features.  
This setting doesn't apply to RDS Custom.  
Type: Boolean  
Required: No

 ** UseLatestRestorableTime **   
Specifies whether the DB instance is restored from the latest backup time. By default, the DB instance isn't restored from the latest backup time.  
Constraints:  
+ Can't be specified if the `RestoreTime` parameter is provided.
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of EC2 VPC security groups to associate with this DB instance.  
Default: The default EC2 VPC security group for the DB subnet group's VPC.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_RestoreDBInstanceToPointInTime_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_RestoreDBInstanceToPointInTime_Errors"></a>

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

 ** DBInstanceAutomatedBackupNotFound **   
No automated backup for this DB instance was found.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

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

 ** DomainNotFoundFault **   
 `Domain` doesn't refer to an existing Active Directory domain.  
HTTP Status Code: 404

 ** InstanceQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB instances.  
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidRestoreFault **   
Cannot restore from VPC backup to non-VPC DB instance.  
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

 ** PointInTimeRestoreNotEnabled **   
 `SourceDBInstanceIdentifier` refers to a DB instance with `BackupRetentionPeriod` equal to 0.  
HTTP Status Code: 400

 ** ProvisionedIopsNotAvailableInAZFault **   
Provisioned IOPS not available in the specified Availability Zone.  
HTTP Status Code: 400

 ** StorageQuotaExceeded **   
The request would result in the user exceeding the allowed amount of storage available across all DB instances.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

 ** TenantDatabaseQuotaExceeded **   
You attempted to create more tenant databases than are permitted in your AWS account.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_RestoreDBInstanceToPointInTime_Examples"></a>

### Example
<a name="API_RestoreDBInstanceToPointInTime_Example_1"></a>

This example illustrates one usage of RestoreDBInstanceToPointInTime.

#### Sample Request
<a name="API_RestoreDBInstanceToPointInTime_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=RestoreDBInstanceToPointInTime
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBInstanceIdentifier=mysqldb
   &TargetDBInstanceIdentifier=mysqldb-pitr
   &UseLatestRestorableTime=true
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T233051Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=087a8eb41cb1ab0fc9ec1575f23e73757ffc6a1e42d7d2b30b9cc0be988cff97
```

#### Sample Response
<a name="API_RestoreDBInstanceToPointInTime_Example_1_Response"></a>

```
<RestoreDBInstanceToPointInTimeResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RestoreDBInstanceToPointInTimeResult>
    <DBInstance>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
      <DBInstanceStatus>creating</DBInstanceStatus>
      <MultiAZ>false</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>mysqldb-pitr</DBInstanceIdentifier>
      <PreferredBackupWindow>08:14-08:44</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:04:50-fri:05:20</PreferredMaintenanceWindow>
      <ReadReplicaDBInstanceIdentifiers/>
      <Engine>mysql</Engine>
      <PendingModifiedValues/>
      <LicenseModel>general-public-license</LicenseModel>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
      <EngineVersion>5.6.13</EngineVersion>
      <OptionGroupMemberships>
        <OptionGroupMembership>
          <OptionGroupName>default:mysql-5-6</OptionGroupName>
          <Status>pending-apply</Status>
        </OptionGroupMembership>
      </OptionGroupMemberships>
      <PubliclyAccessible>true</PubliclyAccessible>
      <DBSecurityGroups>
        <DBSecurityGroup>
          <Status>active</Status>
          <DBSecurityGroupName>default</DBSecurityGroupName>
        </DBSecurityGroup>
      </DBSecurityGroups>
      <DBName>mysqldb</DBName>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
      <DBInstanceClass>db.m1.medium</DBInstanceClass>
    </DBInstance>
  </RestoreDBInstanceToPointInTimeResult>
  <ResponseMetadata>
    <RequestId>13447c70-be2c-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</RestoreDBInstanceToPointInTimeResponse>
```

## See Also
<a name="API_RestoreDBInstanceToPointInTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RestoreDBInstanceToPointInTime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RestoreDBInstanceToPointInTime) 