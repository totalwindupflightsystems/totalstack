---
id: "@specs/aws/rds/docs/API_CreateDBInstanceReadReplica"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBInstanceReadReplica"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBInstanceReadReplica

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBInstanceReadReplica
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBInstanceReadReplica
<a name="API_CreateDBInstanceReadReplica"></a>

Creates a new DB instance that acts as a read replica for an existing source DB instance or Multi-AZ DB cluster. You can create a read replica for a DB instance running Db2, MariaDB, MySQL, Oracle, PostgreSQL, or SQL Server. You can create a read replica for a Multi-AZ DB cluster running MySQL or PostgreSQL. For more information, see [Working with read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) and [Migrating from a Multi-AZ DB cluster to a DB instance using a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html#multi-az-db-clusters-migrating-to-instance-with-read-replica) in the *Amazon RDS User Guide*.

Amazon Aurora doesn't support this operation. To create a DB instance for an Aurora DB cluster, use the `CreateDBInstance` operation.

RDS creates read replicas with backups disabled. All other attributes (including DB security groups and DB parameter groups) are inherited from the source DB instance or cluster, except as specified.

**Important**  
Your source DB instance or cluster must have backup retention enabled.

## Request Parameters
<a name="API_CreateDBInstanceReadReplica_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The DB instance identifier of the read replica. This identifier is the unique key that identifies a DB instance. This parameter is stored as a lowercase string.  
Type: String  
Required: Yes

 **AdditionalStorageVolumes.member.N**   
A list of additional storage volumes to create for the DB instance. You can create up to three additional storage volumes using the names `rdsdbdata2`, `rdsdbdata3`, and `rdsdbdata4`. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.  
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects  
Required: No

 ** AllocatedStorage **   
The amount of storage (in gibibytes) to allocate initially for the read replica. Follow the allocation rules specified in `CreateDBInstance`.  
This setting isn't valid for RDS for SQL Server.  
Be sure to allocate enough storage for your read replica so that the create operation can succeed. You can also allocate additional storage for future growth.
Type: Integer  
Required: No

 ** AutoMinorVersionUpgrade **   
Specifies whether to automatically apply minor engine upgrades to the read replica during the maintenance window.  
This setting doesn't apply to RDS Custom DB instances.  
Default: Inherits the value from the source DB instance.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The Availability Zone (AZ) where the read replica will be created.  
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.  
Example: `us-east-1d`   
Type: String  
Required: No

 ** BackupTarget **   
The location where RDS stores automated backups and manual snapshots.  
Valid Values:  
+  `local` for Dedicated Local Zones
+  `region` for AWS Region 
Type: String  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the read replica's server certificate.  
This setting doesn't apply to RDS Custom DB instances.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the read replica to snapshots of the read replica. By default, tags aren't copied.  
Type: Boolean  
Required: No

 ** CustomIamInstanceProfile **   
The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:  
+ The profile must exist in your account.
+ The profile must have an IAM role that Amazon EC2 has permissions to assume.
+ The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom`.
For the list of permissions required for the IAM role, see [ Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.  
This setting is required for RDS Custom DB instances.  
Type: String  
Required: No

 ** DatabaseInsightsMode **   
The mode of Database Insights to enable for the read replica.  
This setting isn't supported.
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DBInstanceClass **   
The compute and memory capacity of the read replica, for example db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.  
Default: Inherits the value from the source DB instance.  
Type: String  
Required: No

 ** DBParameterGroupName **   
The name of the DB parameter group to associate with this read replica DB instance.  
For the Db2 DB engine, if your source DB instance uses the bring your own license (BYOL) model, then a custom parameter group must be associated with the replica. For a same AWS Region replica, if you don't specify a custom parameter group, Amazon RDS associates the custom parameter group associated with the source DB instance. For a cross-Region replica, you must specify a custom parameter group. This custom parameter group must include your IBM Site ID and IBM Customer ID. For more information, see [IBM IDs for bring your own license (BYOL) for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html#db2-prereqs-ibm-info).   
For Single-AZ or Multi-AZ DB instance read replica instances, if you don't specify a value for `DBParameterGroupName`, then Amazon RDS uses the `DBParameterGroup` of the source DB instance for a same Region read replica, or the default `DBParameterGroup` for the specified DB engine for a cross-Region read replica.  
For Multi-AZ DB cluster same Region read replica instances, if you don't specify a value for `DBParameterGroupName`, then Amazon RDS uses the default `DBParameterGroup`.  
Specifying a parameter group for this operation is only supported for MySQL DB instances for cross-Region read replicas, for Multi-AZ DB cluster read replica instances, for Db2 DB instances, and for Oracle DB instances. It isn't supported for MySQL DB instances for same Region read replicas or for RDS Custom.  
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: No

 ** DBSubnetGroupName **   
A DB subnet group for the DB instance. The new DB instance is created in the VPC associated with the DB subnet group. If no DB subnet group is specified, then the new DB instance isn't created in a VPC.  
Constraints:  
+ If supplied, must match the name of an existing DB subnet group.
+ The specified DB subnet group must be in the same AWS Region in which the operation is running.
+ All read replicas in one AWS Region that are created from the same source DB instance must either:
  + Specify DB subnet groups from the same VPC. All these read replicas are created in the same VPC.
  + Not specify a DB subnet group. All these read replicas are created outside of any VPC.
Example: `mydbsubnetgroup`   
Type: String  
Required: No

 ** DedicatedLogVolume **   
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether to enable deletion protection for the DB instance. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see [ Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.  
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
+ Can't be longer than 64 characters.
Example: `OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain`   
Type: String  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
The list of logs that the new DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Array of strings  
Required: No

 ** EnableCustomerOwnedIp **   
Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts read replica.  
A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the read replica from outside of its virtual private cloud (VPC) on your local network.  
For more information about RDS on Outposts, see [Working with Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide*.  
For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the * AWS Outposts User Guide*.  
Type: Boolean  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
For more information about IAM database authentication, see [ IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to enable Performance Insights for the read replica.  
For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance.  
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted read replica.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you create an encrypted read replica in the same AWS Region as the source DB instance or Multi-AZ DB cluster, don't specify a value for this parameter. A read replica in the same AWS Region is always encrypted with the same KMS key as the source DB instance or cluster.  
If you create an encrypted read replica in a different AWS Region, then you must specify a KMS key identifier for the destination AWS Region. KMS keys are specific to the AWS Region that they are created in, and you can't use KMS keys from one AWS Region in another AWS Region.  
You can't create an encrypted read replica from an unencrypted DB instance or Multi-AZ DB cluster.  
This setting doesn't apply to RDS Custom, which uses the same KMS key as the primary replica.  
Type: String  
Required: No

 ** MaxAllocatedStorage **   
The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.  
For more information about this setting, including limitations that apply to it, see [ Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.  
Type: Integer  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the read replica. To disable collection of Enhanced Monitoring metrics, specify `0`. The default is `0`.  
If `MonitoringRoleArn` is specified, then you must set `MonitoringInterval` to a value other than `0`.  
This setting doesn't apply to RDS Custom DB instances.  
Valid Values: `0, 1, 5, 10, 15, 30, 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`. For information on creating a monitoring role, go to [To create an IAM role for Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole) in the *Amazon RDS User Guide*.  
If `MonitoringInterval` is set to a value other than 0, then you must supply a `MonitoringRoleArn` value.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** MultiAZ **   
Specifies whether the read replica is in a Multi-AZ deployment.  
You can create a read replica as a Multi-AZ DB instance. RDS creates a standby of your replica in another Availability Zone for failover support for the replica. Creating your read replica as a Multi-AZ DB instance is independent of whether the source is a Multi-AZ DB instance or a Multi-AZ DB cluster.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
Valid Values:  
+  `IPV4` 
+  `DUAL` 
The network type is determined by the `DBSubnetGroup` specified for read replica. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*   
Type: String  
Required: No

 ** OptionGroupName **   
The option group to associate the DB instance with. If not specified, RDS uses the option group associated with the source DB instance or cluster.  
For SQL Server, you must use the option group associated with the source.
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you do not specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
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
The port number that the DB instance uses for connections.  
Valid Values: `1150-65535`   
Default: Inherits the value from the source DB instance.  
Type: Integer  
Required: No

 ** PreSignedUrl **   
When you are creating a read replica from one AWS GovCloud (US) Region to another or from one China AWS Region to another, the URL that contains a Signature Version 4 signed request for the `CreateDBInstanceReadReplica` API operation in the source AWS Region that contains the source DB instance.  
This setting applies only to AWS GovCloud (US) Regions and China AWS Regions. It's ignored in other AWS Regions.  
This setting applies only when replicating from a source DB *instance*. Source DB clusters aren't supported in AWS GovCloud (US) Regions and China AWS Regions.  
You must specify this parameter when you create an encrypted read replica from another AWS Region by using the Amazon RDS API. Don't specify `PreSignedUrl` when you are creating an encrypted read replica in the same AWS Region.  
The presigned URL must be a valid request for the `CreateDBInstanceReadReplica` API operation that can run in the source AWS Region that contains the encrypted source DB instance. The presigned URL request must contain the following parameter values:  
+  `DestinationRegion` - The AWS Region that the encrypted read replica is created in. This AWS Region is the same one where the `CreateDBInstanceReadReplica` operation is called that contains this presigned URL.

  For example, if you create an encrypted DB instance in the us-west-1 AWS Region, from a source DB instance in the us-east-2 AWS Region, then you call the `CreateDBInstanceReadReplica` operation in the us-east-1 AWS Region and provide a presigned URL that contains a call to the `CreateDBInstanceReadReplica` operation in the us-west-2 AWS Region. For this example, the `DestinationRegion` in the presigned URL must be set to the us-east-1 AWS Region.
+  `KmsKeyId` - The AWS KMS key identifier for the key to use to encrypt the read replica in the destination AWS Region. This is the same identifier for both the `CreateDBInstanceReadReplica` operation that is called in the destination AWS Region, and the operation contained in the presigned URL.
+  `SourceDBInstanceIdentifier` - The DB instance identifier for the encrypted DB instance to be replicated. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are creating an encrypted read replica from a DB instance in the us-west-2 AWS Region, then your `SourceDBInstanceIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:instance:mysql-instance1-20161115`.
To learn how to generate a Signature Version 4 signed request, see [Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source AWS Region.
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 **ProcessorFeatures.ProcessorFeature.N**   
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB instance is publicly accessible.  
When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.  
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBInstance](API_CreateDBInstance.md).  
Type: Boolean  
Required: No

 ** ReplicaMode **   
The open mode of the replica database.  
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

 ** SourceDBClusterIdentifier **   
The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.  
Constraints:  
+ Must be the identifier of an existing Multi-AZ DB cluster.
+ Can't be specified if the `SourceDBInstanceIdentifier` parameter is also specified.
+ The specified DB cluster must have automatic backups enabled, that is, its backup retention period must be greater than 0.
+ The source DB cluster must be in the same AWS Region as the read replica. Cross-Region replication isn't supported.
Type: String  
Required: No

 ** SourceDBInstanceIdentifier **   
The identifier of the DB instance that will act as the source for the read replica. Each DB instance can have up to 15 read replicas, except for the following engines:  
+ Db2 - Can have up to three replicas.
+ Oracle - Can have up to five read replicas.
+ SQL Server - Can have up to five read replicas.
Constraints:  
+ Must be the identifier of an existing Db2, MariaDB, MySQL, Oracle, PostgreSQL, or SQL Server DB instance.
+ Can't be specified if the `SourceDBClusterIdentifier` parameter is also specified.
+ For the limitations of Oracle read replicas, see [Version and licensing considerations for RDS for Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.limitations.html#oracle-read-replicas.limitations.versions-and-licenses) in the *Amazon RDS User Guide*.
+ For the limitations of SQL Server read replicas, see [Read replica limitations with SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html#SQLServer.ReadReplicas.Limitations) in the *Amazon RDS User Guide*.
+ The specified DB instance must have automatic backups enabled, that is, its backup retention period must be greater than 0.
+ If the source DB instance is in the same AWS Region as the read replica, specify a valid DB instance identifier.
+ If the source DB instance is in a different AWS Region from the read replica, specify a valid DB instance ARN. For more information, see [Constructing an ARN for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the *Amazon RDS User Guide*. This doesn't apply to SQL Server or RDS Custom, which don't support cross-Region replicas.
Type: String  
Required: No

 ** StorageThroughput **   
Specifies the storage throughput value for the read replica.  
This setting doesn't apply to RDS Custom or Amazon Aurora DB instances.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type to associate with the read replica.  
If you specify `io1`, `io2`, or `gp3`, you must also include a value for the `Iops` parameter.  
Valid Values: `gp2 | gp3 | io1 | io2 | standard`   
Default: `io1` if the `Iops` parameter is specified. Otherwise, `gp3`.  
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

 ** UpgradeStorageConfig **   
Whether to upgrade the storage file system configuration on the read replica. This option migrates the read replica from the old storage file system layout to the preferred layout.  
Type: Boolean  
Required: No

 ** UseDefaultProcessorFeatures **   
Specifies whether the DB instance class of the DB instance uses its default processor features.  
This setting doesn't apply to RDS Custom DB instances.  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of Amazon EC2 VPC security groups to associate with the read replica.  
This setting doesn't apply to RDS Custom DB instances.  
Default: The default EC2 VPC security group for the DB subnet group's VPC.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_CreateDBInstanceReadReplica_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_CreateDBInstanceReadReplica_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **   
 `CertificateIdentifier` doesn't refer to an existing certificate.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
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

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotAllowedFault **   
The DBSubnetGroup shouldn't be specified while creating read replicas that lie in the same region as the source instance.  
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

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBSubnetGroupFault **   
The DBSubnetGroup doesn't belong to the same VPC as that of an existing cross-region read replica of the same source instance.  
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
<a name="API_CreateDBInstanceReadReplica_Examples"></a>

### Example
<a name="API_CreateDBInstanceReadReplica_Example_1"></a>

This example illustrates one usage of CreateDBInstanceReadReplica.

#### Sample Request
<a name="API_CreateDBInstanceReadReplica_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateDBInstanceReadReplica
   &DBInstanceIdentifier=mysqldb-rr
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBInstanceIdentifier=mysqldb
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T170525Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=a5bc7bb9648272e9967c76fc582b308d3ee37d6c4f7a4eb62c2d885ec595c373
```

#### Sample Response
<a name="API_CreateDBInstanceReadReplica_Example_1_Response"></a>

```
<CreateDBInstanceReadReplicaResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBInstanceReadReplicaResult>
    <DBInstance>
      <BackupRetentionPeriod>0</BackupRetentionPeriod>
      <MultiAZ>false</MultiAZ>
      <DBInstanceStatus>creating</DBInstanceStatus>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>mysqldb-rr</DBInstanceIdentifier>
      <PreferredBackupWindow>08:14-08:44</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:04:50-fri:05:20</PreferredMaintenanceWindow>
      <ReadReplicaDBInstanceIdentifiers/>
      <Engine>mysql</Engine>
      <PendingModifiedValues/>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.13</EngineVersion>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
      <ReadReplicaSourceDBInstanceIdentifier>mysqldb</ReadReplicaSourceDBInstanceIdentifier>
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
  </CreateDBInstanceReadReplicaResult>
  <ResponseMetadata>
    <RequestId>ba8dedf0-bb9a-11d3-855b-576787000e19</RequestId>
  </ResponseMetadata>
</CreateDBInstanceReadReplicaResponse>
```

## See Also
<a name="API_CreateDBInstanceReadReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBInstanceReadReplica) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBInstanceReadReplica) 