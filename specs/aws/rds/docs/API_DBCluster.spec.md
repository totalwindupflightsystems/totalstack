---
id: "@specs/aws/rds/docs/API_DBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBCluster
<a name="API_DBCluster"></a>

Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster. 

For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.

For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.* 

For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Contents
<a name="API_DBCluster_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ActivityStreamKinesisStreamName **   
The name of the Amazon Kinesis data stream used for the database activity stream.  
Type: String  
Required: No

 ** ActivityStreamKmsKeyId **   
The AWS KMS key identifier used for encrypting messages in the database activity stream.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** ActivityStreamMode **   
The mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.  
Type: String  
Valid Values: `sync | async`   
Required: No

 ** ActivityStreamStatus **   
The status of the database activity stream.  
Type: String  
Valid Values: `stopped | starting | started | stopping`   
Required: No

 ** AllocatedStorage **   
 `AllocatedStorage` specifies the allocated storage size in gibibytes (GiB). For Aurora, `AllocatedStorage` can vary because Aurora DB cluster storage size adjusts as needed.  
Type: Integer  
Required: No

 ** AssociatedRoles.DBClusterRole.N **   
A list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon Web Services on your behalf.  
Type: Array of [DBClusterRole](API_DBClusterRole.md) objects  
Required: No

 ** AutomaticRestartTime **   
The time when a stopped DB cluster is restarted automatically.  
Type: Timestamp  
Required: No

 ** AutoMinorVersionUpgrade **   
Indicates whether minor version patches are applied automatically.  
This setting is for Aurora DB clusters and Multi-AZ DB clusters.  
For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).  
Type: Boolean  
Required: No

 ** AvailabilityZones.AvailabilityZone.N **   
The list of Availability Zones (AZs) where instances in the DB cluster can be created.  
Type: Array of strings  
Required: No

 ** AwsBackupRecoveryPointArn **   
The Amazon Resource Name (ARN) of the recovery point in AWS Backup.  
Type: String  
Required: No

 ** BacktrackConsumedChangeRecords **   
The number of change records stored for Backtrack.  
Type: Long  
Required: No

 ** BacktrackWindow **   
The target backtrack window, in seconds. If this value is set to `0`, backtracking is disabled for the DB cluster. Otherwise, backtracking is enabled.  
Type: Long  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automatic DB snapshots are retained.  
Type: Integer  
Required: No

 ** Capacity **   
The current capacity of an Aurora Serverless v1 DB cluster. The capacity is `0` (zero) when the cluster is paused.  
For more information about Aurora Serverless v1, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide*.  
Type: Integer  
Required: No

 ** CertificateDetails **   
The details of the DB instance’s server certificate.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: [CertificateDetails](API_CertificateDetails.md) object  
Required: No

 ** CharacterSetName **   
If present, specifies the name of the character set that this cluster is associated with.  
Type: String  
Required: No

 ** CloneGroupId **   
The ID of the clone group with which the DB cluster is associated. For newly created clusters, the ID is typically null.   
If you clone a DB cluster when the ID is null, the operation populates the ID value for the source cluster and the clone because both clusters become part of the same clone group. Even if you delete the clone cluster, the clone group ID remains for the lifetime of the source cluster to show that it was used in a cloning operation.  
For PITR, the clone group ID is inherited from the source cluster. For snapshot restore operations, the clone group ID isn't inherited from the source cluster.  
Type: String  
Required: No

 ** ClusterCreateTime **   
The time when the DB cluster was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** ClusterScalabilityType **   
The scalability mode of the Aurora DB cluster. When set to `limitless`, the cluster operates as an Aurora Limitless Database. When set to `standard` (the default), the cluster uses normal DB instance creation.  
Type: String  
Valid Values: `standard | limitless`   
Required: No

 ** CopyTagsToSnapshot **   
Indicates whether tags are copied from the DB cluster to snapshots of the DB cluster.  
Type: Boolean  
Required: No

 ** CrossAccountClone **   
Indicates whether the DB cluster is a clone of a DB cluster owned by a different AWS account.  
Type: Boolean  
Required: No

 ** CustomEndpoints.member.N **   
The custom endpoints associated with the DB cluster.  
Type: Array of strings  
Required: No

 ** DatabaseInsightsMode **   
The mode of Database Insights that is enabled for the DB cluster.  
Type: String  
Valid Values: `standard | advanced`   
Required: No

 ** DatabaseName **   
The name of the initial database that was specified for the DB cluster when it was created, if one was provided. This same name is returned for the life of the DB cluster.  
Type: String  
Required: No

 ** DBClusterArn **   
The Amazon Resource Name (ARN) for the DB cluster.  
Type: String  
Required: No

 ** DBClusterIdentifier **   
The user-supplied identifier for the DB cluster. This identifier is the unique key that identifies a DB cluster.  
Type: String  
Required: No

 ** DBClusterInstanceClass **   
The name of the compute and memory capacity class of the DB instance.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: String  
Required: No

 ** DBClusterMembers.DBClusterMember.N **   
The list of DB instances that make up the DB cluster.  
Type: Array of [DBClusterMember](API_DBClusterMember.md) objects  
Required: No

 ** DBClusterOptionGroupMemberships.DBClusterOptionGroup.N **   
The list of option group memberships for this DB cluster.  
Type: Array of [DBClusterOptionGroupStatus](API_DBClusterOptionGroupStatus.md) objects  
Required: No

 ** DBClusterParameterGroup **   
The name of the DB cluster parameter group for the DB cluster.  
Type: String  
Required: No

 ** DbClusterResourceId **   
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the KMS key for the DB cluster is accessed.  
Type: String  
Required: No

 ** DBSubnetGroup **   
Information about the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.  
Type: String  
Required: No

 ** DBSystemId **   
Reserved for future use.  
Type: String  
Required: No

 ** DeletionProtection **   
Indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.  
Type: Boolean  
Required: No

 ** DomainMemberships.DomainMembership.N **   
The Active Directory Domain membership records associated with the DB cluster.  
Type: Array of [DomainMembership](API_DomainMembership.md) objects  
Required: No

 ** EarliestBacktrackTime **   
The earliest time to which a DB cluster can be backtracked.  
Type: Timestamp  
Required: No

 ** EarliestRestorableTime **   
The earliest time to which a database can be restored with point-in-time restore.  
Type: Timestamp  
Required: No

 ** EnabledCloudwatchLogsExports.member.N **   
A list of log types that this DB cluster is configured to export to CloudWatch Logs.  
Log types vary by DB engine. For information about the log types for each DB engine, see [Amazon RDS Database Log Files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html) in the *Amazon Aurora User Guide.*   
Type: Array of strings  
Required: No

 ** Endpoint **   
The connection endpoint for the primary instance of the DB cluster.  
Type: String  
Required: No

 ** Engine **   
The database engine used for this DB cluster.  
Type: String  
Required: No

 ** EngineLifecycleSupport **   
The lifecycle type for the DB cluster.  
For more information, see CreateDBCluster.  
Type: String  
Required: No

 ** EngineMode **   
The DB engine mode of the DB cluster, either `provisioned` or `serverless`.  
For more information, see [ CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html).  
Type: String  
Required: No

 ** EngineVersion **   
The version of the database engine.  
Type: String  
Required: No

 ** GlobalClusterIdentifier **   
Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database cluster.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** GlobalWriteForwardingRequested **   
Indicates whether write forwarding is enabled for a secondary cluster in an Aurora global database. Because write forwarding takes time to enable, check the value of `GlobalWriteForwardingStatus` to confirm that the request has completed before using the write forwarding feature for this cluster.  
Type: Boolean  
Required: No

 ** GlobalWriteForwardingStatus **   
The status of write forwarding for a secondary cluster in an Aurora global database.  
Type: String  
Valid Values: `enabled | disabled | enabling | disabling | unknown`   
Required: No

 ** HostedZoneId **   
The ID that Amazon Route 53 assigns when you create a hosted zone.  
Type: String  
Required: No

 ** HttpEndpointEnabled **   
Indicates whether the HTTP endpoint is enabled for an Aurora DB cluster.  
When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.  
For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.  
Type: Boolean  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
Indicates whether the mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.  
Type: Boolean  
Required: No

 ** InternetAccessGatewayEnabled **   
Indicates whether the DB cluster has internet-based connectivity enabled through an internet access gateway.  
This setting is applicable only for Aurora PostgreSQL clusters created through express configuration.  
Type: Boolean  
Required: No

 ** IOOptimizedNextAllowedModificationTime **   
The next time you can modify the DB cluster to use the `aurora-iopt1` storage type.  
This setting is only for Aurora DB clusters.  
Type: Timestamp  
Required: No

 ** Iops **   
The Provisioned IOPS (I/O operations per second) value.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** KmsKeyId **   
If `StorageEncrypted` is enabled, the AWS KMS key identifier for the encrypted DB cluster.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: No

 ** LatestRestorableTime **   
The latest time to which a database can be restored with point-in-time restore.  
Type: Timestamp  
Required: No

 ** LimitlessDatabase **   
The details for Aurora Limitless Database.  
Type: [LimitlessDatabase](API_LimitlessDatabase.md) object  
Required: No

 ** LocalWriteForwardingStatus **   
Indicates whether an Aurora DB cluster has in-cluster write forwarding enabled, not enabled, requested, or is in the process of enabling it.  
Type: String  
Valid Values: `enabled | disabled | enabling | disabling | requested`   
Required: No

 ** MasterUsername **   
The master username for the DB cluster.  
Type: String  
Required: No

 ** MasterUserSecret **   
The secret managed by RDS in AWS Secrets Manager for the master user password.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*   
Type: [MasterUserSecret](API_MasterUserSecret.md) object  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster.  
This setting is only for -Aurora DB clusters and Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.  
This setting is only for Aurora DB clusters and Multi-AZ DB clusters.  
Type: String  
Required: No

 ** MultiAZ **   
Indicates whether the DB cluster has instances in multiple Availability Zones.  
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the DB instance.  
The network type is determined by the `DBSubnetGroup` specified for the DB cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*   
This setting is only for Aurora DB clusters.  
Valid Values: `IPV4 | DUAL`   
Type: String  
Required: No

 ** PendingModifiedValues **   
Information about pending changes to the DB cluster. This information is returned only when there are pending changes. Specific changes are identified by subelements.  
Type: [ClusterPendingModifiedValues](API_ClusterPendingModifiedValues.md) object  
Required: No

 ** PercentProgress **   
The progress of the operation as a percentage.  
Type: String  
Required: No

 ** PerformanceInsightsEnabled **   
Indicates whether Performance Insights is enabled for the DB cluster.  
This setting is only for Aurora DB clusters and Multi-AZ DB clusters.  
Type: Boolean  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
This setting is only for Aurora DB clusters and Multi-AZ DB clusters.  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data.  
This setting is only for Aurora DB clusters and Multi-AZ DB clusters.  
Valid Values:  
+  `7` 
+  *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731` 
Default: `7` days  
Type: Integer  
Required: No

 ** Port **   
The port that the database engine is listening on.  
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

 ** PubliclyAccessible **   
Indicates whether the DB cluster is publicly accessible.  
When the DB cluster is publicly accessible and you connect from outside of the DB cluster's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.  
When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBCluster](API_CreateDBCluster.md).  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Boolean  
Required: No

 ** RdsCustomClusterConfiguration **   
Reserved for future use.  
Type: [RdsCustomClusterConfiguration](API_RdsCustomClusterConfiguration.md) object  
Required: No

 ** ReaderEndpoint **   
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Aurora Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Aurora distributes the connection requests among the Aurora Replicas in the DB cluster. This functionality can help balance your read workload across multiple Aurora Replicas in your DB cluster.  
If a failover occurs, and the Aurora Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Aurora Replicas in the cluster, you can then reconnect to the reader endpoint.  
Type: String  
Required: No

 ** ReadReplicaIdentifiers.ReadReplicaIdentifier.N **   
Contains one or more identifiers of the read replicas associated with this DB cluster.  
Type: Array of strings  
Required: No

 ** ReplicationSourceIdentifier **   
The identifier of the source DB cluster if this DB cluster is a read replica.  
Type: String  
Required: No

 ** ScalingConfigurationInfo **   
The scaling configuration for an Aurora DB cluster in `serverless` DB engine mode.  
For more information, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide*.  
Type: [ScalingConfigurationInfo](API_ScalingConfigurationInfo.md) object  
Required: No

 ** ServerlessV2PlatformVersion **   
The version of the Aurora Serverless V2 platform used by the DB cluster. For more information, see [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.  
Type: String  
Required: No

 ** ServerlessV2ScalingConfiguration **   
The scaling configuration for an Aurora Serverless v2 DB cluster.  
For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.  
Type: [ServerlessV2ScalingConfigurationInfo](API_ServerlessV2ScalingConfigurationInfo.md) object  
Required: No

 ** Status **   
The current state of this DB cluster.  
Type: String  
Required: No

 ** StatusInfos.DBClusterStatusInfo.N **   
Reserved for future use.  
Type: Array of [DBClusterStatusInfo](API_DBClusterStatusInfo.md) objects  
Required: No

 ** StorageEncrypted **   
Indicates whether the DB cluster is encrypted.  
Type: Boolean  
Required: No

 ** StorageEncryptionType **   
The type of encryption used to protect data at rest in the DB cluster. Possible values:  
+  `none` - The DB cluster is not encrypted.
+  `sse-rds` - The DB cluster is encrypted using an AWS owned KMS key.
+  `sse-kms` - The DB cluster is encrypted using a customer managed KMS key or AWS managed KMS key.
Type: String  
Valid Values: `none | sse-kms | sse-rds`   
Required: No

 ** StorageThroughput **   
The storage throughput for the DB cluster. The throughput is automatically set based on the IOPS that you provision, and is not configurable.  
This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** StorageType **   
The storage type associated with the DB cluster.  
Type: String  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** UpgradeRolloutOrder **   
This data type represents the order in which the clusters are upgraded.  
+ [first] - Typically used for development or testing environments.
+ [second] - Default order for resources not specifically configured.
+ [last] - Usually reserved for production environments.
Type: String  
Valid Values: `first | second | last`   
Required: No

 ** VPCNetworkingEnabled **   
Indicates whether the DB cluster uses VPC-based networking.  
This setting is applicable only for Aurora PostgreSQL clusters created through express configuration.  
Type: Boolean  
Required: No

 ** VpcSecurityGroups.VpcSecurityGroupMembership.N **   
The list of VPC security groups that the DB cluster belongs to.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects  
Required: No

## See Also
<a name="API_DBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBCluster) 