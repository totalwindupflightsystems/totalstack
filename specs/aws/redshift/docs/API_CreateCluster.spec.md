---
id: "@specs/aws/redshift/docs/API_CreateCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCluster
<a name="API_CreateCluster"></a>

Creates a new cluster with the specified parameters.

To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:
+ Creating a public cluster
+ Restoring a public cluster
+ Modifying a private cluster to be public
+ Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ Alphabetic characters must be lowercase.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique for all clusters within an AWS account.
Example: `myexamplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** MasterUsername **   
The user name associated with the admin user account for the cluster that is being created.  
Constraints:  
+ Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be `PUBLIC`.
+ Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
+ The first character must be a letter.
+ Must not contain a colon (:) or a slash (/).
+ Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide. 
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** NodeType **   
The node type to be provisioned for the cluster. For information about node types, go to [ Working with Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes) in the *Amazon Redshift Cluster Management Guide*.   
Valid Values: `dc2.large` \| `dc2.8xlarge`\| `rg.xlarge` \| `rg.4xlarge` \| `ra3.large` \| `ra3.xlplus` \| `ra3.4xlarge` \| `ra3.16xlarge`   
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
When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.  
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
Default: `1`   
Constraints: Must be a value from 0 to 35.  
Type: Integer  
Required: No

 ** AvailabilityZone **   
The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.  
Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.  
Example: `us-east-2d`   
Constraint: The specified Availability Zone must be in the same region as the current endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AvailabilityZoneRelocation **   
The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.  
Type: Boolean  
Required: No

 ** CatalogName **   
The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.  
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
Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to [Working with Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html)   
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
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterSubnetGroupName **   
The name of a cluster subnet group to be associated with this cluster.  
If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterType **   
The type of the cluster. When cluster type is specified as  
+  `single-node`, the **NumberOfNodes** parameter is not required.
+  `multi-node`, the **NumberOfNodes** parameter is required.
Valid Values: `multi-node` \| `single-node`   
Default: `multi-node`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The version of the Amazon Redshift engine software that you want to deploy on the cluster.  
The version selected runs on all the nodes in the cluster.  
Constraints: Only version 1.0 is currently available.  
Example: `1.0`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DBName **   
The name of the first database to be created when the cluster is created.  
To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to [Create a Database](https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html) in the Amazon Redshift Database Developer Guide.   
Default: `dev`   
Constraints:  
+ Must contain 1 to 64 alphanumeric characters.
+ Must contain only lowercase letters.
+ Cannot be a word that is reserved by the service. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide. 
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DefaultIamRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was created.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ElasticIp **   
The Elastic IP (EIP) address for the cluster.  
Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to [Supported Platforms to Launch Your Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms) in the Amazon Redshift Cluster Management Guide.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Encrypted **   
If `true`, the data in the cluster is encrypted at rest. If you set the value on this parameter to `false`, the request will fail.  
Default: true  
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

 **IamRoles.IamRoleArn.N**   
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format.   
The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to [Quotas and limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.  
Type: Array of strings  
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

 ** LoadSampleData **   
A flag that specifies whether to load sample data once the cluster is created.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaintenanceTrackName **   
An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the `current` track.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ManageMasterPassword **   
If `true`, Amazon Redshift uses AWS Secrets Manager to manage this cluster's admin credentials. You can't use `MasterUserPassword` if `ManageMasterPassword` is true. If `ManageMasterPassword` is false or not set, Amazon Redshift uses `MasterUserPassword` for the admin user account's password.   
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

 ** MasterUserPassword **   
The password associated with the admin user account for the cluster that is being created.  
You can't use `MasterUserPassword` if `ManageMasterPassword` is `true`.  
Constraints:  
+ Must be between 8 and 64 characters in length.
+ Must contain at least one uppercase letter.
+ Must contain at least one lowercase letter.
+ Must contain one number.
+ Can be any printable ASCII character (ASCII code 33-126) except `'` (single quote), `"` (double quote), `\`, `/`, or `@`.
Type: String  
Required: No

 ** MultiAZ **   
If true, Amazon Redshift will deploy the cluster in two Availability Zones (AZ).  
Type: Boolean  
Required: No

 ** NumberOfNodes **   
The number of compute nodes in the cluster. This parameter is required when the **ClusterType** parameter is specified as `multi-node`.   
For information about determining how many nodes you need, go to [ Working with Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes) in the *Amazon Redshift Cluster Management Guide*.   
If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.  
Default: `1`   
Constraints: Value must be at least 1 and no more than 100.  
Type: Integer  
Required: No

 ** Port **   
The port number on which the cluster accepts incoming connections.  
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.  
Default: `5439`   
Valid Values:   
+ For clusters with RG or RA3 nodes - Select a port within the ranges `5431-5455` or `8191-8215`. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)
+ For clusters with dc2 nodes - Select a port within the range `1150-65535`.
Type: Integer  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range (in UTC) during which automated cluster maintenance can occur.  
 Format: `ddd:hh24:mi-ddd:hh24:mi`   
 Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see [Maintenance Windows](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows) in Amazon Redshift Cluster Management Guide.  
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
The Amazon resource name (ARN) of the Amazon Redshift IAM Identity Center application.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotScheduleIdentifier **   
A unique identifier for the snapshot schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.  
Default: The default VPC security group is associated with the cluster.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_CreateCluster_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_CreateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidClusterSubnetGroupStateFault **   
The cluster subnet group cannot be deleted because it is in use.  
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
<a name="API_CreateCluster_Examples"></a>

### Example
<a name="API_CreateCluster_Example_1"></a>

This example illustrates one usage of CreateCluster.

#### Sample Request
<a name="API_CreateCluster_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateCluster
&ClusterIdentifier=mycluster
&NodeType=rg.4xlarge
&MasterUsername=adminuser
&MasterUserPassword=A1b2c3d4
&NumberOfNodes=2
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateCluster_Example_1_Response"></a>

```
<CreateClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateClusterResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>2</NumberOfNodes>
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
      <NextMaintenanceWindowStartTime>2019-12-27T04:00:00Z</NextMaintenanceWindowStartTime>
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
      <Encrypted>true</Encrypted>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <PendingModifiedValues>
        <MasterUserPassword>****</MasterUserPassword>
      </PendingModifiedValues>
      <PreferredMaintenanceWindow>fri:04:00-fri:04:30</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>creating</ClusterStatus>
    </Cluster>
  </CreateClusterResult>
  <ResponseMetadata>
    <RequestId>61a11272-281d-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</CreateClusterResponse>
```

## See Also
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateCluster) 