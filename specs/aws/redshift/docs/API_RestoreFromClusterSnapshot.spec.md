---
id: "@specs/aws/redshift/docs/API_RestoreFromClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreFromClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RestoreFromClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RestoreFromClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreFromClusterSnapshot
<a name="API_RestoreFromClusterSnapshot"></a>

Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the [ModifyCluster](API_ModifyCluster.md) API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.

If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:
+ Creating a public cluster
+ Restoring a public cluster
+ Modifying a private cluster to be public
+ Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

 For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_RestoreFromClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster that will be created from restoring the snapshot.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ Alphabetic characters must be lowercase.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique for all clusters within an AWS account.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AdditionalInfo **   
Reserved.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AllowVersionUpgrade **   
If `true`, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.   
Default: `true`   
Type: Boolean  
Required: No

 ** AquaConfigurationStatus **   
This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).  
Type: String  
Valid Values: `enabled | disabled | auto`   
Required: No

 ** AutomatedSnapshotRetentionPeriod **   
The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with [CreateClusterSnapshot](API_CreateClusterSnapshot.md).   
You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.  
Default: The value selected for the cluster from which the snapshot was taken.  
Constraints: Must be a value from 0 to 35.  
Type: Integer  
Required: No

 ** AvailabilityZone **   
The Amazon EC2 Availability Zone in which to restore the cluster.  
Default: A random, system-chosen Availability Zone.  
Example: `us-east-2a`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AvailabilityZoneRelocation **   
The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is restored.  
Type: Boolean  
Required: No

 ** CatalogName **   
The name of the AWS Glue Data Catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.  
Constraints:  
+ Must contain at least one lowercase letter.
+ Can only contain lowercase letters (a-z), numbers (0-9), underscores (\_), and hyphens (-).
Pattern: `^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$`   
Example: `my-catalog_01`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$`   
Required: No

 ** ClusterParameterGroupName **   
The name of the parameter group to be associated with this cluster.  
Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to [Working with Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html).  
Constraints:  
+ Must be 1 to 255 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **ClusterSecurityGroups.ClusterSecurityGroupName.N**   
A list of security groups to be associated with this cluster.  
Default: The default cluster security group for Amazon Redshift.  
Cluster security groups only apply to clusters outside of VPCs.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterSubnetGroupName **   
The name of the subnet group where you want to cluster restored.  
A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DefaultIamRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified while it was restored from a snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ElasticIp **   
The Elastic IP (EIP) address for the cluster. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Encrypted **   
Enables support for restoring an unencrypted snapshot to a cluster encrypted with AWS Key Management Service (KMS) and a customer managed key.  
Type: Boolean  
Required: No

 ** EnhancedVpcRouting **   
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.  
If this option is `true`, enhanced VPC routing is enabled.   
Default: false  
Type: Boolean  
Required: No

 ** HsmClientCertificateIdentifier **   
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** HsmConfigurationIdentifier **   
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **IamRoles.IamRoleArn.N**   
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format.   
The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to [Quotas and limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** IpAddressType **   
The IP address type for the cluster. Possible values are `ipv4` and `dualstack`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** KmsKeyId **   
The AWS Key Management Service (KMS) key ID of the encryption key that encrypts data in the cluster restored from a shared snapshot. You can also provide the key ID when you restore from an unencrypted snapshot to an encrypted cluster in the same account. Additionally, you can specify a new KMS key ID when you restore from an encrypted snapshot in the same account in order to change it. In that case, the restored cluster is encrypted with the new KMS key ID.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaintenanceTrackName **   
The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the `MaintenanceTrack` value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ManageMasterPassword **   
If `true`, Amazon Redshift uses AWS Secrets Manager to manage the restored cluster's admin credentials. If `ManageMasterPassword` is false or not set, Amazon Redshift uses the admin credentials the cluster had at the time the snapshot was taken.  
Type: Boolean  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.  
The value must be either -1 or an integer between 1 and 3,653.  
Type: Integer  
Required: No

 ** MasterPasswordSecretKmsKeyId **   
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if `ManageMasterPassword` is true.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MultiAZ **   
If true, the snapshot will be restored to a cluster deployed in two Availability Zones.  
Type: Boolean  
Required: No

 ** NodeType **   
The node type that the restored cluster will be provisioned with.  
If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc2.large node type into another dc2 type. For more information about node types, see [ About Clusters and Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes) in the *Amazon Redshift Cluster Management Guide*.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The number of nodes specified when provisioning the restored cluster.  
Type: Integer  
Required: No

 ** OwnerAccount **   
The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Port **   
The port number on which the cluster accepts connections.  
Default: The same port as the original cluster.  
Valid values: For clusters with DC2 nodes, must be within the range `1150`-`65535`. For clusters with RG or RA3 nodes, must be within the ranges `5431`-`5455` or `8191`-`8215`.  
Type: Integer  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range (in UTC) during which automated cluster maintenance can occur.  
 Format: `ddd:hh24:mi-ddd:hh24:mi`   
 Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see [Maintenance Windows](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows) in Amazon Redshift Cluster Management Guide.   
Valid Days: Mon \| Tue \| Wed \| Thu \| Fri \| Sat \| Sun  
Constraints: Minimum 30-minute window.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PubliclyAccessible **   
If `true`, the cluster can be accessed from a public network.   
Default: false  
Type: Boolean  
Required: No

 ** RedshiftIdcApplicationArn **   
The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling AWS IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ReservedNodeId **   
The identifier of the target reserved node offering.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotArn **   
The Amazon Resource Name (ARN) of the snapshot associated with the message to restore from a cluster. You must specify this parameter or `snapshotIdentifier`, but not both.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotClusterIdentifier **   
The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than \* for the cluster name.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotIdentifier **   
The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. You must specify this parameter or `snapshotArn`, but not both.  
Example: `my-snapshot-id`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotScheduleIdentifier **   
A unique identifier for the snapshot schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** TargetReservedNodeOfferingId **   
The identifier of the target reserved node offering.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.  
Default: The default VPC security group is associated with the cluster.  
VPC security groups only apply to clusters in VPCs.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_RestoreFromClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_RestoreFromClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessToSnapshotDenied **   
The owner of the specified snapshot has not authorized your account to access the snapshot.  
HTTP Status Code: 400

 ** ClusterAlreadyExists **   
The account already has a cluster with the given identifier.  
HTTP Status Code: 400

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** ClusterQuotaExceeded **   
The request would exceed the allowed number of cluster instances for this account. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** ClusterSubnetGroupNotFoundFault **   
The cluster subnet group name does not refer to an existing cluster subnet group.  
HTTP Status Code: 400

 ** DependentServiceAccessDenied **   
A dependent service denied access for the integration.  
HTTP Status Code: 403

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** HsmClientCertificateNotFoundFault **   
There is no Amazon Redshift HSM client certificate with the specified identifier.  
HTTP Status Code: 400

 ** HsmConfigurationNotFoundFault **   
There is no Amazon Redshift HSM configuration with the specified identifier.  
HTTP Status Code: 400

 ** InsufficientClusterCapacity **   
The number of nodes specified exceeds the allotted capacity of the cluster.  
HTTP Status Code: 400

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** InvalidClusterSubnetGroupStateFault **   
The cluster subnet group cannot be deleted because it is in use.  
HTTP Status Code: 400

 ** InvalidClusterTrack **   
The provided cluster track name is not valid.  
HTTP Status Code: 400

 ** InvalidElasticIpFault **   
The Elastic IP (EIP) is invalid or cannot be found.  
HTTP Status Code: 400

 ** InvalidReservedNodeState **   
Indicates that the Reserved Node being exchanged is not in an active state.  
HTTP Status Code: 400

 ** InvalidRestore **   
The restore is invalid.  
HTTP Status Code: 406

 ** InvalidSubnet **   
The requested subnet is not valid, or not all of the subnets are in the same VPC.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The cluster subnet group does not cover all Availability Zones.  
HTTP Status Code: 400

 ** Ipv6CidrBlockNotFoundFault **   
There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.  
HTTP Status Code: 400

 ** LimitExceededFault **   
The encryption key has exceeded its grant limit in AWS KMS.  
HTTP Status Code: 400

 ** NumberOfNodesPerClusterLimitExceeded **   
The operation would exceed the number of nodes allowed for a cluster.  
HTTP Status Code: 400

 ** NumberOfNodesQuotaExceeded **   
The operation would exceed the number of nodes allotted to the account. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** RedshiftIdcApplicationNotExists **   
The application you attempted to find doesn't exist.  
HTTP Status Code: 404

 ** ReservedNodeAlreadyExists **   
User already has a reservation with the given identifier.  
HTTP Status Code: 404

 ** ReservedNodeAlreadyMigrated **   
Indicates that the reserved node has already been exchanged.  
HTTP Status Code: 400

 ** ReservedNodeNotFound **   
The specified reserved compute node not found.  
HTTP Status Code: 404

 ** ReservedNodeOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

 ** SnapshotScheduleNotFound **   
We could not find the specified snapshot schedule.   
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_RestoreFromClusterSnapshot_Examples"></a>

### Example
<a name="API_RestoreFromClusterSnapshot_Example_1"></a>

This example illustrates one usage of RestoreFromClusterSnapshot.

#### Sample Request
<a name="API_RestoreFromClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=RestoreFromClusterSnapshot
&ClusterIdentifier=mycluster
&SnapshotIdentifier=mysnapshotid
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_RestoreFromClusterSnapshot_Example_1_Response"></a>

```
<RestoreFromClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <RestoreFromClusterSnapshotResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ClusterSecurityGroups/>
      <NodeType>rg.4xlarge</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-29T23:15:00Z</NextMaintenanceWindowStartTime>
      <DeferredMaintenanceWindows/>
      <Tags/>
      <VpcSecurityGroups>
        <VpcSecurityGroup>
          <VpcSecurityGroupId>sh-a1a123ab</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroup>
      </VpcSecurityGroups>
      <ClusterParameterGroups>
        <ClusterParameterGroup>
          <ParameterGroupName>default.redshift-1.0</ParameterGroupName>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
        </ClusterParameterGroup>
      </ClusterParameterGroups>
      <Encrypted>false</Encrypted>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <PendingModifiedValues/>
      <PreferredMaintenanceWindow>sun:23:15-sun:23:45</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>creating</ClusterStatus>
    </Cluster>
  </RestoreFromClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>56190ef5-28f6-11ea-8a28-2fd1719d0e86</RequestId>
  </ResponseMetadata>
</RestoreFromClusterSnapshotResponse>
```

## See Also
<a name="API_RestoreFromClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RestoreFromClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RestoreFromClusterSnapshot) 