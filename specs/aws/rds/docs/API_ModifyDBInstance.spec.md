---
id: "@specs/aws/rds/docs/API_ModifyDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBInstance
<a name="API_ModifyDBInstance"></a>

Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call `DescribeValidDBInstanceModifications` before you call `ModifyDBInstance`.

## Request Parameters
<a name="API_ModifyDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The identifier of DB instance to modify. This value is stored as a lowercase string.  
Constraints:  
+ Must match the identifier of an existing DB instance.
Type: String  
Required: Yes

 **AdditionalStorageVolumes.member.N**   
A list of additional storage volumes to modify or delete for the DB instance. You can create up to 3 additional storage volumes. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.  
Type: Array of [ModifyAdditionalStorageVolume](API_ModifyAdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The new amount of storage in gibibytes (GiB) to allocate for the DB instance.  
For RDS for Db2, MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL, the value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.  
For the valid values for allocated storage for each engine, see `CreateDBInstance`.  
Constraints:  
+ When you increase the allocated storage for a DB instance that uses Provisioned IOPS (`gp3`, `io1`, or `io2` storage type), you must also specify the `Iops` parameter. You can use the current value for `Iops`.
Type: Integer  
Required: No

 ** AllowMajorVersionUpgrade **   
Specifies whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.  
This setting doesn't apply to RDS Custom DB instances.  
Constraints:  
+ Major version upgrades must be allowed when specifying a value for the `EngineVersion` parameter that's a different major version than the DB instance's current version.
Type: Boolean  
Required: No

 ** ApplyImmediately **   
Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB instance. By default, this parameter is disabled.  
If this parameter is disabled, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to [RebootDBInstance](API_RebootDBInstance.md), or the next failure reboot. Review the table of parameters in [Modifying a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) in the *Amazon RDS User Guide* to see the impact of enabling or disabling `ApplyImmediately` for each modified parameter and to determine when the changes are applied.  
Type: Boolean  
Required: No

 ** AutomationMode **   
The automation mode of the RDS Custom DB instance. If `full`, the DB instance automates monitoring and instance recovery. If `all paused`, the instance pauses automation for the duration set by `ResumeFullAutomationModeMinutes`.  
Type: String  
Valid Values: `full | all-paused`   
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window. An outage occurs when all the following conditions are met:  
+ The automatic upgrade is enabled for the maintenance window.
+ A newer minor version is available.
+ RDS has enabled automatic patching for the engine version.
If any of the preceding conditions isn't met, Amazon RDS applies the change as soon as possible and doesn't cause an outage.  
For an RDS Custom DB instance, don't enable this setting. Otherwise, the operation returns an error.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Length Constraints: Minimum length of 43. Maximum length of 350.  
Pattern: `arn:aws[a-z-]*:backup:[-a-z0-9]+:[0-9]{12}:[-a-z]+:([a-z0-9\-]+:)?[a-z][a-z0-9\-]{0,255}`   
Required: No

 ** BackupRetentionPeriod **   
The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.  
Enabling and disabling backups can result in a brief I/O suspension that lasts from a few seconds to a few minutes, depending on the size and class of your DB instance.
These changes are applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request. If you change the parameter from one non-zero value to another non-zero value, the change is asynchronously applied as soon as possible.  
This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster. For more information, see `ModifyDBCluster`.  
Default: Uses existing setting  
Constraints:  
+ Must be a value from 0 to 35.
+ Can't be set to 0 if the DB instance is a source to read replicas.
+ Can't be set to 0 for an RDS Custom for Oracle DB instance.
Type: Integer  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the DB instance's server certificate.  
This setting doesn't apply to RDS Custom DB instances.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** CertificateRotationRestart **   
Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.  
By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.  
Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.
If you are using SSL/TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL/TLS certificate:  
+ For more information about rotating your SSL/TLS certificate for RDS DB engines, see [ Rotating Your SSL/TLS Certificate.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon RDS User Guide.* 
+ For more information about rotating your SSL/TLS certificate for Aurora DB engines, see [ Rotating Your SSL/TLS Certificate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon Aurora User Guide*.
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** CloudwatchLogsExportConfiguration **   
The log types to be enabled for export to CloudWatch Logs for a specific DB instance.  
A change to the `CloudwatchLogsExportConfiguration` parameter is always applied to the DB instance immediately. Therefore, the `ApplyImmediately` parameter has no effect.  
This setting doesn't apply to RDS Custom DB instances.  
The following values are valid for each DB engine:  
+ Aurora MySQL - `audit | error | general | slowquery | iam-db-auth-error` 
+ Aurora PostgreSQL - `postgresql | iam-db-auth-error` 
+ RDS for MySQL - `error | general | slowquery | iam-db-auth-error` 
+ RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error` 
For more information about exporting CloudWatch Logs for Amazon RDS, see [ Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
For more information about exporting CloudWatch Logs for Amazon Aurora, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.  
Type: [CloudwatchLogsExportConfiguration](API_CloudwatchLogsExportConfiguration.md) object  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags aren't copied.  
This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see `ModifyDBCluster`.  
Type: Boolean  
Required: No

 ** DatabaseInsightsMode **   
Specifies the mode of Database Insights to enable for the DB instance.  
Aurora DB instances inherit this value from the DB cluster, so you can't change this value.
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBInstanceClass **   
The new compute and memory capacity of the DB instance, for example `db.m4.large`. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide*. For RDS Custom, see [DB instance class support for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.instances) and [ DB instance class support for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html#custom-reqs-limits.instancesMS).  
If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless you specify `ApplyImmediately` in your request.   
Default: Uses existing setting  
Constraints:  
+ If you are modifying the DB instance class and upgrading the engine version at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.
Type: String  
Required: No

 ** DBParameterGroupName **   
The name of the DB parameter group to apply to the DB instance.  
Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. In this case, the DB instance isn't rebooted automatically, and the parameter changes aren't applied during the next maintenance window. However, if you modify dynamic parameters in the newly associated DB parameter group, these changes are applied immediately without a reboot.  
This setting doesn't apply to RDS Custom DB instances.  
Default: Uses existing setting  
Constraints:  
+ Must be in the same DB parameter group family as the DB instance.
Type: String  
Required: No

 ** DBPortNumber **   
The port number on which the database accepts connections.  
The value of the `DBPortNumber` parameter must not match any of the port values specified for options in the option group for the DB instance.  
If you change the `DBPortNumber` value, your database restarts regardless of the value of the `ApplyImmediately` parameter.  
This setting doesn't apply to RDS Custom DB instances.  
Valid Values: `1150-65535`   
Default:  
+ Amazon Aurora - `3306` 
+ RDS for Db2 - `50000` 
+ RDS for MariaDB - `3306` 
+ RDS for Microsoft SQL Server - `1433` 
+ RDS for MySQL - `3306` 
+ RDS for Oracle - `1521` 
+ RDS for PostgreSQL - `5432` 
Constraints:  
+ For RDS for Microsoft SQL Server, the value can't be `1234`, `1434`, `3260`, `3343`, `3389`, `47001`, or `49152-49156`.
Type: Integer  
Required: No

 **DBSecurityGroups.DBSecurityGroupName.N**   
A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible.  
This setting doesn't apply to RDS Custom DB instances.  
Constraints:  
+ If supplied, must match existing DB security groups.
Type: Array of strings  
Required: No

 ** DBSubnetGroupName **   
The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. If your DB instance isn't in a VPC, you can also use this parameter to move your DB instance into a VPC. For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Non-VPC2VPC) in the *Amazon RDS User Guide*.  
Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you enable `ApplyImmediately`.  
This setting doesn't apply to RDS Custom DB instances.  
Constraints:  
+ If supplied, must match existing DB subnet group.
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DedicatedLogVolume **   
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
This setting doesn't apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see `ModifyDBCluster`. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.  
Type: Boolean  
Required: No

 ** DisableDomain **   
Specifies whether to remove the DB instance from the Active Directory domain.  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to move the DB instance to. Specify `none` to remove the instance from its current domain. You must create the domain before this operation. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.  
For more information, see [ Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** DomainAuthSecretArn **   
The ARN for the Secrets Manager secret with the credentials for the user joining the domain.  
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
Example: `OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain`   
Type: String  
Required: No

 ** EnableCustomerOwnedIp **   
Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.  
A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.  
For more information about RDS on Outposts, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.  
For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the * AWS Outposts User Guide*.  
Type: Boolean  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
This setting doesn't apply to Amazon Aurora. Mapping AWS IAM accounts to database accounts is managed by the DB cluster.  
For more information about IAM database authentication, see [ IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*   
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to enable Performance Insights for the DB instance.  
For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** Engine **   
The target Oracle DB engine when you convert a non-CDB to a CDB. This intermediate step is necessary to upgrade an Oracle Database 19c non-CDB to an Oracle Database 21c CDB.  
Note the following requirements:  
+ Make sure that you specify `oracle-ee-cdb` or `oracle-se2-cdb`.
+ Make sure that your DB engine runs Oracle Database 19c with an April 2021 or later RU.
Note the following limitations:  
+ You can't convert a CDB to a non-CDB.
+ You can't convert a replica database.
+ You can't convert a non-CDB to a CDB and upgrade the engine version in the same command.
+ You can't convert the existing custom parameter or option group when it has options or parameters that are permanent or persistent. In this situation, the DB instance reverts to the default option and parameter group. To avoid reverting to the default, specify a new parameter group with `--db-parameter-group-name` and a new option group with `--option-group-name`.
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.  
For major version upgrades, if a nondefault DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.  
If you specify only a major version, Amazon RDS updates the DB instance to the default minor version if the current minor version is lower. For information about valid engine versions, see `CreateDBInstance`, or call `DescribeDBEngineVersions`.  
If the instance that you're modifying is acting as a read replica, the engine version that you specify must be the same or higher than the version that the source DB instance or cluster is running.  
In RDS Custom for Oracle, this parameter is supported for read replicas only if they are in the `PATCH_DB_FAILURE` lifecycle.  
Constraints:  
+ If you are upgrading the engine version and modifying the DB instance class at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.
Type: String  
Required: No

 ** Iops **   
The new Provisioned IOPS (I/O operations per second) value for the RDS instance.  
Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request. If you are migrating from Provisioned IOPS to standard storage, set this value to 0. The DB instance will require a reboot for the change in storage type to take effect.  
If you choose to migrate your DB instance from using standard storage to Provisioned IOPS (io1), or from Provisioned IOPS to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.  
  
Constraints:  
+ For RDS for MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL - The value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
+ When you increase the Provisioned IOPS, you must also specify the `AllocatedStorage` parameter. You can use the current value for `AllocatedStorage`.
Default: Uses existing setting  
Type: Integer  
Required: No

 ** LicenseModel **   
The license model for the DB instance.  
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Valid Values:  
+ RDS for Db2 - `bring-your-own-license` 
+ RDS for MariaDB - `general-public-license` 
+ RDS for Microsoft SQL Server - `license-included | bring-your-own-media` 
+ RDS for MySQL - `general-public-license` 
+ RDS for Oracle - `bring-your-own-license | license-included` 
+ RDS for PostgreSQL - `postgresql-license` 
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
If the DB instance doesn't manage the master user password with AWS Secrets Manager, you can turn on this management. In this case, you can't specify `MasterUserPassword`.  
If the DB instance already manages the master user password with AWS Secrets Manager, and you specify that the master user password is not managed with AWS Secrets Manager, then you must specify `MasterUserPassword`. In this case, Amazon RDS deletes the secret and uses the new password for the master user specified by `MasterUserPassword`.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
+ Can't specify for RDS for Oracle CDB instances in the multi-tenant configuration. Use `ModifyTenantDatabase` instead.
+ Can't specify the parameters `ManageMasterUserPassword` and `MultiTenant` in the same operation.
Type: Boolean  
Required: No

 ** MasterUserAuthenticationType **   
Specifies the authentication type for the master user. With IAM master user authentication, you can change the master DB user to use IAM database authentication.  
You can specify one of the following values:  
+  `password` - Use standard database authentication with a password.
+  `iam-db-auth` - Use IAM database authentication for the master user.
This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.  
Type: String  
Valid Values: `password | iam-db-auth`   
Required: No

 ** MasterUserPassword **   
The new password for the master user.  
Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the `MasterUserPassword` element exists in the `PendingModifiedValues` element of the operation response.  
Amazon RDS API operations never return the password, so this operation provides a way to regain access to a primary instance user if the password is lost. This includes restoring privileges that might have been accidentally revoked.
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora

  The password for the master user is managed by the DB cluster. For more information, see `ModifyDBCluster`.
+ RDS Custom
+ RDS for Oracle CDBs in the multi-tenant configuration

  Specify the master password in `ModifyTenantDatabase` instead.
Default: Uses existing setting  
Constraints:  
+ Can't be specified if `ManageMasterUserPassword` is turned on.
+ Can include any printable ASCII character except "/", """, or "@". For RDS for Oracle, can't include the "&" (ampersand) or the "'" (single quotes) character.
Length Constraints:  
+ RDS for Db2 - Must contain from 8 to 255 characters.
+ RDS for MariaDB - Must contain from 8 to 41 characters.
+ RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.
+ RDS for MySQL - Must contain from 8 to 41 characters.
+ RDS for Oracle - Must contain from 8 to 30 characters.
+ RDS for PostgreSQL - Must contain from 8 to 128 characters.
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if both of the following conditions are met:  
+ The DB instance doesn't manage the master user password in AWS Secrets Manager.

  If the DB instance already manages the master user password in AWS Secrets Manager, you can't change the KMS key used to encrypt the secret.
+ You are turning on `ManageMasterUserPassword` to manage the master user password in AWS Secrets Manager.

  If you are turning on `ManageMasterUserPassword` and don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.  
For more information about this setting, including limitations that apply to it, see [ Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Integer  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify `0`.  
If `MonitoringRoleArn` is specified, set `MonitoringInterval` to a value other than `0`.  
This setting doesn't apply to RDS Custom DB instances.  
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [To create an IAM role for Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole) in the *Amazon RDS User Guide.*   
If `MonitoringInterval` is set to a value other than `0`, supply a `MonitoringRoleArn` value.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** MultiAZ **   
Specifies whether the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage. The change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** MultiTenant **   
Specifies whether the to convert your DB instance from the single-tenant conﬁguration to the multi-tenant conﬁguration. This parameter is supported only for RDS for Oracle CDB instances.  
During the conversion, RDS creates an initial tenant database and associates the DB name, master user name, character set, and national character set metadata with this database. The tags associated with the instance also propagate to the initial tenant database. You can add more tenant databases to your DB instance by using the `CreateTenantDatabase` operation.  
The conversion to the multi-tenant configuration is permanent and irreversible, so you can't later convert back to the single-tenant configuration. When you specify this parameter, you must also specify `ApplyImmediately`.
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*   
Valid Values: `IPV4 | DUAL`   
Type: String  
Required: No

 ** NewDBInstanceIdentifier **   
The new identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot occurs immediately if you enable `ApplyImmediately`, or will occur during the next maintenance window if you disable `ApplyImmediately`. This value is stored as a lowercase string.  
This setting doesn't apply to RDS Custom DB instances.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`   
Type: String  
Required: No

 ** OptionGroupName **   
The option group to associate the DB instance with.  
Changing this parameter doesn't result in an outage, with one exception. If the parameter change results in an option group that enables OEM, it can cause a brief period, lasting less than a second, during which new connections are rejected but existing connections aren't interrupted.  
The change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.  
Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance after it is associated with a DB instance.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you don't specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data.  
This setting doesn't apply to RDS Custom DB instances.  
Valid Values:  
+  `7` 
+  *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731` 
Default: `7` days  
If you specify a retention period that isn't valid, such as `94`, Amazon RDS returns an error.  
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

 ** PreferredMaintenanceWindow **   
The weekly time range during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter causes a reboot of the DB instance. If you change this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.  
For more information, see [Amazon RDS Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) in the *Amazon RDS User Guide.*   
Default: Uses existing setting  
Constraints:  
+ Must be in the format `ddd:hh24:mi-ddd:hh24:mi`.
+ The day values must be `mon | tue | wed | thu | fri | sat | sun`. 
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred backup window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 **ProcessorFeatures.ProcessorFeature.N**   
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects  
Required: No

 ** PromotionTier **   
The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [ Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Default: `1`   
Valid Values: `0 - 15`   
Type: Integer  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB instance is publicly accessible.  
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB instance doesn't permit it.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
 `PubliclyAccessible` only applies to DB instances in a VPC. The DB instance must be part of a public subnet and `PubliclyAccessible` must be enabled for it to be publicly accessible.  
Changes to the `PubliclyAccessible` parameter are applied immediately regardless of the value of the `ApplyImmediately` parameter.  
Type: Boolean  
Required: No

 ** ReplicaMode **   
The open mode of a replica database.  
This parameter is only supported for Db2 DB instances and Oracle DB instances.    
 **Db2**   
Standby DB replicas are included in Db2 Advanced Edition (AE), Db2 Community Edition (CE), and Db2 Standard Edition (SE). The main use case for standby replicas is cross-Region disaster recovery. Because it doesn't accept user connections, a standby replica can't serve a read-only workload.  
You can create a combination of standby and read-only DB replicas for the same primary DB instance. For more information, see [Working with replicas for Amazon RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html) in the *Amazon RDS User Guide*.  
To create standby DB replicas for RDS for Db2, set this parameter to `mounted`.  
 **Oracle**   
Mounted DB replicas are included in Oracle Database Enterprise Edition. The main use case for mounted replicas is cross-Region disaster recovery. The primary database doesn't use Active Data Guard to transmit information to the mounted replica. Because it doesn't accept user connections, a mounted replica can't serve a read-only workload.  
You can create a combination of mounted and read-only DB replicas for the same primary DB instance. For more information, see [Working with read replicas for Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide*.  
For RDS Custom, you must specify this parameter and set it to `mounted`. The value won't be set by default. After replica creation, you can manage the open mode manually.
Type: String  
Valid Values: `open-read-only | mounted`   
Required: No

 ** ResumeFullAutomationModeMinutes **   
The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation.  
Default: `60`   
Constraints:  
+ Must be at least 60.
+ Must be no more than 1,440.
Type: Integer  
Required: No

 ** RotateMasterUserPassword **   
Specifies whether to rotate the secret managed by AWS Secrets Manager for the master user password.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB instance. The secret value contains the updated password.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ You must apply the change immediately when rotating the master user password.
Type: Boolean  
Required: No

 ** StorageThroughput **   
The storage throughput value for the DB instance.  
This setting applies only to the `gp3` storage type.  
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type to associate with the DB instance.  
If you specify `io1`, `io2`, or `gp3` you must also include a value for the `Iops` parameter.  
If you choose to migrate your DB instance from using standard storage to gp2 (General Purpose SSD), gp3, or Provisioned IOPS (io1), or from these storage types to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.  
Valid Values: `gp2 | gp3 | io1 | io2 | standard`   
Default: `io1`, if the `Iops` parameter is specified. Otherwise, `gp2`.  
Type: String  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB instance.  
Valid Values:   
+  `auto-backup` - The DB instance's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

 ** TdeCredentialArn **   
The ARN from the key store with which to associate the instance for TDE encryption.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** TdeCredentialPassword **   
The password for the given ARN from the key store in order to access the device.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** UseDefaultProcessorFeatures **   
Specifies whether the DB instance class of the DB instance uses its default processor features.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of Amazon EC2 VPC security groups to associate with this DB instance. This change is asynchronously applied as soon as possible.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see `ModifyDBCluster`.)
+ RDS Custom
Constraints:  
+ If supplied, must match existing VPC security group IDs.
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_ModifyDBInstance_Errors"></a>

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

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

 ** DBUpgradeDependencyFailure **   
The DB upgrade failed because a resource the DB depends on can't be modified.  
HTTP Status Code: 400

 ** DomainNotFoundFault **   
 `Domain` doesn't refer to an existing Active Directory domain.  
HTTP Status Code: 404

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBSecurityGroupState **   
The state of the DB security group doesn't allow deletion.  
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

 ** TenantDatabaseQuotaExceeded **   
You attempted to create more tenant databases than are permitted in your AWS account.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBInstance_Examples"></a>

### Example
<a name="API_ModifyDBInstance_Example_1"></a>

This example illustrates one usage of ModifyDBInstance.

#### Sample Request
<a name="API_ModifyDBInstance_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=ModifyDBInstance
   &AllocatedStorage=20
   &DBInstanceIdentifier=myawsuser-dbi04
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T192732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=1dc9dd716f4855e9bdf188c70f1cf9f6251b070b68b81103b59ec70c3e7854b3
```

#### Sample Response
<a name="API_ModifyDBInstance_Example_1_Response"></a>

```
<ModifyDBInstanceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBInstanceResult>
    <DBInstance>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
      <DBInstanceStatus>available</DBInstanceStatus>
      <MultiAZ>true</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>myawsuser-dbi04</DBInstanceIdentifier>
      <PreferredBackupWindow>10:03-10:33</PreferredBackupWindow>
      <PreferredMaintenanceWindow>wed:03:32-wed:04:02</PreferredMaintenanceWindow>
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <ReadReplicaDBInstanceIdentifiers/>
      <LatestRestorableTime>2014-04-25T19:25:00Z</LatestRestorableTime>
      <Engine>mysql</Engine>
      <PendingModifiedValues>
        <AllocatedStorage>20</AllocatedStorage>
      </PendingModifiedValues>
      <LicenseModel>general-public-license</LicenseModel>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
      <Endpoint>
        <Port>3306</Port>
        <Address>myawsuser-dbi04.cg037hpkuyjt.us-east-1.rds.amazonaws.com</Address>
      </Endpoint>
      <EngineVersion>5.6.13</EngineVersion>
      <SecondaryAvailabilityZone>us-east-1b</SecondaryAvailabilityZone>
      <OptionGroupMemberships>
        <OptionGroupMembership>
          <OptionGroupName>default:mysql-5-6</OptionGroupName>
          <Status>in-sync</Status>
        </OptionGroupMembership>
      </OptionGroupMemberships>
      <PubliclyAccessible>true</PubliclyAccessible>
      <DBSecurityGroups>
        <DBSecurityGroup>
          <Status>active</Status>
          <DBSecurityGroupName>default</DBSecurityGroupName>
        </DBSecurityGroup>
      </DBSecurityGroups>
      <DBName>myawsuser_db04</DBName>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <InstanceCreateTime>2014-04-25T18:07:51.508Z</InstanceCreateTime>
      <AllocatedStorage>15</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
      <DBInstanceClass>db.m1.small</DBInstanceClass>
    </DBInstance>
  </ModifyDBInstanceResult>
  <ResponseMetadata>
    <RequestId>f643f1ac-bbfe-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</ModifyDBInstanceResponse>
```

## See Also
<a name="API_ModifyDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBInstance) 