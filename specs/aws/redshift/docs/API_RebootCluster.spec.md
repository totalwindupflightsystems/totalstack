---
id: "@specs/aws/redshift/docs/API_RebootCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RebootCluster"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RebootCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RebootCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RebootCluster
<a name="API_RebootCluster"></a>

Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to `rebooting`. A cluster event is created when the reboot is completed. Any pending cluster modifications (see [ModifyCluster](API_ModifyCluster.md)) are applied at this reboot. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*. 

## Request Parameters
<a name="API_RebootCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The cluster identifier.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_RebootCluster_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_RebootCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

## Examples
<a name="API_RebootCluster_Examples"></a>

### Example
<a name="API_RebootCluster_Example_1"></a>

This example illustrates one usage of RebootCluster.

#### Sample Request
<a name="API_RebootCluster_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=RebootCluster
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_RebootCluster_Example_1_Response"></a>

```
<RebootClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <RebootClusterResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
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
      <ClusterSecurityGroups/>
      <NodeType>dc2.large</NodeType>
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
      <PendingModifiedValues/>
      <PreferredMaintenanceWindow>sun:23:15-mon:03:15</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>rebooting</ClusterStatus>
    </Cluster>
  </RebootClusterResult>
  <ResponseMetadata>
    <RequestId>6f1299dc-28f5-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</RebootClusterResponse>
```

## See Also
<a name="API_RebootCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RebootCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RebootCluster) 