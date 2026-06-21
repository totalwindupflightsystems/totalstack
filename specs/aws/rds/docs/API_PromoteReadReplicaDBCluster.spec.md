---
id: "@specs/aws/rds/docs/API_PromoteReadReplicaDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PromoteReadReplicaDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# PromoteReadReplicaDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_PromoteReadReplicaDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PromoteReadReplicaDBCluster
<a name="API_PromoteReadReplicaDBCluster"></a>

Promotes a read replica DB cluster to a standalone DB cluster.

## Request Parameters
<a name="API_PromoteReadReplicaDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier of the DB cluster read replica to promote. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing DB cluster read replica.
Example: `my-cluster-replica1`   
Type: String  
Required: Yes

## Response Elements
<a name="API_PromoteReadReplicaDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_PromoteReadReplicaDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_PromoteReadReplicaDBCluster_Examples"></a>

### Example
<a name="API_PromoteReadReplicaDBCluster_Example_1"></a>

This example illustrates one usage of PromoteReadReplicaDBCluster.

#### Sample Request
<a name="API_PromoteReadReplicaDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=PromoteReadReplicaDBCluster
   &DBClusterIdentifier=my-cluster-replica1
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20160328/us-east-1/rds/aws4_request
   &X-Amz-Date=20160328T221226Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=e2b2cfc3db7766b6ef86922f664e05ab306754e30e408d9fd3c8e58069a9b386
```

#### Sample Response
<a name="API_PromoteReadReplicaDBCluster_Example_1_Response"></a>

```
<PromoteReadReplicaDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <PromoteReadReplicaDBClusterResult>
    <DBCluster>
      <Port>3306</Port>
      <Engine>aurora</Engine>
      <Status>creating</Status>
      <BackupRetentionPeriod>1</BackupRetentionPeriod>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <Status>active</Status>
          <VpcSecurityGroupId>sg-2103dc23</VpcSecurityGroupId>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <DBSubnetGroup>default</DBSubnetGroup>
      <EngineVersion>5.6.10a</EngineVersion>
      <Endpoint>sample-cluster.cluster-ctrayan0rynq.us-east-1.rds.amazonaws.com</Endpoint>
      <DBClusterParameterGroup>default.aurora5.6</DBClusterParameterGroup>
      <AvailabilityZones>
        <AvailabilityZone>us-east-1a</AvailabilityZone>
        <AvailabilityZone>us-east-1c</AvailabilityZone>
        <AvailabilityZone>us-east-1e</AvailabilityZone>
      </AvailabilityZones>
      <DBClusterIdentifier>my-cluster-replica1</DBClusterIdentifier>
      <PreferredBackupWindow>04:22-04:52</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:06:44-fri:07:14</PreferredMaintenanceWindow>
        <DBClusterMembers>
          <DBClusterMember>
            <IsClusterWriter>true</IsClusterWriter>
            <DBInstanceIdentifier>my-cluster1-master</DBInstanceIdentifier>
          </DBClusterMember>
          <DBClusterMember>
            <IsClusterWriter>false</IsClusterWriter>
            <DBInstanceIdentifier>my-cluster1-read1</DBInstanceIdentifier>
          </DBClusterMember>
        </DBClusterMembers>
      <AllocatedStorage>1</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
    </DBCluster>
  </PromoteReadReplicaDBClusterResult>
  <ResponseMetadata>
    <RequestId>8e8c0d64-be21-11d3-a71c-13dc2f771e41</RequestId>
  </ResponseMetadata>
</PromoteReadReplicaDBClusterResponse>
```

## See Also
<a name="API_PromoteReadReplicaDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/PromoteReadReplicaDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PromoteReadReplicaDBCluster) 