---
id: "@specs/aws/redshift/docs/API_DeleteCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCluster
<a name="API_DeleteCluster"></a>

Deletes a previously provisioned cluster without its final snapshot being created. A successful response from the web service indicates that the request was received correctly. Use [DescribeClusters](API_DescribeClusters.md) to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

If you want to shut down the cluster and retain it for future use, set *SkipFinalClusterSnapshot* to `false` and specify a name for *FinalClusterSnapshotIdentifier*. You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be "final-snapshot" while the snapshot is being taken, then it's "deleting" once Amazon Redshift begins deleting the cluster. 

 For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DeleteCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster to be deleted.  
Constraints:  
+ Must contain lowercase characters.
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** FinalClusterSnapshotIdentifier **   
The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, *SkipFinalClusterSnapshot* must be `false`.   
Constraints:  
+ Must be 1 to 255 alphanumeric characters.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** FinalClusterSnapshotRetentionPeriod **   
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.  
The value must be either -1 or an integer between 1 and 3,653.  
The default value is -1.  
Type: Integer  
Required: No

 ** SkipFinalClusterSnapshot **   
Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If `true`, a final cluster snapshot is not created. If `false`, a final cluster snapshot is created before the cluster is deleted.   
The *FinalClusterSnapshotIdentifier* parameter must be specified if *SkipFinalClusterSnapshot* is `false`.
Default: `false`   
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteCluster_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DeleteCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotAlreadyExists **   
The value specified as a snapshot identifier is already used by an existing snapshot.  
HTTP Status Code: 400

 ** ClusterSnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of cluster snapshots.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteCluster_Examples"></a>

### Example
<a name="API_DeleteCluster_Example_1"></a>

This example illustrates one usage of DeleteCluster.

#### Sample Request
<a name="API_DeleteCluster_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteCluster
&ClusterIdentifier=mycluster
&SkipFinalClusterSnapshot=true
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteCluster_Example_1_Response"></a>

```
<DeleteClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DeleteClusterResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>2</NumberOfNodes>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>
      <Endpoint>
        <Port>5439</Port>
        <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
      </Endpoint>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <ClusterCreateTime>2019-12-26T20:25:38.716Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ClusterSecurityGroups/>
      <NodeType>dc2.large</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-27T04:00:00Z</NextMaintenanceWindowStartTime>
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
      <Encrypted>true</Encrypted>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <PendingModifiedValues>
        <ClusterType>single-node</ClusterType>
        <NodeType>dc2.large</NodeType>
      </PendingModifiedValues>
      <PreferredMaintenanceWindow>fri:04:00-fri:04:30</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>deleting</ClusterStatus>
    </Cluster>
  </DeleteClusterResult>
  <ResponseMetadata>
    <RequestId>4b6dd471-2838-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</DeleteClusterResponse>
```

## See Also
<a name="API_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteCluster) 