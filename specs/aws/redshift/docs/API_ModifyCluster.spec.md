---
id: "@specs/aws/redshift/docs/API_ModifyCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyCluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyCluster
<a name="API_ModifyCluster"></a>

Modifies the settings for a cluster.

You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.

You can add another security or parameter group, or change the admin user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:
+ Creating a public cluster
+ Restoring a public cluster
+ Modifying a private cluster to be public
+ Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_ModifyCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster to be modified.  
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AllowVersionUpgrade **   
If `true`, major version upgrades will be applied automatically to the cluster during the maintenance window.   
Default: `false`   
Type: Boolean  
Required: No

 ** AutomatedSnapshotRetentionPeriod **   
The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with [CreateClusterSnapshot](API_CreateClusterSnapshot.md).   
If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.  
You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.  
Default: Uses existing setting.  
Constraints: Must be a value from 0 to 35.  
Type: Integer  
Required: No

 ** AvailabilityZone **   
The option to initiate relocation for an Amazon Redshift cluster to the target Availability Zone.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AvailabilityZoneRelocation **   
The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.  
Type: Boolean  
Required: No

 ** ClusterParameterGroupName **   
The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use [RebootCluster](API_RebootCluster.md).   
Default: Uses existing setting.  
Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **ClusterSecurityGroups.ClusterSecurityGroupName.N**   
A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.  
Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.  
Constraints:  
+ Must be 1 to 255 alphanumeric characters or hyphens
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterType **   
The new cluster type.  
When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use [DescribeResize](API_DescribeResize.md) to track the progress of the resize request.   
Valid Values: ` multi-node | single-node `   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The new version number of the Amazon Redshift engine to upgrade to.  
For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.  
Example: `1.0`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ElasticIp **   
The Elastic IP (EIP) address for the cluster.  
Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to [Supported Platforms to Launch Your Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms) in the Amazon Redshift Cluster Management Guide.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Encrypted **   
Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the `KmsKeyId` parameter, we encrypt the cluster with the provided `KmsKeyId`. If you don't provide a `KmsKeyId`, we encrypt with the default key.   
If the value is not encrypted (false), then the cluster is decrypted.   
Type: Boolean  
Required: No

 ** EnhancedVpcRouting **   
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.  
If this option is `true`, enhanced VPC routing is enabled.   
Default: false  
Type: Boolean  
Required: No

 ** ExtraComputeForAutomaticOptimization **   
If `true`, allocates additional compute resources for running automatic optimization operations.  
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

 ** IpAddressType **   
The IP address types that the cluster supports. Possible values are `ipv4` and `dualstack`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** KmsKeyId **   
The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaintenanceTrackName **   
The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the `PendingModifiedValues` for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ManageMasterPassword **   
If `true`, Amazon Redshift uses AWS Secrets Manager to manage this cluster's admin credentials. You can't use `MasterUserPassword` if `ManageMasterPassword` is true. If `ManageMasterPassword` is false or not set, Amazon Redshift uses `MasterUserPassword` for the admin user account's password.   
Type: Boolean  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesn't retroactively change the retention periods of existing manual snapshots.  
The value must be either -1 or an integer between 1 and 3,653.  
The default value is -1.  
Type: Integer  
Required: No

 ** MasterPasswordSecretKmsKeyId **   
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if `ManageMasterPassword` is true.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MasterUserPassword **   
The new password for the cluster admin user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the `MasterUserPassword` element exists in the `PendingModifiedValues` element of the operation response.   
You can't use `MasterUserPassword` if `ManageMasterPassword` is `true`.  
Operations never return the password, so this operation provides a way to regain access to the admin user account for a cluster if the password is lost.
Default: Uses existing setting.  
Constraints:  
+ Must be between 8 and 64 characters in length.
+ Must contain at least one uppercase letter.
+ Must contain at least one lowercase letter.
+ Must contain one number.
+ Can be any printable ASCII character (ASCII code 33-126) except `'` (single quote), `"` (double quote), `\`, `/`, or `@`.
Type: String  
Required: No

 ** MultiAZ **   
If true and the cluster is currently only deployed in a single Availability Zone, the cluster will be modified to be deployed in two Availability Zones.  
Type: Boolean  
Required: No

 ** NewClusterIdentifier **   
The new identifier for the cluster.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ Alphabetic characters must be lowercase.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique for all clusters within an AWS account.
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NodeType **   
The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.  
 For more information about resizing clusters, go to [Resizing Clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html) in the *Amazon Redshift Cluster Management Guide*.  
Valid Values: `dc2.large` \| `dc2.8xlarge`\| `rg.xlarge` \| `rg.4xlarge` \| `ra3.large` \| `ra3.xlplus` \| `ra3.4xlarge` \| `ra3.16xlarge`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.  
 For more information about resizing clusters, go to [Resizing Clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html) in the *Amazon Redshift Cluster Management Guide*.  
Valid Values: Integer greater than `0`.  
Type: Integer  
Required: No

 ** Port **   
The option to change the port of an Amazon Redshift cluster.  
Valid Values:   
+ For clusters with RG or RA3 nodes - Select a port within the ranges `5431-5455` or `8191-8215`. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)
+ For clusters with dc2 nodes - Select a port within the range `1150-65535`.
Type: Integer  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.  
This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.  
Default: Uses existing setting.  
Format: ddd:hh24:mi-ddd:hh24:mi, for example `wed:07:30-wed:08:00`.  
Valid Days: Mon \| Tue \| Wed \| Thu \| Fri \| Sat \| Sun  
Constraints: Must be at least 30 minutes.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PubliclyAccessible **   
If `true`, the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.  
Default: false  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_ModifyCluster_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_ModifyCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterAlreadyExists **   
The account already has a cluster with the given identifier.  
HTTP Status Code: 400

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** CustomCnameAssociationFault **   
An error occurred when an attempt was made to change the custom domain association.  
HTTP Status Code: 400

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
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

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidClusterTrack **   
The provided cluster track name is not valid.  
HTTP Status Code: 400

 ** InvalidElasticIpFault **   
The Elastic IP (EIP) is invalid or cannot be found.  
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
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

 ** TableLimitExceeded **   
The number of tables in the cluster exceeds the limit for the requested new cluster node type.   
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

 ** UnsupportedOptionFault **   
A request option was specified that is not supported.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyCluster_Examples"></a>

### Example
<a name="API_ModifyCluster_Example_1"></a>

This example changes the weekly preferred maintenance window for a cluster to be the minimum four hour window starting Sundays at 11:15 PM, and ending Mondays at 3:15 AM.

#### Sample Request
<a name="API_ModifyCluster_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyCluster
&ClusterIdentifier=mycluster
&PreferredMaintenanceWindow=Sun%3A23%3A15-Mon%3A03%3A15
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyCluster_Example_1_Response"></a>

```
<ModifyClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyClusterResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ExpectedNextSnapshotScheduleTimeStatus>OnTrack</ExpectedNextSnapshotScheduleTimeStatus>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>
      <Endpoint>
        <Port>5439</Port>
        <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
      </Endpoint>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <ClusterCreateTime>2019-12-27T17:48:01.504Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ClusterSecurityGroups/>
      <ExpectedNextSnapshotScheduleTime>2019-12-28T05:48:20.939Z</ExpectedNextSnapshotScheduleTime>
      <NodeType>rg.4xlarge</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-29T23:15:00Z</NextMaintenanceWindowStartTime>
      <DeferredMaintenanceWindows/>
      <Tags>
        <Tag>
          <Value>newtag</Value>
          <Key>mytag</Key>
        </Tag>
      </Tags>
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
      <PreferredMaintenanceWindow>sun:23:15-mon:03:15</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>available</ClusterStatus>
    </Cluster>
  </ModifyClusterResult>
  <ResponseMetadata>
    <RequestId>819eaffd-28df-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</ModifyClusterResponse>
```

## See Also
<a name="API_ModifyCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyCluster) 