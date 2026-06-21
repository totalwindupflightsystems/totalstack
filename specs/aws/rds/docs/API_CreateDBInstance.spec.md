---
id: "@specs/aws/rds/docs/API_CreateDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBInstance
<a name="API_CreateDBInstance"></a>

Creates a new DB instance.

The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster. For an Aurora DB cluster, you can call this operation multiple times to add more than one DB instance to the cluster.

For more information about creating an RDS DB instance, see [ Creating an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.

For more information about creating a DB instance in an Aurora DB cluster, see [ Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_CreateDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceClass **   
The compute and memory capacity of the DB instance, for example `db.m5.large`. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: Yes

 ** DBInstanceIdentifier **   
The identifier for this DB instance. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`   
Type: String  
Required: Yes

 ** Engine **   
The database engine to use for this DB instance.  
Not every database engine is available in every AWS Region.  
Valid Values:  
+  `aurora-mysql` (for Aurora MySQL DB instances)
+  `aurora-postgresql` (for Aurora PostgreSQL DB instances)
+  `custom-oracle-ee` (for RDS Custom for Oracle DB instances)
+  `custom-oracle-ee-cdb` (for RDS Custom for Oracle DB instances)
+  `custom-oracle-se2` (for RDS Custom for Oracle DB instances)
+  `custom-oracle-se2-cdb` (for RDS Custom for Oracle DB instances)
+  `custom-sqlserver-ee` (for RDS Custom for SQL Server DB instances)
+  `custom-sqlserver-se` (for RDS Custom for SQL Server DB instances)
+  `custom-sqlserver-web` (for RDS Custom for SQL Server DB instances)
+  `custom-sqlserver-dev` (for RDS Custom for SQL Server DB instances)
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
+  `sqlserver-dev-ee` 
+  `sqlserver-ee` 
+  `sqlserver-se` 
+  `sqlserver-ex` 
+  `sqlserver-web` 
Type: String  
Required: Yes

 **AdditionalStorageVolumes.member.N**   
A list of additional storage volumes to create for the DB instance. You can create up to three additional storage volumes using the names `rdsdbdata2`, `rdsdbdata3`, and `rdsdbdata4`. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.  
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The amount of storage in gibibytes (GiB) to allocate for the DB instance.  
This setting doesn't apply to Amazon Aurora DB instances. Aurora cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in an Aurora cluster volume.    
 **Amazon RDS Custom**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.  
 **RDS for Db2**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp3): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.  
 **RDS for MariaDB**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.  
 **RDS for MySQL**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.  
 **RDS for Oracle**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 10 to 3072.  
 **RDS for PostgreSQL**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
+ Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
+ Magnetic storage (standard): Must be an integer from 5 to 3072.  
 **RDS for SQL Server**   
Constraints to the amount of storage for each storage type are the following:  
+ General Purpose (SSD) storage (gp2, gp3):
  + Enterprise and Standard editions: Must be an integer from 20 to 16384.
  + Web and Express editions: Must be an integer from 20 to 16384.
+ Provisioned IOPS storage (io1, io2):
  + Enterprise and Standard editions: Must be an integer from 100 to 16384.
  + Web and Express editions: Must be an integer from 100 to 16384.
+ Magnetic storage (standard):
  + Enterprise and Standard editions: Must be an integer from 20 to 1024.
  + Web and Express editions: Must be an integer from 20 to 1024.
Type: Integer  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.  
If you create an RDS Custom DB instance, you must set `AutoMinorVersionUpgrade` to `false`.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).  
For Amazon Aurora, each Aurora DB cluster hosts copies of its storage in three separate Availability Zones. Specify one of these Availability Zones. Aurora automatically chooses an appropriate Availability Zone if you don't specify one.  
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.  
Constraints:  
+ The `AvailabilityZone` parameter can't be specified if the DB instance is a Multi-AZ deployment.
+ The specified Availability Zone must be in the same AWS Region as the current endpoint.
Example: `us-east-1d`   
Type: String  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to `0` disables automated backups.  
This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster.  
Default: `1`   
Constraints:  
+ Must be a value from 0 to 35.
+ Can't be set to 0 if the DB instance is a source to read replicas.
+ Can't be set to 0 for an RDS Custom for Oracle DB instance.
Type: Integer  
Required: No

 ** BackupTarget **   
The location for storing automated backups and manual snapshots.  
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

 ** CharacterSetName **   
For supported engines, the character set (`CharacterSet`) to associate the DB instance with.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora - The character set is managed by the DB cluster. For more information, see `CreateDBCluster`.
+ RDS Custom - However, if you need to change the character set, you can change it on the database itself.
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.  
This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting.  
Type: Boolean  
Required: No

 ** CustomIamInstanceProfile **   
The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance.  
This setting is required for RDS Custom.  
Constraints:  
+ The profile must exist in your account.
+ The profile must have an IAM role that Amazon EC2 has permissions to assume.
+ The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom`.
For the list of permissions required for the IAM role, see [ Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.  
Type: String  
Required: No

 ** DatabaseInsightsMode **   
The mode of Database Insights to enable for the DB instance.  
Aurora DB instances inherit this value from the DB cluster, so you can't change this value.
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBClusterIdentifier **   
The identifier of the DB cluster that this DB instance will belong to.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** DBName **   
The meaning of this parameter differs according to the database engine you use.    
 **Amazon Aurora MySQL**   
The name of the database to create when the primary DB instance of the Aurora MySQL DB cluster is created. If this parameter isn't specified for an Aurora MySQL DB cluster, no database is created in the DB cluster.  
Constraints:  
+ Must contain 1 to 64 alphanumeric characters.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the database engine.  
 **Amazon Aurora PostgreSQL**   
The name of the database to create when the primary DB instance of the Aurora PostgreSQL DB cluster is created. A database named `postgres` is always created. If this parameter is specified, an additional database with this name is created.  
Constraints:  
+ It must contain 1 to 63 alphanumeric characters.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0 to 9).
+ Can't be a word reserved by the database engine.  
 **Amazon RDS Custom for Oracle**   
The Oracle System ID (SID) of the created RDS Custom DB instance. If you don't specify a value, the default value is `ORCL` for non-CDBs and `RDSCDB` for CDBs.  
Default: `ORCL`   
Constraints:  
+ Must contain 1 to 8 alphanumeric characters.
+ Must contain a letter.
+ Can't be a word reserved by the database engine.  
 **Amazon RDS Custom for SQL Server**   
Not applicable. Must be null.  
 **RDS for Db2**   
The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance. In some cases, we recommend that you don't add a database name. For more information, see [Additional considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-db-instance-prereqs.html#db2-prereqs-additional-considerations) in the *Amazon RDS User Guide*.  
Constraints:  
+ Must contain 1 to 64 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the specified database engine.  
 **RDS for MariaDB**   
The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.  
Constraints:  
+ Must contain 1 to 64 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the specified database engine.  
 **RDS for MySQL**   
The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.  
Constraints:  
+ Must contain 1 to 64 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the specified database engine.  
 **RDS for Oracle**   
The Oracle System ID (SID) of the created DB instance. If you don't specify a value, the default value is `ORCL`. You can't specify the string `null`, or any other reserved word, for `DBName`.  
Default: `ORCL`   
Constraints:  
+ Can't be longer than 8 characters.  
 **RDS for PostgreSQL**   
The name of the database to create when the DB instance is created. A database named `postgres` is always created. If this parameter is specified, an additional database with this name is created.  
Constraints:  
+ Must contain 1 to 63 letters, numbers, or underscores.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
+ Can't be a word reserved by the specified database engine.  
 **RDS for SQL Server**   
Not applicable. Must be null.
Type: String  
Required: No

 ** DBParameterGroupName **   
The name of the DB parameter group to associate with this DB instance. If you don't specify a value, then Amazon RDS uses the default DB parameter group for the specified DB engine and version.  
This setting doesn't apply to RDS Custom DB instances.  
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: No

 **DBSecurityGroups.DBSecurityGroupName.N**   
A list of DB security groups to associate with this DB instance.  
This setting applies to the legacy EC2-Classic platform, which is no longer used to create new DB instances. Use the `VpcSecurityGroupIds` setting instead.  
Type: Array of strings  
Required: No

 ** DBSubnetGroupName **   
A DB subnet group to associate with this DB instance.  
Constraints:  
+ Must match the name of an existing DB subnet group.
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DBSystemId **   
The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. In this context, the term "Oracle database instance" refers exclusively to the system global area (SGA) and Oracle background processes. If you don't specify a SID, the value defaults to `RDSCDB`. The Oracle SID is also the name of your CDB.  
Type: String  
Required: No

 ** DedicatedLogVolume **   
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
This setting doesn't apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see `CreateDBCluster`. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to create the DB instance in. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.  
For more information, see [ Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (The domain is managed by the DB cluster.)
+ RDS Custom
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
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (The domain is managed by the DB cluster.)
+ RDS Custom
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
The list of log types to enable for exporting to CloudWatch Logs. For more information, see [ Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (CloudWatch Logs exports are managed by the DB cluster.)
+ RDS Custom
The following values are valid for each DB engine:  
+ RDS for Db2 - `diag.log | notify.log | iam-db-auth-error` 
+ RDS for MariaDB - `audit | error | general | slowquery | iam-db-auth-error` 
+ RDS for Microsoft SQL Server - `agent | error` 
+ RDS for MySQL - `audit | error | general | slowquery | iam-db-auth-error` 
+ RDS for Oracle - `alert | audit | listener | trace | oemagent` 
+ RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error` 
Type: Array of strings  
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
For more information, see [ IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (Mapping AWS IAM accounts to database accounts is managed by the DB cluster.)
+ RDS Custom
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to enable Performance Insights for the DB instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this DB instance.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, creating the DB instance will fail if the DB major version is past its end of standard support date.
This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the life cycle type is managed by the DB cluster.  
You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide*.  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine to use.  
This setting doesn't apply to Amazon Aurora DB instances. The version number of the database engine the DB instance uses is managed by the DB cluster.  
For a list of valid engine versions, use the `DescribeDBEngineVersions` operation.  
The following are the database engines and links to information about the major and minor versions that are available with Amazon RDS. Not every database engine is available for every AWS Region.    
 **Amazon RDS Custom for Oracle**   
A custom engine version (CEV) that you have previously created. This setting is required for RDS Custom for Oracle. The CEV name has the following format: 19.*customized\_string*. A valid CEV name is `19.my_cev1`. For more information, see [ Creating an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html#custom-creating.create) in the *Amazon RDS User Guide*.  
 **Amazon RDS Custom for SQL Server**   
See [RDS Custom for SQL Server general requirements](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html) in the *Amazon RDS User Guide*.  
 **RDS for Db2**   
For information, see [Db2 on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html#Db2.Concepts.VersionMgmt) in the *Amazon RDS User Guide*.  
 **RDS for MariaDB**   
For information, see [MariaDB on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt) in the *Amazon RDS User Guide*.  
 **RDS for Microsoft SQL Server**   
For information, see [Microsoft SQL Server versions on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) in the *Amazon RDS User Guide*.  
 **RDS for MySQL**   
For information, see [MySQL on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide*.  
 **RDS for Oracle**   
For information, see [Oracle Database Engine release notes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html) in the *Amazon RDS User Guide*.  
 **RDS for PostgreSQL**   
For information, see [Amazon RDS for PostgreSQL versions and extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts) in the *Amazon RDS User Guide*.
Type: String  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance. For information about valid IOPS values, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.  
Constraints:  
+ For RDS for Db2, MariaDB, MySQL, Oracle, and PostgreSQL - Must be a multiple between .5 and 50 of the storage amount for the DB instance.
+ For RDS for SQL Server - Must be a multiple between 1 and 50 of the storage amount for the DB instance.
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
This setting doesn't apply to Amazon Aurora DB instances. The AWS KMS key identifier is managed by the DB cluster. For more information, see `CreateDBCluster`.  
If `StorageEncrypted` is enabled, and you do not specify a value for the `KmsKeyId` parameter, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
For Amazon RDS Custom, a KMS key is required for DB instances. For most RDS engines, if you leave this parameter empty while enabling `StorageEncrypted`, the engine uses the default KMS key. However, RDS Custom doesn't use the default key when this parameter is empty. You must explicitly specify a key.  
Type: String  
Required: No

 ** LicenseModel **   
The license model information for this DB instance.  
License models for RDS for Db2 require additional configuration. The bring your own license (BYOL) model requires a custom parameter group and an AWS License Manager self-managed license. The Db2 license through AWS Marketplace model requires an AWS Marketplace subscription. For more information, see [Amazon RDS for Db2 licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide*.  
The default for RDS for Db2 is `bring-your-own-license`.
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Valid Values:  
+ RDS for Db2 - `bring-your-own-license | marketplace-license` 
+ RDS for MariaDB - `general-public-license` 
+ RDS for Microsoft SQL Server - `license-included | bring-your-own-media` 
+ RDS for MySQL - `general-public-license` 
+ RDS for Oracle - `bring-your-own-license | license-included` 
+ RDS for PostgreSQL - `postgresql-license` 
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
Type: Boolean  
Required: No

 ** MasterUserAuthenticationType **   
Specifies the authentication type for the master user. With IAM master user authentication, you can configure the master DB user with IAM database authentication when you create a DB instance.  
You can specify one of the following values:  
+  `password` - Use standard database authentication with a password.
+  `iam-db-auth` - Use IAM database authentication for the master user.
This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.  
Type: String  
Valid Values: `password | iam-db-auth`   
Required: No

 ** MasterUsername **   
The name for the master user.  
This setting doesn't apply to Amazon Aurora DB instances. The name for the master user is managed by the DB cluster.  
This setting is required for RDS DB instances.  
Constraints:  
+ Must be 1 to 16 letters, numbers, or underscores.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
Type: String  
Required: No

 ** MasterUserPassword **   
The password for the master user.  
This setting doesn't apply to Amazon Aurora DB instances. The password for the master user is managed by the DB cluster.  
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
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.  
For more information about this setting, including limitations that apply to it, see [ Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.  
This setting doesn't apply to the following DB instances:  
+ Amazon Aurora (Storage is managed by the DB cluster.)
+ RDS Custom
Type: Integer  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify `0`.  
If `MonitoringRoleArn` is specified, then you must set `MonitoringInterval` to a value other than `0`.  
This setting doesn't apply to RDS Custom DB instances.  
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [Setting Up and Enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide*.  
If `MonitoringInterval` is set to a value other than `0`, then you must supply a `MonitoringRoleArn` value.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** MultiAZ **   
Specifies whether the DB instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.  
This setting doesn't apply to Amazon Aurora because the DB instance Availability Zones (AZs) are managed by the DB cluster.  
Type: Boolean  
Required: No

 ** MultiTenant **   
Specifies whether to use the multi-tenant configuration or the single-tenant configuration (default). This parameter only applies to RDS for Oracle container database (CDB) engines.  
Note the following restrictions:   
+ The DB engine that you specify in the request must support the multi-tenant configuration. If you attempt to enable the multi-tenant configuration on a DB engine that doesn't support it, the request fails.
+ If you specify the multi-tenant configuration when you create your DB instance, you can't later modify this DB instance to use the single-tenant configuration.
Type: Boolean  
Required: No

 ** NcharCharacterSetName **   
The name of the NCHAR character set for the Oracle DB instance.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*   
Valid Values: `IPV4 | DUAL`   
Type: String  
Required: No

 ** OptionGroupName **   
The option group to associate the DB instance with.  
Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group. Also, that option group can't be removed from a DB instance after it is associated with a DB instance.  
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
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

 ** Port **   
The port number on which the database accepts connections.  
This setting doesn't apply to Aurora DB instances. The port number is managed by the cluster.  
Valid Values: `1150-65535`   
Default:  
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

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information, see [Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide*.  
This setting doesn't apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster.  
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The time range each week during which system maintenance can occur. For more information, see [Amazon RDS Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) in the *Amazon RDS User Guide.*   
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.  
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
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
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
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its domain name system (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is controlled by its security group settings.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
The default behavior when `PubliclyAccessible` is not specified depends on whether a `DBSubnetGroup` is specified.  
If `DBSubnetGroup` isn't specified, `PubliclyAccessible` defaults to `false` for Aurora instances and `true` for non-Aurora instances.  
If `DBSubnetGroup` is specified, `PubliclyAccessible` defaults to `false` unless the value of `DBSubnetGroup` is `default`, in which case `PubliclyAccessible` defaults to `true`.  
If `PubliclyAccessible` is true and the VPC that the `DBSubnetGroup` is in doesn't have an internet gateway attached to it, Amazon RDS returns an error.  
Type: Boolean  
Required: No

 ** StorageEncrypted **   
Specifes whether the DB instance is encrypted. By default, it isn't encrypted.  
For RDS Custom DB instances, either enable this setting or leave it unset. Otherwise, Amazon RDS reports an error.  
This setting doesn't apply to Amazon Aurora DB instances. The encryption for DB instances is managed by the DB cluster.  
Type: Boolean  
Required: No

 ** StorageThroughput **   
The storage throughput value, in mebibyte per second (MiBps), for the DB instance.  
This setting applies only to the `gp3` storage type.  
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type to associate with the DB instance.  
If you specify `io1`, `io2`, or `gp3`, you must also include a value for the `Iops` parameter.  
This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.  
Valid Values: `gp2 | gp3 | io1 | io2 | standard`   
Default: `io1`, if the `Iops` parameter is specified. Otherwise, `gp3`.  
Type: String  
Required: No

 **Tags.Tag.N**   
Tags to assign to the DB instance.  
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
This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.  
Type: String  
Required: No

 ** TdeCredentialPassword **   
The password for the given ARN from the key store in order to access the device.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** Timezone **   
The time zone of the DB instance. The time zone parameter is currently supported only by [RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone) and [RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone).  
Type: String  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of Amazon EC2 VPC security groups to associate with this DB instance.  
This setting doesn't apply to Amazon Aurora DB instances. The associated list of EC2 VPC security groups is managed by the DB cluster.  
Default: The default EC2 VPC security group for the DB subnet group's VPC.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_CreateDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_CreateDBInstance_Errors"></a>

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

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
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

 ** DomainNotFoundFault **   
 `Domain` doesn't refer to an existing Active Directory domain.  
HTTP Status Code: 404

 ** InstanceQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB instances.  
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
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

 ** TenantDatabaseQuotaExceeded **   
You attempted to create more tenant databases than are permitted in your AWS account.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_CreateDBInstance_Examples"></a>

### Example
<a name="API_CreateDBInstance_Example_1"></a>

This example illustrates one usage of CreateDBInstance.

#### Sample Request
<a name="API_CreateDBInstance_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateDBInstance
   &AllocatedStorage=15
   &DBInstanceClass=db.m5.large
   &DBInstanceIdentifier=myawsuser-dbi01
   &Engine=MySQL
   &MasterUserPassword=<password>
   &MasterUsername=myawsuser
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140424/us-east-1/rds/aws4_request
   &X-Amz-Date=20140424T194844Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=bee4aabc750bf7dad0cd9e22b952bd6089d91e2a16592c2293e532eeaab8bc77
```

#### Sample Response
<a name="API_CreateDBInstance_Example_1_Response"></a>

```
<CreateDBInstanceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBInstanceResult>
    <DBInstance>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
      <DBInstanceStatus>creating</DBInstanceStatus>
      <MultiAZ>false</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>myawsuser-dbi01</DBInstanceIdentifier>
      
      <PreferredBackupWindow>03:50-04:20</PreferredBackupWindow>
      <PreferredMaintenanceWindow>wed:06:38-wed:07:08</PreferredMaintenanceWindow>
      <ReadReplicaDBInstanceIdentifiers/>
      <Engine>mysql</Engine>
      <PendingModifiedValues>
        <MasterUserPassword>****</MasterUserPassword>
      </PendingModifiedValues>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.13</EngineVersion>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
      <OptionGroupMemberships>
        <OptionGroupMembership>
          <OptionGroupName>default:mysql-5-6</OptionGroupName>
          <Status>in-sync</Status>
        </OptionGroupMembership>
      </OptionGroupMemberships>
      <DBSecurityGroups>
        <DBSecurityGroup>
          <Status>active</Status>
          <DBSecurityGroupName>default</DBSecurityGroupName>
        </DBSecurityGroup>
      </DBSecurityGroups>
      <PubliclyAccessible>true</PubliclyAccessible>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <AllocatedStorage>15</AllocatedStorage>
      <DBInstanceClass>db.m5.large</DBInstanceClass>
      <MasterUsername>myawsuser</MasterUsername>
    </DBInstance>
  </CreateDBInstanceResult>
  <ResponseMetadata>
    <RequestId>523e3218-afc7-11c3-90f5-f90431260ab4</RequestId>
  </ResponseMetadata>
</CreateDBInstanceResponse>
```

## See Also
<a name="API_CreateDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBInstance) 