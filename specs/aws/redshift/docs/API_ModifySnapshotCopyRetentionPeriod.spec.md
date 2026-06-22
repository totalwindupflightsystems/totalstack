---
id: "@specs/aws/redshift/docs/API_ModifySnapshotCopyRetentionPeriod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifySnapshotCopyRetentionPeriod"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifySnapshotCopyRetentionPeriod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifySnapshotCopyRetentionPeriod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifySnapshotCopyRetentionPeriod
<a name="API_ModifySnapshotCopyRetentionPeriod"></a>

Modifies the number of days to retain snapshots in the destination AWS Region after they are copied from the source AWS Region. By default, this operation only changes the retention period of copied automated snapshots. The retention periods for both new and existing copied automated snapshots are updated with the new retention period. You can set the manual option to change only the retention periods of copied manual snapshots. If you set this option, only newly copied manual snapshots have the new retention period. 

## Request Parameters
<a name="API_ModifySnapshotCopyRetentionPeriod_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination AWS Region.  
Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** RetentionPeriod **   
The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region.  
By default, this only changes the retention period of copied automated snapshots.   
If you decrease the retention period for automated snapshots that are copied to a destination AWS Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.  
Constraints: Must be at least 1 and no more than 35 for automated snapshots.   
If you specify the `manual` option, only newly copied manual snapshots will have the new retention period.   
If you specify the value of -1 newly copied manual snapshots are retained indefinitely.  
Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.  
Type: Integer  
Required: Yes

 ** Manual **   
Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_ModifySnapshotCopyRetentionPeriod_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_ModifySnapshotCopyRetentionPeriod_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

 ** SnapshotCopyDisabledFault **   
Cross-region snapshot copy was temporarily disabled. Try your request again.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_ModifySnapshotCopyRetentionPeriod_Examples"></a>

### Example
<a name="API_ModifySnapshotCopyRetentionPeriod_Example_1"></a>

This example illustrates one usage of ModifySnapshotCopyRetentionPeriod.

#### Sample Request
<a name="API_ModifySnapshotCopyRetentionPeriod_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifySnapshotCopyRetentionPeriod
&ClusterIdentifier=mycluster
&RetentionPeriod=15
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifySnapshotCopyRetentionPeriod_Example_1_Response"></a>

```
<ModifySnapshotCopyRetentionPeriodResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifySnapshotCopyRetentionPeriodResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>
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
      <ClusterStatus>available</ClusterStatus>
    </Cluster>
  </ModifySnapshotCopyRetentionPeriodResult>
  <ResponseMetadata>
    <RequestId>f24fc770-28f3-11ea-9467-b9a67a99da45</RequestId>
  </ResponseMetadata>
</ModifySnapshotCopyRetentionPeriodResponse>
```

## See Also
<a name="API_ModifySnapshotCopyRetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod) 