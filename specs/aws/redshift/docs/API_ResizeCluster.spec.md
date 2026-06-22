---
id: "@specs/aws/redshift/docs/API_ResizeCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResizeCluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ResizeCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ResizeCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResizeCluster
<a name="API_ResizeCluster"></a>

Changes the size of the cluster. You can change the cluster's type, or change the number or type of nodes. The default behavior is to use the elastic resize method. With an elastic resize, your cluster is available for read and write operations more quickly than with the classic resize method. 

Elastic resize operations have the following restrictions:
+ You can only resize clusters of the following types:
  + dc2.large
  + dc2.8xlarge
  + rg.xlarge
  + rg.4xlarge
  + ra3.large
  + ra3.xlplus
  + ra3.4xlarge
  + ra3.16xlarge
+ The type of nodes that you add must match the node type for the cluster.

## Request Parameters
<a name="API_ResizeCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier for the cluster to resize.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Classic **   
A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to `false`, the resize type is elastic.   
Type: Boolean  
Required: No

 ** ClusterType **   
The new cluster type for the specified cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NodeType **   
The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.  
Type: Integer  
Required: No

 ** ReservedNodeId **   
The identifier of the reserved node.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** TargetReservedNodeOfferingId **   
The identifier of the target reserved node offering.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_ResizeCluster_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_ResizeCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** InsufficientClusterCapacity **   
The number of nodes specified exceeds the allotted capacity of the cluster.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidReservedNodeState **   
Indicates that the Reserved Node being exchanged is not in an active state.  
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
<a name="API_ResizeCluster_Examples"></a>

### Example
<a name="API_ResizeCluster_Example_1"></a>

This example illustrates one usage of ResizeCluster.

#### Sample Request
<a name="API_ResizeCluster_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ResizeCluster
&ClusterIdentifier=mycluster
&ClusterType=multi-node
&NodeType=rg.4xlarge
&NumberOfNodes=6
&Classic=true
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ResizeCluster_Example_1_Response"></a>

```
<ResizeClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResizeClusterResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <AvailabilityZone>us-east-2d</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>
      <Endpoint>
        <Port>5439</Port>
        <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
      </Endpoint>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <ClusterCreateTime>2019-12-27T17:48:01.504Z</ClusterCreateTime>
      <ClusterSnapshotCopyStatus>
        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
        <DestinationRegion>us-east-1</DestinationRegion>
        <RetentionPeriod>15</RetentionPeriod>
      </ClusterSnapshotCopyStatus>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ResizeInfo>
        <AllowCancelResize>true</AllowCancelResize>
        <ResizeType>ClassicResize</ResizeType>
      </ResizeInfo>
      <ClusterSecurityGroups/>
      <NodeType>rg.4xlarge</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2020-01-26T23:15:00Z</NextMaintenanceWindowStartTime>
      <DeferredMaintenanceWindows>
        <DeferredMaintenanceWindow>
          <DeferMaintenanceEndTime>2020-01-26T19:39:15.075Z</DeferMaintenanceEndTime>
          <DeferMaintenanceIdentifier>dfm-VcfYqSYqQ4tdXOqbKwOo</DeferMaintenanceIdentifier>
          <DeferMaintenanceStartTime>2019-12-27T19:39:15.075Z</DeferMaintenanceStartTime>
        </DeferredMaintenanceWindow>
      </DeferredMaintenanceWindows>
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
      <PendingModifiedValues>
        <ClusterType>multi-node</ClusterType>
        <NumberOfNodes>6</NumberOfNodes>
        <NodeType>rg.4xlarge</NodeType>
      </PendingModifiedValues>
      <PreferredMaintenanceWindow>sun:23:15-mon:03:15</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>resizing</ClusterStatus>
    </Cluster>
  </ResizeClusterResult>
  <ResponseMetadata>
    <RequestId>d504c6c0-28f5-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</ResizeClusterResponse>
```

## See Also
<a name="API_ResizeCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ResizeCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ResizeCluster) 