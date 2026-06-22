---
id: "@specs/aws/docdb/docs/API_DBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBCluster
<a name="API_DBCluster"></a>

Detailed information about a cluster. 

## Contents
<a name="API_DBCluster_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AssociatedRoles.DBClusterRole.N **   
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. (IAM) roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.  
Type: Array of [DBClusterRole](API_DBClusterRole.md) objects  
Required: No

 ** AvailabilityZones.AvailabilityZone.N **   
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.  
Type: Array of strings  
Required: No

 ** BackupRetentionPeriod **   
Specifies the number of days for which automatic snapshots are retained.  
Type: Integer  
Required: No

 ** CloneGroupId **   
Identifies the clone group to which the DB cluster is associated.  
Type: String  
Required: No

 ** ClusterCreateTime **   
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** DBClusterArn **   
The Amazon Resource Name (ARN) for the cluster.  
Type: String  
Required: No

 ** DBClusterIdentifier **   
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.  
Type: String  
Required: No

 ** DBClusterMembers.DBClusterMember.N **   
Provides the list of instances that make up the cluster.  
Type: Array of [DBClusterMember](API_DBClusterMember.md) objects  
Required: No

 ** DBClusterParameterGroup **   
Specifies the name of the cluster parameter group for the cluster.  
Type: String  
Required: No

 ** DbClusterResourceId **   
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.  
Type: String  
Required: No

 ** DBSubnetGroup **   
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.  
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether this cluster can be deleted. If `DeletionProtection` is enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled. `DeletionProtection` protects clusters from being accidentally deleted.  
Type: Boolean  
Required: No

 ** EarliestRestorableTime **   
The earliest time to which a database can be restored with point-in-time restore.  
Type: Timestamp  
Required: No

 ** EnabledCloudwatchLogsExports.member.N **   
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.  
Type: Array of strings  
Required: No

 ** Endpoint **   
Specifies the connection endpoint for the primary instance of the cluster.  
Type: String  
Required: No

 ** Engine **   
Provides the name of the database engine to be used for this cluster.  
Type: String  
Required: No

 ** EngineVersion **   
Indicates the database engine version.  
Type: String  
Required: No

 ** HostedZoneId **   
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.  
Type: String  
Required: No

 ** IOOptimizedNextAllowedModificationTime **   
The next time you can modify the Amazon DocumentDB cluster to use the iopt1 storage type.  
Type: Timestamp  
Required: No

 ** KmsKeyId **   
If `StorageEncrypted` is `true`, the AWS KMS key identifier for the encrypted cluster.  
Type: String  
Required: No

 ** LatestRestorableTime **   
Specifies the latest time to which a database can be restored with point-in-time restore.  
Type: Timestamp  
Required: No

 ** MasterUsername **   
Contains the master user name for the cluster.  
Type: String  
Required: No

 ** MasterUserSecret **   
The secret managed by Amazon DocumentDB in AWS Secrets Manager for the master user password.  
Type: [ClusterMasterUserSecret](API_ClusterMasterUserSecret.md) object  
Required: No

 ** MultiAZ **   
Specifies whether the cluster has instances in multiple Availability Zones.  
Type: Boolean  
Required: No

 ** NetworkType **   
The network type of the cluster.  
The network type is determined by the `DBSubnetGroup` specified for the cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [DocumentDB clusters in a VPC](https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html) in the Amazon DocumentDB Developer Guide.  
Valid Values: `IPV4` \| `DUAL`   
Type: String  
Required: No

 ** PercentProgress **   
Specifies the progress of the operation as a percentage.  
Type: String  
Required: No

 ** Port **   
Specifies the port that the database engine is listening on.  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.   
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).  
Type: String  
Required: No

 ** ReaderEndpoint **   
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.   
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.  
Type: String  
Required: No

 ** ReadReplicaIdentifiers.ReadReplicaIdentifier.N **   
Contains one or more identifiers of the secondary clusters that are associated with this cluster.  
Type: Array of strings  
Required: No

 ** ReplicationSourceIdentifier **   
Contains the identifier of the source cluster if this cluster is a secondary cluster.  
Type: String  
Required: No

 ** ServerlessV2ScalingConfiguration **   
The scaling configuration of an Amazon DocumentDB Serverless cluster.  
Type: [ServerlessV2ScalingConfigurationInfo](API_ServerlessV2ScalingConfigurationInfo.md) object  
Required: No

 ** Status **   
Specifies the current state of this cluster.  
Type: String  
Required: No

 ** StorageEncrypted **   
Specifies whether the cluster is encrypted.  
Type: Boolean  
Required: No

 ** StorageType **   
Storage type associated with your cluster  
For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide*.  
Valid values for storage type - `standard | iopt1`   
Default value is `standard `   
Type: String  
Required: No

 ** VpcSecurityGroups.VpcSecurityGroupMembership.N **   
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects  
Required: No

## See Also
<a name="API_DBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBCluster) 