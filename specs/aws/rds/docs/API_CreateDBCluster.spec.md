---
id: "@specs/aws/rds/docs/API_CreateDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBCluster
<a name="API_CreateDBCluster"></a>

Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.

If you create an Aurora DB cluster, the request creates an empty cluster. You must explicitly create the writer instance for your DB cluster using the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) operation. If you create a Multi-AZ DB cluster, the request creates a writer and two reader DB instances for you, each in a different Availability Zone.

You can use the `ReplicationSourceIdentifier` parameter to create an Amazon Aurora DB cluster as a read replica of another DB cluster or Amazon RDS for MySQL or PostgreSQL DB instance. For more information about Amazon Aurora, see [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

You can also use the `ReplicationSourceIdentifier` parameter to create a Multi-AZ DB cluster read replica with an RDS for MySQL or PostgreSQL DB instance as the source. For more information about Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

You can use the `WithExpressConfiguration` parameter to create an Aurora DB Cluster with express configuration and create cluster in seconds. Express configuration provides a cluster with a writer instance and feature specific values set to all other input parameters of this API. 

## Request Parameters
<a name="API_CreateDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier for this DB cluster. This parameter is stored as a lowercase string.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must contain from 1 to 63 (for Aurora DB clusters) or 1 to 52 (for Multi-AZ DB clusters) letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1`   
Type: String  
Required: Yes

 ** Engine **   
The database engine to use for this DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
+  `mysql` 
+  `postgres` 
+  `neptune` - For information about using Amazon Neptune, see the [https://docs.aws.amazon.com/neptune/latest/userguide/intro.html](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html).
Type: String  
Required: Yes

 ** AllocatedStorage **   
The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.  
Valid for Cluster Type: Multi-AZ DB clusters only  
This setting is required to create a Multi-AZ DB cluster.  
Type: Integer  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB cluster.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 **AvailabilityZones.AvailabilityZone.N**   
A list of Availability Zones (AZs) where you specifically want to create DB instances in the DB cluster.  
For the first three DB instances that you create, RDS distributes each DB instance to a different AZ that you specify. For additional DB instances that you create, RDS randomly distributes them to the AZs that you specified. For example, if you create a DB cluster with one writer instance and three reader instances, RDS might distribute the writer instance to AZ 1, the first reader instance to AZ 2, the second reader instance to AZ 3, and the third reader instance to either AZ 1, AZ 2, or AZ 3.   
For more information, see [Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.AvailabilityZones) and [High availability for Aurora DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Instances) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters only  
Constraints:  
+ Can't specify more than three AZs.
Type: Array of strings  
Required: No

 ** BacktrackWindow **   
The target backtrack window, in seconds. To disable backtracking, set this value to `0`.  
Valid for Cluster Type: Aurora MySQL DB clusters only  
Default: `0`   
Constraints:  
+ If specified, this value must be set to a number from 0 to 259,200 (72 hours).
Type: Long  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Default: `1`   
Constraints:  
+ Must be a value from 1 to 35.
Type: Integer  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the DB cluster's server certificate.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide*.  
Valid for Cluster Type: Multi-AZ DB clusters  
Type: String  
Required: No

 ** CharacterSetName **   
The name of the character set (`CharacterSet`) to associate the DB cluster with.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** ClusterScalabilityType **   
Specifies the scalability mode of the Aurora DB cluster. When set to `limitless`, the cluster operates as an Aurora Limitless Database. When set to `standard` (the default), the cluster uses normal DB instance creation.  
Valid for: Aurora DB clusters only  
You can't modify this setting after you create the DB cluster.
Type: String  
Valid Values: `standard | limitless`   
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** DatabaseInsightsMode **   
The mode of Database Insights to enable for the DB cluster.  
If you set this value to `advanced`, you must also set the `PerformanceInsightsEnabled` parameter to `true` and the `PerformanceInsightsRetentionPeriod` parameter to 465.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DatabaseName **   
The name for your database of up to 64 alphanumeric characters. A database named `postgres` is always created. If this parameter is specified, an additional database with this name is created.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** DBClusterInstanceClass **   
The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example `db.m6gd.xlarge`. Not all DB instance classes are available in all AWS Regions, or for all database engines.  
For the full list of DB instance classes and availability for your engine, see [DB instance class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.  
This setting is required to create a Multi-AZ DB cluster.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Type: String  
Required: No

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group to associate with this DB cluster. If you don't specify a value, then the default DB cluster parameter group for the specified DB engine and version is used.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ If supplied, must match the name of an existing DB cluster parameter group.
Type: String  
Required: No

 ** DBSubnetGroupName **   
A DB subnet group to associate with this DB cluster.  
This setting is required to create a Multi-AZ DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must match the name of an existing DB subnet group.
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DBSystemId **   
Reserved for future use.  
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to create the DB cluster in.  
For Amazon Aurora DB clusters, Amazon RDS can use Kerberos authentication to authenticate users that connect to the DB cluster.  
For more information, see [Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** DomainIAMRoleName **   
The name of the IAM role to use when making API calls to the Directory Service.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
The list of log types that need to be enabled for exporting to CloudWatch Logs.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
The following values are valid for each DB engine:  
+ Aurora MySQL - `audit | error | general | instance | slowquery | iam-db-auth-error` 
+ Aurora PostgreSQL - `instance | postgresql | iam-db-auth-error` 
+ RDS for MySQL - `error | general | slowquery | iam-db-auth-error` 
+ RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error` 
For more information about exporting CloudWatch Logs for Amazon RDS, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
For more information about exporting CloudWatch Logs for Amazon Aurora, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.  
Type: Array of strings  
Required: No

 ** EnableGlobalWriteForwarding **   
Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.  
You can set this value only on Aurora DB clusters that are members of an Aurora global database. With this parameter enabled, a secondary cluster can forward writes to the current primary cluster, and the resulting changes are replicated back to this cluster. For the primary DB cluster of an Aurora global database, this value is used immediately if the primary is demoted by a global cluster API operation, but it does nothing until then.  
Valid for Cluster Type: Aurora DB clusters only  
Type: Boolean  
Required: No

 ** EnableHttpEndpoint **   
Specifies whether to enable the HTTP endpoint for the DB cluster. By default, the HTTP endpoint isn't enabled.  
When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.  
For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters only  
Type: Boolean  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
For more information, see [ IAM Database Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon Aurora User Guide* or [IAM database authentication for MariaDB, MySQL, and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide*.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** EnableLimitlessDatabase **   
Specifies whether to enable Aurora Limitless Database. You must enable Aurora Limitless Database to create a DB shard group.  
Valid for: Aurora DB clusters only  
This setting is no longer used. Instead use the `ClusterScalabilityType` setting.
Type: Boolean  
Required: No

 ** EnableLocalWriteForwarding **   
Specifies whether read replicas can forward write operations to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.  
Valid for: Aurora DB clusters only  
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to turn on Performance Insights for the DB cluster.  
For more information, see [ Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this DB cluster.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, creating the DB cluster will fail if the DB major version is past its end of standard support date.
You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:  
+ Amazon Aurora - [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide* 
+ Amazon RDS - [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* 
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** EngineMode **   
The DB engine mode of the DB cluster, either `provisioned` or `serverless`.  
The `serverless` engine mode only applies for Aurora Serverless v1 DB clusters. Aurora Serverless v2 DB clusters use the `provisioned` engine mode.  
For information about limitations and requirements for Serverless DB clusters, see the following sections in the *Amazon Aurora User Guide*:  
+  [Limitations of Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html#aurora-serverless.limitations) 
+  [Requirements for Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html) 
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine to use.  
To list all of the available engine versions for Aurora MySQL version 2 (5.7-compatible) and version 3 (MySQL 8.0-compatible), use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"`   
You can supply either `5.7` or `8.0` to use the default engine version for Aurora MySQL version 2 or version 3, respectively.  
To list all of the available engine versions for Aurora PostgreSQL, use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions[].EngineVersion"`   
To list all of the available engine versions for RDS for MySQL, use the following command:  
 `aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions[].EngineVersion"`   
To list all of the available engine versions for RDS for PostgreSQL, use the following command:  
 `aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions[].EngineVersion"`   
For information about a specific engine, see the following topics:  
+ Aurora MySQL - see [Database engine updates for Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) in the *Amazon Aurora User Guide*.
+ Aurora PostgreSQL - see [Amazon Aurora PostgreSQL releases and engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html) in the *Amazon Aurora User Guide*.
+ RDS for MySQL - see [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide*.
+ RDS for PostgreSQL - see [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts) in the *Amazon RDS User Guide*.
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** GlobalClusterIdentifier **   
The global cluster ID of an Aurora cluster that becomes the primary cluster in the new global database cluster.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.  
For information about valid IOPS values, see [Provisioned IOPS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.  
This setting is required to create a Multi-AZ DB cluster.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Constraints:  
+ Must be a multiple between .5 and 50 of the storage amount for the DB cluster.
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted DB cluster.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
When a KMS key isn't specified in `KmsKeyId`:  
+ If `ReplicationSourceIdentifier` identifies an encrypted source, then Amazon RDS uses the KMS key used to encrypt the source. Otherwise, Amazon RDS uses your default KMS key.
+ If the `StorageEncrypted` parameter is enabled and `ReplicationSourceIdentifier` isn't specified, then Amazon RDS uses your default KMS key.
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
If you create a read replica of an encrypted DB cluster in another AWS Region, make sure to set `KmsKeyId` to a KMS key identifier that is valid in the destination AWS Region. This KMS key is used to encrypt the read replica in that AWS Region.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*   
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
Type: Boolean  
Required: No

 ** MasterUserAuthenticationType **   
Specifies the authentication type for the master user. With IAM master user authentication, you can configure the master DB user with IAM database authentication when you create a DB cluster.  
You can specify one of the following values:  
+  `password` - Use standard database authentication with a password.
+  `iam-db-auth` - Use IAM database authentication for the master user.
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.  
Type: String  
Valid Values: `password | iam-db-auth`   
Required: No

 ** MasterUsername **   
The name of the master user for the DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must be 1 to 16 letters or numbers.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
Type: String  
Required: No

 ** MasterUserPassword **   
The password for the master database user.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must contain from 8 to 41 characters.
+ Can contain any printable ASCII character except "/", """, or "@".
+ Can't be specified if `ManageMasterUserPassword` is turned on.
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB cluster.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify `0`.  
If `MonitoringRoleArn` is specified, also set `MonitoringInterval` to a value other than `0`.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [Setting up and enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide*.  
If `MonitoringInterval` is set to a value other than `0`, supply a `MonitoringRoleArn` value.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** NetworkType **   
The network type of the DB cluster.  
The network type is determined by the `DBSubnetGroup` specified for the DB cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*   
Valid for Cluster Type: Aurora DB clusters only  
Valid Values: `IPV4 | DUAL`   
Type: String  
Required: No

 ** OptionGroupName **   
The option group to associate the DB cluster with.  
DB clusters are associated with a default option group that can't be modified.  
Type: String  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you don't specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values:  
+  `7` 
+  *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731` 
Default: `7` days  
If you specify a retention period that isn't valid, such as `94`, Amazon RDS issues an error.  
Type: Integer  
Required: No

 ** Port **   
The port number on which the instances in the DB cluster accept connections.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values: `1150-65535`   
Default:  
+ RDS for MySQL and Aurora MySQL - `3306` 
+ RDS for PostgreSQL and Aurora PostgreSQL - `5432` 
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled using the `BackupRetentionPeriod` parameter.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To view the time blocks available, see [ Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow) in the *Amazon Aurora User Guide*.  
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range during which system maintenance can occur.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see [ Adjusting the Preferred DB Cluster Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora) in the *Amazon Aurora User Guide*.  
Constraints:  
+ Must be in the format `ddd:hh24:mi-ddd:hh24:mi`.
+ Days must be one of `Mon | Tue | Wed | Thu | Fri | Sat | Sun`.
+ Must be in Universal Coordinated Time (UTC).
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreSignedUrl **   
When you are replicating a DB cluster from one AWS GovCloud (US) Region to another, an URL that contains a Signature Version 4 signed request for the `CreateDBCluster` operation to be called in the source AWS Region where the DB cluster is replicated from. Specify `PreSignedUrl` only when you are performing cross-Region replication from an encrypted DB cluster.  
The presigned URL must be a valid request for the `CreateDBCluster` API operation that can run in the source AWS Region that contains the encrypted DB cluster to copy.  
The presigned URL request must contain the following parameter values:  
+  `KmsKeyId` - The AWS KMS key identifier for the KMS key to use to encrypt the copy of the DB cluster in the destination AWS Region. This should refer to the same KMS key for both the `CreateDBCluster` operation that is called in the destination AWS Region, and the operation contained in the presigned URL.
+  `DestinationRegion` - The name of the AWS Region that Aurora read replica will be created in.
+  `ReplicationSourceIdentifier` - The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster from the us-west-2 AWS Region, then your `ReplicationSourceIdentifier` would look like Example: `arn:aws:rds:us-west-2:123456789012:cluster:aurora-cluster1`.
To learn how to generate a Signature Version 4 signed request, see [ Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [ Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source AWS Region.
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB cluster is publicly accessible.  
Valid for Cluster Type: Multi-AZ DB clusters only  
When the DB cluster is publicly accessible and you connect from outside of the DB cluster's virtual private cloud (VPC), its domain name system (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is controlled by its security group settings.  
When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.  
The default behavior when `PubliclyAccessible` is not specified depends on whether a `DBSubnetGroup` is specified.  
If `DBSubnetGroup` isn't specified, `PubliclyAccessible` defaults to `true`.  
If `DBSubnetGroup` is specified, `PubliclyAccessible` defaults to `false` unless the value of `DBSubnetGroup` is `default`, in which case `PubliclyAccessible` defaults to `true`.  
If `PubliclyAccessible` is true and the VPC that the `DBSubnetGroup` is in doesn't have an internet gateway attached to it, Amazon RDS returns an error.  
Type: Boolean  
Required: No

 ** RdsCustomClusterConfiguration **   
Reserved for future use.  
Type: [RdsCustomClusterConfiguration](API_RdsCustomClusterConfiguration.md) object  
Required: No

 ** ReplicationSourceIdentifier **   
The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a read replica.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** ScalingConfiguration **   
For DB clusters in `serverless` DB engine mode, the scaling properties of the DB cluster.  
Valid for Cluster Type: Aurora DB clusters only  
Type: [ScalingConfiguration](API_ScalingConfiguration.md) object  
Required: No

 ** ServerlessV2ScalingConfiguration **   
Contains the scaling configuration of an Aurora Serverless v2 DB cluster.  
For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.  
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object  
Required: No

 ** StorageEncrypted **   
Specifies whether the DB cluster is encrypted.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** StorageType **   
The storage type to associate with the DB cluster.  
For information on storage types for Aurora DB clusters, see [Storage configurations for Amazon Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type). For information on storage types for Multi-AZ DB clusters, see [Settings for creating Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html#create-multi-az-db-cluster-settings).  
This setting is required to create a Multi-AZ DB cluster.  
When specified for a Multi-AZ DB cluster, a value for the `Iops` parameter is required.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values:  
+ Aurora DB clusters - `aurora | aurora-iopt1` 
+ Multi-AZ DB clusters - `io1 | io2 | gp3` 
Default:  
+ Aurora DB clusters - `aurora` 
+ Multi-AZ DB clusters - `io1` 
When you create an Aurora DB cluster with the storage type set to `aurora-iopt1`, the storage type is returned in the response. The storage type isn't returned when you set it to `aurora`.
Type: String  
Required: No

 **Tags.Tag.N**   
Tags to assign to the DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB cluster.  
Valid Values:   
+  `cluster-auto-backup` - The DB cluster's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of EC2 VPC security groups to associate with this DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Array of strings  
Required: No

 ** WithExpressConfiguration **   
Specifies to create an Aurora DB Cluster with express configuration in seconds. Express configuration provides a cluster with a writer instance and feature specific values set to all other input parameters of this API.   
Valid for Cluster Type: Aurora DB clusters  
Type: Boolean  
Required: No

## Response Elements
<a name="API_CreateDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_CreateDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **   
The user already has a DB cluster with the given identifier.  
HTTP Status Code: 400

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterParameterGroupNotFound **   
 `DBClusterParameterGroupName` doesn't refer to an existing DB cluster parameter group.  
HTTP Status Code: 404

 ** DBClusterQuotaExceededFault **   
The user attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.  
HTTP Status Code: 403

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
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

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.  
HTTP Status Code: 404

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InsufficientStorageClusterCapacity **   
There is insufficient storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBSubnetGroupFault **   
The DBSubnetGroup doesn't belong to the same VPC as that of an existing cross-region read replica of the same source instance.  
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **   
The DB subnet group cannot be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The global cluster is in an invalid state and can't perform the requested operation.  
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

 ** StorageQuotaExceeded **   
The request would result in the user exceeding the allowed amount of storage available across all DB instances.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_CreateDBCluster_Examples"></a>

### Creating an Aurora DB cluster
<a name="API_CreateDBCluster_Example_1"></a>

This example illustrates one usage of CreateDBCluster.

#### Sample Request
<a name="API_CreateDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CreateDBCluster
    &DBClusterIdentifier=sample-cluster
    &Engine=aurora
    &MasterUserPassword=<password>
    &MasterUsername=myawsuser
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20150927/us-east-1/rds/aws4_request
    &X-Amz-Date=20220927T164851Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=6a8f4bd6a98f649c75ea04a6b3929ecc75ac09739588391cd7250f5280e716db
```

#### Sample Response
<a name="API_CreateDBCluster_Example_1_Response"></a>

```
<CreateDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBClusterResult>
    <DBCluster>
      <Port>3306</Port>
      <Engine>aurora</Engine>
      <Status>creating</Status>
      <BackupRetentionPeriod>1</BackupRetentionPeriod>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <Status>active</Status>
          <VpcSecurityGroupId>sg-2103dc23</VpcSecurityGroupId>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <DBSubnetGroup>default</DBSubnetGroup>
      <EngineVersion>5.7</EngineVersion>
      <Endpoint>sample-cluster.cluster-ctrayan0rynq.us-east-1.rds.amazonaws.com</Endpoint>
      <DBClusterParameterGroup>default.aurora5.6</DBClusterParameterGroup>
      <AvailabilityZones>
        <AvailabilityZone>us-east-1a</AvailabilityZone>
        <AvailabilityZone>us-east-1c</AvailabilityZone>
        <AvailabilityZone>us-east-1e</AvailabilityZone>
      </AvailabilityZones>
      <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
      <PreferredBackupWindow>04:22-04:52</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:06:44-fri:07:14</PreferredMaintenanceWindow>
      <DBClusterMembers/>
      <AllocatedStorage>1</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
    </DBCluster>
  </CreateDBClusterResult>
  <ResponseMetadata>
    <RequestId>46d2b228-7681-11e5-3e8b-9b2c0d5d51a9</RequestId>
  </ResponseMetadata>
</CreateDBClusterResponse>
```

### Creating a Multi-AZ DB cluster
<a name="API_CreateDBCluster_Example_2"></a>

This example illustrates one usage of CreateDBCluster.

#### Sample Request
<a name="API_CreateDBCluster_Example_2_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=CreateDBCluster
    &AvailabilityZones.AvailabilityZone.1=us-west-2a
    &BackupRetentionPeriod=2
    &DatabaseName=mydb
    &DBClusterIdentifier=my-multi-az-cluster
    &DBClusterParameterGroupName=my-multi-az-cpg
    &VpcSecurityGroupIds.VpcSecurityGroupId.1=sg-6921cc28
    &DBSubnetGroupName=mysubnet1
    &Engine=mysql
    &EngineVersion=8.0.26
    &Port=3306
    &MasterUsername=admin
    &MasterUserPassword=<password>
    &PreferredBackupWindow=11:34-12:04
    &PreferredMaintenanceWindow=sat:07:05-sat:07:35
    &StorageEncrypted=true
    &KmsKeyId=123EXAMPLE-abcd-4567-efgEXAMPLE
    &EngineMode=provisioned
    &DeletionProtection=false
    &EnableHttpEndpoint=false
    &CopyTagsToSnapshot=true
    &DBClusterInstanceClass=db.r6gd.large
    &AllocatedStorage=100
    &StorageType=io1
    &Iops=1000
    &PubliclyAccessible=true
    &AutoMinorVersionUpgrade=true
    &MonitoringInterval=30
    &MonitoringRoleArn=arn:aws:iam:123456789012:role/enhance-monitoring-role
    &EnablePerformanceInsights=true
    &PerformanceInsightsKMSKeyId=123EXAMPLE-abcd-4567-efgEXAMPLE
    &PerformanceInsightsRetentionPeriod=7
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20211026/us-west-2/rds/aws4_request
    &X-Amz-Date=20220927T203712Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=6a8f4bd6a98f649c75ea04a6b3929ecc75ac09739588391cd7250f5280e716db
```

#### Sample Response
<a name="API_CreateDBCluster_Example_2_Response"></a>

```
<CreateDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBClusterResult>
    <DBCluster>
      <CrossAccountClone>false</CrossAccountClone>
      <AllocatedStorage>100</AllocatedStorage>
      <DatabaseName>mydb</DatabaseName>
      <AssociatedRoles />
      <AvailabilityZones>
          <AvailabilityZone>us-west-2a</AvailabilityZone>
          <AvailabilityZone>us-west-2b</AvailabilityZone>
          <AvailabilityZone>us-west-2c</AvailabilityZone>
      </AvailabilityZones>
      <ReadReplicaIdentifiers />
      <Iops>1000</Iops>
      <PerformanceInsightsKMSKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</PerformanceInsightsKMSKeyId>
      <PerformanceInsightsRetentionPeriod>7</PerformanceInsightsRetentionPeriod>
      <EngineVersion>8.0.mysql_aurora.3.01.0</EngineVersion>
      <MasterUsername>admin</MasterUsername>
      <DBClusterMembers>
          <DBClusterMember>
              <DBInstanceIdentifier>my-multi-az-cluster-3</DBInstanceIdentifier>
              <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
              <PromotionTier>1</PromotionTier>
              <IsClusterWriter>false</IsClusterWriter>
          </DBClusterMember>
          <DBClusterMember>
              <DBInstanceIdentifier>my-multi-az-cluster-instance-2</DBInstanceIdentifier>
              <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
              <PromotionTier>1</PromotionTier>
              <IsClusterWriter>false</IsClusterWriter>
          </DBClusterMember>
          <DBClusterMember>
              <DBInstanceIdentifier>my-multi-az-cluster-instance-1</DBInstanceIdentifier>
              <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
              <PromotionTier>1</PromotionTier>
              <IsClusterWriter>false</IsClusterWriter>
          </DBClusterMember>
      </DBClusterMembers>
      <HttpEndpointEnabled>false</HttpEndpointEnabled>
      <Port>3306</Port>
      <MonitoringInterval>30</MonitoringInterval>
      <BackupRetentionPeriod>2</BackupRetentionPeriod>
      <KmsKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</KmsKeyId>
      <DBClusterIdentifier>my-multi-az-cluster</DBClusterIdentifier>
      <DbClusterResourceId>cluster-RCPGZXFNIHCTBQLDRJX6CP62VQ</DbClusterResourceId>
      <Status>creating</Status>
      <PreferredBackupWindow>11:34-12:04</PreferredBackupWindow>
      <DeletionProtection>false</DeletionProtection>
      <Endpoint>my-multi-az-cluster.cluster-123456789012.us-west-2.rds.amazonaws.com</Endpoint>
      <EngineMode>provisioned</EngineMode>
      <Engine>mysql</Engine>
      <ReaderEndpoint>my-multi-az-cluster.cluster-ro-123456789012.us-west-2.rds.amazonaws.com</ReaderEndpoint>
      <PubliclyAccessible>true</PubliclyAccessible>
      <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
      <ClusterCreateTime>2021-10-20T00:12:00.867Z</ClusterCreateTime>
      <PerformanceInsightsEnabled>true</PerformanceInsightsEnabled>
      <MultiAZ>true</MultiAZ>
      <DomainMemberships />
      <MonitoringRoleArn>arn:aws:iam::123456789012:role/enhance-monitoring-role</MonitoringRoleArn>
      <StorageEncrypted>true</StorageEncrypted>
      <DBSubnetGroup>mysubnet1</DBSubnetGroup>
      <VpcSecurityGroups>
          <VpcSecurityGroupMembership>
              <VpcSecurityGroupId>sg-6921cc28</VpcSecurityGroupId>
              <Status>active</Status>
          </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <TagList />
      <HostedZoneId>Z3GZ3VYA3PGHTQ</HostedZoneId>
      <PreferredMaintenanceWindow>sat:07:05-sat:07:35</PreferredMaintenanceWindow>
      <DBClusterParameterGroup>my-multi-az-cpg</DBClusterParameterGroup>
      <StorageType>io1</StorageType>
      <DBClusterInstanceClass>db.r6gd.large</DBClusterInstanceClass>
      <CopyTagsToSnapshot>false</CopyTagsToSnapshot>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:my-multi-az-cluster</DBClusterArn>
    </DBCluster>
  </CreateDBClusterResult>
  <ResponseMetadata>
    <RequestId>4c11cdec-1dbb-452c-bfc0-7580e4ba91ce</RequestId>
  </ResponseMetadata>
</CreateDBClusterResponse>
```

### Creating an Aurora DB cluster With Express Configuration
<a name="API_CreateDBCluster_Example_3"></a>

This example illustrates one usage of CreateDBCluster.

#### Sample Request
<a name="API_CreateDBCluster_Example_3_Request"></a>

```
                    https://rds.us-east-1.amazonaws.com/
                    ?Action=CreateDBCluster
                    &DBClusterIdentifier=sample-cluster
                    &Engine=aurora-postgresql
                    &WithExpressConfiguration
                    &SignatureMethod=HmacSHA256
                    &SignatureVersion=4
                    &Version=2014-10-31
                    &X-Amz-Algorithm=AWS4-HMAC-SHA256
                    &X-Amz-Credential=AKIADQKE4SARGYLE/20150927/us-east-1/rds/aws4_request
                    &X-Amz-Date=20220927T164851Z
                    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
                    &X-Amz-Signature=6a8f4bd6a98f649c75ea04a6b3929ecc75ac09739588391cd7250f5280e716db
```

#### Sample Response
<a name="API_CreateDBCluster_Example_3_Response"></a>

```
                    <CreateDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
                    <CreateDBClusterResult>
                    <DBCluster>
                    <AllocatedStorage>1</AllocatedStorage>
                    <AvailabilityZones>
                    <AvailabilityZone>us-east-1c</AvailabilityZone>
                    <AvailabilityZone>us-east-1a</AvailabilityZone>
                    <AvailabilityZone>us-east-1b</AvailabilityZone>
                    </AvailabilityZones>
                    <BackupRetentionPeriod>7</BackupRetentionPeriod>
                    <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
                    <DBClusterParameterGroup>default.aurora-postgresql17</DBClusterParameterGroup>
                    <Status>creating</Status>
                    <MultiAZ>false</MultiAZ>
                    <Engine>aurora-postgresql</Engine>
                    <EngineVersion>17.7</EngineVersion>
                    <Port>5432</Port>
                    <MasterUsername>postgres</MasterUsername>
                    <PreferredBackupWindow>06:15-06:45</PreferredBackupWindow>
                    <PreferredMaintenanceWindow>sat:03:44-sat:04:14</PreferredMaintenanceWindow>
                    <ReadReplicaIdentifiers/>
                    <DBClusterMembers>
                    <DBClusterMember>
                    <DBInstanceIdentifier>sample-cluster-instance-1</DBInstanceIdentifier>
                    <IsClusterWriter>false</IsClusterWriter>
                    <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
                    <PromotionTier>1</PromotionTier>
                    </DBClusterMember>
                    </DBClusterMembers>
                    <VpcSecurityGroups/>
                    <StorageEncrypted>false</StorageEncrypted>
                    <DbClusterResourceId>cluster-OWV7DRHS2W7R4LXZRYNXCHZST4</DbClusterResourceId>
                    <DBClusterArn>arn:aws:rds:us-east-1:654654253058:cluster:sample-cluster</DBClusterArn>
                    <AssociatedRoles/>
                    <IAMDatabaseAuthenticationEnabled>true</IAMDatabaseAuthenticationEnabled>
                    <ClusterCreateTime>2026-01-10T22:14:02Z</ClusterCreateTime>
                    <EngineMode>provisioned</EngineMode>
                    <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
                    <DeletionProtection>false</DeletionProtection>
                    <HttpEndpointEnabled>false</HttpEndpointEnabled>
                    <CopyTagsToSnapshot>false</CopyTagsToSnapshot>
                    <CrossAccountClone>false</CrossAccountClone>
                    <DomainMemberships/>
                    <TagList/>
                    <ServerlessV2ScalingConfiguration>
                    <MinCapacity>0.0</MinCapacity>
                    <MaxCapacity>16.0</MaxCapacity>
                    <SecondsUntilAutoPause>300</SecondsUntilAutoPause>
                    </ServerlessV2ScalingConfiguration>
                    <ServerlessV2PlatformVersion>3</ServerlessV2PlatformVersion>
                    <DatabaseInsightsMode>standard</DatabaseInsightsMode>
                    <PerformanceInsightsEnabled>false</PerformanceInsightsEnabled>
                    <LocalWriteForwardingStatus>disabled</LocalWriteForwardingStatus>
                    <EngineLifecycleSupport>open-source-rds-extended-support</EngineLifecycleSupport>
                    </DBCluster>
                    </CreateDBClusterResult>
                    <ResponseMetadata>
                    <RequestId>46d2b228-7681-11e5-3e8b-9b2c0d5d51a9</RequestId>
                    </ResponseMetadata>
                    </CreateDBClusterResponse>
```

## See Also
<a name="API_CreateDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBCluster) 