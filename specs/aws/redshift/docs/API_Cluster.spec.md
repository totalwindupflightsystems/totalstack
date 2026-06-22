---
id: "@specs/aws/redshift/docs/API_Cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cluster
<a name="API_Cluster"></a>

Describes a cluster.

## Contents
<a name="API_Cluster_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowVersionUpgrade **   
A boolean value that, if `true`, indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.   
Type: Boolean  
Required: No

 ** AquaConfiguration **   
This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).  
Type: [AquaConfiguration](API_AquaConfiguration.md) object  
Required: No

 ** AutomatedSnapshotRetentionPeriod **   
The number of days that automatic cluster snapshots are retained.  
Type: Integer  
Required: No

 ** AvailabilityZone **   
The name of the Availability Zone in which the cluster is located.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AvailabilityZoneRelocationStatus **   
Describes the status of the Availability Zone relocation operation.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CatalogArn **   
The Amazon Resource Name (ARN) of the Glue data catalog associated with the cluster enabled with Amazon Redshift federated permissions.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterAvailabilityStatus **   
The availability status of the cluster for queries. Possible values are the following:  
+ Available - The cluster is available for queries. 
+ Unavailable - The cluster is not available for queries.
+ Maintenance - The cluster is intermittently available for queries due to maintenance activities.
+ Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
+ Failed - The cluster failed and is not available for queries.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterCreateTime **   
The date and time that the cluster was created.  
Type: Timestamp  
Required: No

 ** ClusterIdentifier **   
The unique identifier of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterNamespaceArn **   
The namespace Amazon Resource Name (ARN) of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterNodes.member.N **   
The nodes in the cluster.  
Type: Array of [ClusterNode](API_ClusterNode.md) objects  
Required: No

 ** ClusterParameterGroups.ClusterParameterGroup.N **   
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.  
Type: Array of [ClusterParameterGroupStatus](API_ClusterParameterGroupStatus.md) objects  
Required: No

 ** ClusterPublicKey **   
The public key for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterRevisionNumber **   
The specific revision number of the database in the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterSecurityGroups.ClusterSecurityGroup.N **   
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains `ClusterSecurityGroup.Name` and `ClusterSecurityGroup.Status` subelements.   
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter.   
Type: Array of [ClusterSecurityGroupMembership](API_ClusterSecurityGroupMembership.md) objects  
Required: No

 ** ClusterSnapshotCopyStatus **   
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.  
Type: [ClusterSnapshotCopyStatus](API_ClusterSnapshotCopyStatus.md) object  
Required: No

 ** ClusterStatus **   
 The current state of the cluster. Possible values are the following:  
+  `available` 
+  `available, prep-for-resize` 
+  `available, resize-cleanup` 
+  `cancelling-resize` 
+  `creating` 
+  `deleting` 
+  `final-snapshot` 
+  `hardware-failure` 
+  `incompatible-hsm` 
+  `incompatible-network` 
+  `incompatible-parameters` 
+  `incompatible-restore` 
+  `modifying` 
+  `paused` 
+  `rebooting` 
+  `renaming` 
+  `resizing` 
+  `rotating-keys` 
+  `storage-full` 
+  `updating-hsm` 
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterSubnetGroupName **   
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The version ID of the Amazon Redshift engine that is running on the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustomDomainCertificateArn **   
The certificate Amazon Resource Name (ARN) for the custom domain name.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustomDomainCertificateExpiryDate **   
The expiration date for the certificate associated with the custom domain name.  
Type: Timestamp  
Required: No

 ** CustomDomainName **   
The custom domain name associated with the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DataTransferProgress **   
  
Type: [DataTransferProgress](API_DataTransferProgress.md) object  
Required: No

 ** DBName **   
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named `dev`dev was created by default.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DefaultIamRoleArn **   
The Amazon Resource Name (ARN) for the IAM role set as default for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DeferredMaintenanceWindows.DeferredMaintenanceWindow.N **   
Describes a group of `DeferredMaintenanceWindow` objects.  
Type: Array of [DeferredMaintenanceWindow](API_DeferredMaintenanceWindow.md) objects  
Required: No

 ** ElasticIpStatus **   
The status of the elastic IP (EIP) address.  
Type: [ElasticIpStatus](API_ElasticIpStatus.md) object  
Required: No

 ** ElasticResizeNumberOfNodeOptions **   
The number of nodes that you can resize the cluster to with the elastic resize method.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Encrypted **   
A boolean value that, if `true`, indicates that data in the cluster is encrypted at rest.  
Type: Boolean  
Required: No

 ** Endpoint **   
The connection endpoint.  
Type: [Endpoint](API_Endpoint.md) object  
Required: No

 ** EnhancedVpcRouting **   
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.  
If this option is `true`, enhanced VPC routing is enabled.   
Default: false  
Type: Boolean  
Required: No

 ** ExpectedNextSnapshotScheduleTime **   
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.   
Type: Timestamp  
Required: No

 ** ExpectedNextSnapshotScheduleTimeStatus **   
 The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:  
+ OnTrack - The next snapshot is expected to be taken on time. 
+ Pending - The next snapshot is pending to be taken. 
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ExtraComputeForAutomaticOptimization **   
A boolean value that, if `true`, indicates that the cluster allocates additional compute resources to run automatic optimization operations.  
Default: false  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** HsmStatus **   
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.  
Values: active, applying  
Type: [HsmStatus](API_HsmStatus.md) object  
Required: No

 ** IamRoles.ClusterIamRole.N **   
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.  
Type: Array of [ClusterIamRole](API_ClusterIamRole.md) objects  
Required: No

 ** IpAddressType **   
The IP address type for the cluster. Possible values are `ipv4` and `dualstack`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** KmsKeyId **   
The AWS Key Management Service (KMS) key ID of the encryption key used to encrypt data in the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** LakehouseRegistrationStatus **   
The status of the lakehouse registration for the cluster. Indicates whether the cluster is successfully registered with Amazon Redshift federated permissions.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaintenanceTrackName **   
The name of the maintenance track for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.  
The value must be either -1 or an integer between 1 and 3,653.  
Type: Integer  
Required: No

 ** MasterPasswordSecretArn **   
The Amazon Resource Name (ARN) for the cluster's admin user credentials secret.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MasterPasswordSecretKmsKeyId **   
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MasterUsername **   
The admin user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ModifyStatus **   
The status of a modify operation, if any, initiated for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MultiAZ **   
A boolean value that, if true, indicates that the cluster is deployed in two Availability Zones.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MultiAZSecondary **   
The secondary compute unit of a cluster, if Multi-AZ deployment is turned on.  
Type: [SecondaryClusterInfo](API_SecondaryClusterInfo.md) object  
Required: No

 ** NextMaintenanceWindowStartTime **   
The date and time in UTC when system maintenance can begin.  
Type: Timestamp  
Required: No

 ** NodeType **   
The node type for the nodes in the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The number of compute nodes in the cluster.  
Type: Integer  
Required: No

 ** PendingActions.member.N **   
Cluster operations that are waiting to be started.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PendingModifiedValues **   
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.  
Type: [PendingModifiedValues](API_PendingModifiedValues.md) object  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PubliclyAccessible **   
A boolean value that, if `true`, indicates that the cluster can be accessed from a public network.  
Default: false  
Type: Boolean  
Required: No

 ** ReservedNodeExchangeStatus **   
The status of the reserved-node exchange request. Statuses include in-progress and requested.  
Type: [ReservedNodeExchangeStatus](API_ReservedNodeExchangeStatus.md) object  
Required: No

 ** ResizeInfo **   
Returns the following:  
+ AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
+ ResizeType: Returns ClassicResize
Type: [ResizeInfo](API_ResizeInfo.md) object  
Required: No

 ** RestoreStatus **   
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.  
Type: [RestoreStatus](API_RestoreStatus.md) object  
Required: No

 ** SnapshotScheduleIdentifier **   
A unique identifier for the cluster snapshot schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotScheduleState **   
The current state of the cluster snapshot schedule.  
Type: String  
Valid Values: `MODIFYING | ACTIVE | FAILED`   
Required: No

 ** Tags.Tag.N **   
The list of tags for the cluster.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TotalStorageCapacityInMegaBytes **   
The total storage capacity of the cluster in megabytes.   
Type: Long  
Required: No

 ** VpcId **   
The identifier of the VPC the cluster is in, if the cluster is in a VPC.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** VpcSecurityGroups.VpcSecurityGroup.N **   
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects  
Required: No

## See Also
<a name="API_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Cluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Cluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Cluster) 