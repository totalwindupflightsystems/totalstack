---
id: "@specs/aws/rds/docs/API_ModifyDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBCluster
<a name="API_ModifyDBCluster"></a>

Modifies the settings of an Amazon Aurora DB cluster or a Multi-AZ DB cluster. You can change one or more settings by specifying these parameters and the new values in the request.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_ModifyDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier for the cluster being modified. This parameter isn't case-sensitive.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must match the identifier of an existing DB cluster.
Type: String  
Required: Yes

 ** AllocatedStorage **   
The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Type: Integer  
Required: No

 ** AllowEngineModeChange **   
Specifies whether engine mode changes from `serverless` to `provisioned` are allowed.  
Valid for Cluster Type: Aurora Serverless v1 DB clusters only  
Constraints:  
+ You must allow engine mode changes when specifying a different value for the `EngineMode` parameter from the DB cluster's current engine mode.
Type: Boolean  
Required: No

 ** AllowMajorVersionUpgrade **   
Specifies whether major version upgrades are allowed.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ You must allow major version upgrades when specifying a value for the `EngineVersion` parameter that is a different major version than the DB cluster's current version.
Type: Boolean  
Required: No

 ** ApplyImmediately **   
Specifies whether the modifications in this request are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB cluster. If this parameter is disabled, changes to the DB cluster are applied during the next maintenance window.  
Most modifications can be applied immediately or during the next scheduled maintenance window. Some modifications, such as turning on deletion protection and changing the master password, are applied immediately—regardless of when you choose to apply them.  
By default, this parameter is disabled.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
Type: String  
Length Constraints: Minimum length of 43. Maximum length of 350.  
Pattern: `arn:aws[a-z-]*:backup:[-a-z0-9]+:[0-9]{12}:[-a-z]+:([a-z0-9\-]+:)?[a-z][a-z0-9\-]{0,255}`   
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
The number of days for which automated backups are retained. Specify a minimum value of `1`.  
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

 ** CloudwatchLogsExportConfiguration **   
The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
The following values are valid for each DB engine:  
+ Aurora MySQL - `audit | error | general | instance | slowquery | iam-db-auth-error` 
+ Aurora PostgreSQL - `instance | postgresql | iam-db-auth-error` 
+ RDS for MySQL - `error | general | slowquery | iam-db-auth-error` 
+ RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error` 
For more information about exporting CloudWatch Logs for Amazon RDS, see [ Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
For more information about exporting CloudWatch Logs for Amazon Aurora, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.  
Type: [CloudwatchLogsExportConfiguration](API_CloudwatchLogsExportConfiguration.md) object  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** DatabaseInsightsMode **   
Specifies the mode of Database Insights to enable for the DB cluster.  
If you change the value from `standard` to `advanced`, you must set the `PerformanceInsightsEnabled` parameter to `true` and the `PerformanceInsightsRetentionPeriod` parameter to 465.  
If you change the value from `advanced` to `standard`, you can set the `PerformanceInsightsEnabled` parameter to `true` to collect detailed database counter and per-query metrics.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBClusterInstanceClass **   
The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example `db.m6gd.xlarge`. Not all DB instance classes are available in all AWS Regions, or for all database engines.  
For the full list of DB instance classes and availability for your engine, see [ DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Type: String  
Required: No

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group to use for the DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** DBInstanceParameterGroupName **   
The name of the DB parameter group to apply to all instances of the DB cluster.  
When you apply a parameter group using the `DBInstanceParameterGroupName` parameter, the DB cluster isn't rebooted automatically. Also, parameter changes are applied immediately rather than during the next maintenance window.
Valid for Cluster Type: Aurora DB clusters only  
Default: The existing name setting  
Constraints:  
+ The DB parameter group must be in the same DB parameter group family as this DB cluster.
+ The `DBInstanceParameterGroupName` parameter is valid in combination with the `AllowMajorVersionUpgrade` parameter for a major version upgrade only.
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to move the DB cluster to. Specify `none` to remove the cluster from its current domain. The domain must be created prior to this operation.  
For more information, see [Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** DomainIAMRoleName **   
The name of the IAM role to use when making API calls to the Directory Service.  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** EnableGlobalWriteForwarding **   
Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.  
You can set this value only on Aurora DB clusters that are members of an Aurora global database. With this parameter enabled, a secondary cluster can forward writes to the current primary cluster, and the resulting changes are replicated back to this cluster. For the primary DB cluster of an Aurora global database, this value is used immediately if the primary is demoted by a global cluster API operation, but it does nothing until then.  
Valid for Cluster Type: Aurora DB clusters only  
Type: Boolean  
Required: No

 ** EnableHttpEndpoint **   
Specifies whether to enable the HTTP endpoint for an Aurora Serverless v1 DB cluster. By default, the HTTP endpoint isn't enabled.  
When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the Aurora Serverless v1 DB cluster. You can also query your database from inside the RDS console with the RDS query editor.  
For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.  
This parameter applies only to Aurora Serverless v1 DB clusters. To enable or disable the HTTP endpoint for an Aurora Serverless v2 or provisioned DB cluster, use the `EnableHttpEndpoint` and `DisableHttpEndpoint` operations.
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
This setting is no longer used. Instead use the `ClusterScalabilityType` setting when you create your Aurora Limitless Database DB cluster.
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

 ** EngineMode **   
The DB engine mode of the DB cluster, either `provisioned` or `serverless`.  
The DB engine mode can be modified only from `serverless` to `provisioned`.
For more information, see [ CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html).  
Valid for Cluster Type: Aurora DB clusters only  
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless `ApplyImmediately` is enabled.  
If the cluster that you're modifying has one or more read replicas, all replicas must be running an engine version that's the same or later than the version you specify.  
To list all of the available engine versions for Aurora MySQL, use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"`   
To list all of the available engine versions for Aurora PostgreSQL, use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions[].EngineVersion"`   
To list all of the available engine versions for RDS for MySQL, use the following command:  
 `aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions[].EngineVersion"`   
To list all of the available engine versions for RDS for PostgreSQL, use the following command:  
 `aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions[].EngineVersion"`   
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.  
For information about valid IOPS values, see [Amazon RDS Provisioned IOPS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Constraints:  
+ Must be a multiple between .5 and 50 of the storage amount for the DB cluster.
Type: Integer  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
If the DB cluster doesn't manage the master user password with AWS Secrets Manager, you can turn on this management. In this case, you can't specify `MasterUserPassword`.  
If the DB cluster already manages the master user password with AWS Secrets Manager, and you specify that the master user password is not managed with AWS Secrets Manager, then you must specify `MasterUserPassword`. In this case, RDS deletes the secret and uses the new password for the master user specified by `MasterUserPassword`.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*   
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** MasterUserAuthenticationType **   
Specifies the authentication type for the master user. With IAM master user authentication, you can change the master DB user to use IAM database authentication.  
You can specify one of the following values:  
+  `password` - Use standard database authentication with a password.
+  `iam-db-auth` - Use IAM database authentication for the master user.
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.  
Type: String  
Valid Values: `password | iam-db-auth`   
Required: No

 ** MasterUserPassword **   
The new password for the master database user.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must contain from 8 to 41 characters.
+ Can contain any printable ASCII character except "/", """, or "@".
+ Can't be specified if `ManageMasterUserPassword` is turned on.
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if both of the following conditions are met:  
+ The DB cluster doesn't manage the master user password in AWS Secrets Manager.

  If the DB cluster already manages the master user password in AWS Secrets Manager, you can't change the KMS key that is used to encrypt the secret.
+ You are turning on `ManageMasterUserPassword` to manage the master user password in AWS Secrets Manager.

  If you are turning on `ManageMasterUserPassword` and don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify `0`.  
If `MonitoringRoleArn` is specified, also set `MonitoringInterval` to a value other than `0`.  
Valid for Cluster Type: Multi-AZ DB clusters only  
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, see [To create an IAM role for Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole) in the *Amazon RDS User Guide.*   
If `MonitoringInterval` is set to a value other than `0`, supply a `MonitoringRoleArn` value.  
Valid for Cluster Type: Multi-AZ DB clusters only  
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

 ** NewDBClusterIdentifier **   
The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster2`   
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
The port number on which the DB cluster accepts connections.  
Valid for Cluster Type: Aurora DB clusters only  
Valid Values: `1150-65535`   
Default: The same port as the original DB cluster.  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter.  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To view the time blocks available, see [ Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see [ Adjusting the Preferred DB Cluster Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora) in the *Amazon Aurora User Guide*.  
Constraints:  
+ Must be in the format `ddd:hh24:mi-ddd:hh24:mi`.
+ Days must be one of `Mon | Tue | Wed | Thu | Fri | Sat | Sun`.
+ Must be in Universal Coordinated Time (UTC).
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** RotateMasterUserPassword **   
Specifies whether to rotate the secret managed by AWS Secrets Manager for the master user password.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB cluster. The secret value contains the updated password.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*   
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ You must apply the change immediately when rotating the master user password.
Type: Boolean  
Required: No

 ** ScalingConfiguration **   
The scaling properties of the DB cluster. You can only modify scaling properties for DB clusters in `serverless` DB engine mode.  
Valid for Cluster Type: Aurora DB clusters only  
Type: [ScalingConfiguration](API_ScalingConfiguration.md) object  
Required: No

 ** ServerlessV2ScalingConfiguration **   
Contains the scaling configuration of an Aurora Serverless v2 DB cluster.  
For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.  
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object  
Required: No

 ** StorageType **   
The storage type to associate with the DB cluster.  
For information on storage types for Aurora DB clusters, see [Storage configurations for Amazon Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type). For information on storage types for Multi-AZ DB clusters, see [Settings for creating Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html#create-multi-az-db-cluster-settings).  
When specified for a Multi-AZ DB cluster, a value for the `Iops` parameter is required.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values:  
+ Aurora DB clusters - `aurora | aurora-iopt1` 
+ Multi-AZ DB clusters - `io1 | io2 | gp3` 
Default:  
+ Aurora DB clusters - `aurora` 
+ Multi-AZ DB clusters - `io1` 
Type: String  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of EC2 VPC security groups to associate with this DB cluster.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_ModifyDBCluster_Errors"></a>

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

 ** DBInstanceAlreadyExists **   
The user already has a DB instance with the given identifier.  
HTTP Status Code: 400

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** DomainNotFoundFault **   
 `Domain` doesn't refer to an existing Active Directory domain.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBSecurityGroupState **   
The state of the DB security group doesn't allow deletion.  
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

 ** StorageTypeNotAvailableFault **   
The `aurora-iopt1` storage type isn't available, because you modified the DB cluster to use this storage type less than one month ago.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBCluster_Examples"></a>

### Modifying an Aurora DB cluster
<a name="API_ModifyDBCluster_Example_1"></a>

This example illustrates one usage of ModifyDBCluster.

#### Sample Request
<a name="API_ModifyDBCluster_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ModifyDBCluster
    &DBClusterIdentifier=sample-cluster3
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140725/us-west-2/rds/aws4_request
    &X-Amz-Date=20140725T161457Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=d6d1c65c2e94f5800ab411a3f7336625820b103713b6c063430900514e21d784
```

#### Sample Response
<a name="API_ModifyDBCluster_Example_1_Response"></a>

```
<ModifyDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBClusterResult>
    <DBCluster>
      <Engine>aurora5.6</Engine>
      <Status>available</Status>
      <BackupRetentionPeriod>0</BackupRetentionPeriod>
      <DBSubnetGroup>my-subgroup</DBSubnetGroup>
      <EngineVersion>5.6.10a</EngineVersion>
      <Endpoint>sample-cluster3.cluster-cefgqfx9y5fy.us-east-1.rds.amazonaws.com</Endpoint>
      <DBClusterIdentifier>sample-cluster3</DBClusterIdentifier>
      <PreferredBackupWindow>07:06-07:36</PreferredBackupWindow>
      <PreferredMaintenanceWindow>tue:10:18-tue:10:48</PreferredMaintenanceWindow>
      <DBClusterMembers>
        <DBClusterMember>
          <IsClusterWriter>true</IsClusterWriter>
          <DBInstanceIdentifier>sample-cluster3-master</DBInstanceIdentifier>
        </DBClusterMember>
        <DBClusterMember>
          <IsClusterWriter>false</IsClusterWriter>
          <DBInstanceIdentifier>sample-cluster3-read1</DBInstanceIdentifier>
        </DBClusterMember>
      </DBClusterMembers>
      <AllocatedStorage>15</AllocatedStorage>
      <MasterUsername>awsuser</MasterUsername>
    </DBCluster>
  </ModifyDBClusterResult>
  <ResponseMetadata>
    <RequestId>d2cd0e2f-1416-11e4-9210-cf99df4125d0</RequestId>
  </ResponseMetadata>
</ModifyDBClusterResponse>
```

### Modifying a Multi-AZ DB cluster
<a name="API_ModifyDBCluster_Example_2"></a>

This example illustrates one usage of ModifyDBCluster.

#### Sample Request
<a name="API_ModifyDBCluster_Example_2_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ModifyDBCluster
    &DBClusterIdentifier=my-multi-az-cluster
    &DBClusterInstanceClass=db.m6gd.large
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20211026/us-west-2/rds/aws4_request
    &X-Amz-Date=20211027T000032Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=d6d1c65c2e94f5800ab411a3f7336625820b103713b6c063430900514e21d784
```

#### Sample Response
<a name="API_ModifyDBCluster_Example_2_Response"></a>

```
<ModifyDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/"> 
  <ModifyDBClusterResult> 
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
        <EngineVersion>8.0.26</EngineVersion> 
        <MasterUsername>admin</MasterUsername> 
        <DBClusterMembers> 
          <DBClusterMember> 
            <DBInstanceIdentifier>my-multi-az-cluster-instance-3</DBInstanceIdentifier> 
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
            <IsClusterWriter>true</IsClusterWriter> 
          </DBClusterMember> 
        </DBClusterMembers> 
        <HttpEndpointEnabled>false</HttpEndpointEnabled> 
        <Port>3306</Port> 
        <MonitoringInterval>30</MonitoringInterval> 
        <BackupRetentionPeriod>2</BackupRetentionPeriod> 
        <KmsKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</KmsKeyId> 
        <DBClusterIdentifier>my-multi-az-cluster</DBClusterIdentifier> 
        <DbClusterResourceId>cluster-TSW4QJNKY3P2DNDRR523BDGEIU</DbClusterResourceId> 
        <Status>available</Status> 
        <LatestRestorableTime>2021-10-26T23:55:00Z</LatestRestorableTime> 
        <PreferredBackupWindow>11:34-12:04</PreferredBackupWindow> 
        <DeletionProtection>false</DeletionProtection> 
        <Endpoint>my-multi-az-cluster.cluster-123456789012.us-west-2.rds.amazonaws.com</Endpoint> 
        <EngineMode>provisioned</EngineMode> 
        <Engine>mysql</Engine> 
        <ReaderEndpoint>my-multi-az-cluster.cluster-ro-123456789012.us-west-2.rds.amazonaws.com</ReaderEndpoint> 
        <PubliclyAccessible>true</PubliclyAccessible> 
        <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled> 
        <EarliestRestorableTime>2021-10-26T20:42:03.375Z</EarliestRestorableTime> 
        <ClusterCreateTime>2021-10-26T20:31:54.943Z</ClusterCreateTime> 
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
        <HostedZoneId>Z3GZ3VYA3PGHTQ</HostedZoneId> 
        <TagList /> 
        <PreferredMaintenanceWindow>sat:07:05-sat:07:35</PreferredMaintenanceWindow> 
        <DBClusterParameterGroup>my-multi-az-cpg</DBClusterParameterGroup> 
        <StorageType>io1</StorageType> 
        <DBClusterInstanceClass>db.m6gd.large</DBClusterInstanceClass> 
        <CopyTagsToSnapshot>false</CopyTagsToSnapshot> 
        <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade> 
        <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:my-multi-az-cluster</DBClusterArn> 
      </DBCluster> 
  </ModifyDBClusterResult> 
  <ResponseMetadata> 
    <RequestId>69673d54-e48e-4ba4-9333-c5a6c1e7526a</RequestId> 
  </ResponseMetadata> 
</ModifyDBClusterResponse>
```

## See Also
<a name="API_ModifyDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBCluster) 