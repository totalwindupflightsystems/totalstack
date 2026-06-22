---
id: "@specs/aws/redshift/docs/API_DisableSnapshotCopy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisableSnapshotCopy"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DisableSnapshotCopy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DisableSnapshotCopy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisableSnapshotCopy
<a name="API_DisableSnapshotCopy"></a>

Disables the automatic copying of snapshots from one region to another region for a specified cluster.

If your cluster and its snapshots are encrypted using an encrypted symmetric key from AWS Key Management Service, use [DeleteSnapshotCopyGrant](API_DeleteSnapshotCopyGrant.md) to delete the grant that grants Amazon Redshift permission to the key in the destination region. 

## Request Parameters
<a name="API_DisableSnapshotCopy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.  
Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_DisableSnapshotCopy_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DisableSnapshotCopy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** SnapshotCopyAlreadyDisabledFault **   
The cluster already has cross-region snapshot copy disabled.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_DisableSnapshotCopy_Examples"></a>

### Example
<a name="API_DisableSnapshotCopy_Example_1"></a>

This example illustrates one usage of DisableSnapshotCopy.

#### Sample Request
<a name="API_DisableSnapshotCopy_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DisableSnapshotCopy
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
<a name="API_DisableSnapshotCopy_Example_1_Response"></a>

```
<DisableSnapshotCopyResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DisableSnapshotCopyResult>
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
      <NodeType>dc2.large</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-29T05:30:00Z</NextMaintenanceWindowStartTime>
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
      <PreferredMaintenanceWindow>sun:05:30-sun:06:00</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>available</ClusterStatus>
    </Cluster>
  </DisableSnapshotCopyResult>
  <ResponseMetadata>
    <RequestId>7ec20f61-28da-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</DisableSnapshotCopyResponse>
```

## See Also
<a name="API_DisableSnapshotCopy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DisableSnapshotCopy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DisableSnapshotCopy) 