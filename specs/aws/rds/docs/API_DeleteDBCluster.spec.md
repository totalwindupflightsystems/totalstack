---
id: "@specs/aws/rds/docs/API_DeleteDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBCluster
<a name="API_DeleteDBCluster"></a>

The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.

If you're deleting a Multi-AZ DB cluster with read replicas, all cluster members are terminated and read replicas are promoted to standalone instances.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DeleteDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.  
Constraints:  
+ Must match an existing DBClusterIdentifier.
Type: String  
Required: Yes

 ** DeleteAutomatedBackups **   
Specifies whether to remove automated backups immediately after the DB cluster is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB cluster is deleted, unless the AWS Backup policy specifies a point-in-time restore rule.  
Type: Boolean  
Required: No

 ** FinalDBSnapshotIdentifier **   
The DB cluster snapshot identifier of the new DB cluster snapshot created when `SkipFinalSnapshot` is disabled.  
If you specify this parameter and also skip the creation of a final DB cluster snapshot with the `SkipFinalShapshot` parameter, the request results in an error.
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Type: String  
Required: No

 ** SkipFinalSnapshot **   
Specifies whether to skip the creation of a final DB cluster snapshot before RDS deletes the DB cluster. If you set this value to `true`, RDS doesn't create a final DB cluster snapshot. If you set this value to `false` or don't specify it, RDS creates a DB cluster snapshot before it deletes the DB cluster. By default, this parameter is disabled, so RDS creates a final DB cluster snapshot.  
If `SkipFinalSnapshot` is disabled, you must specify a value for the `FinalDBSnapshotIdentifier` parameter.
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_DeleteDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAutomatedBackupQuotaExceededFault **   
The quota for retained automated backups was exceeded. This prevents you from retaining any additional automated backups. The retained automated backups quota is the same as your DB cluster quota.  
HTTP Status Code: 400

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterSnapshotAlreadyExistsFault **   
The user already has a DB cluster snapshot with the given identifier.  
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **   
The supplied value isn't a valid DB cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The global cluster is in an invalid state and can't perform the requested operation.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB snapshots.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBCluster_Examples"></a>

### Deleting an Aurora DB cluster
<a name="API_DeleteDBCluster_Example_1"></a>

This example illustrates one usage of DeleteDBCluster.

#### Sample Request
<a name="API_DeleteDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=DeleteDBCluster
    &DBClusterIdentifier=sample-cluster2
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140725/us-east-1/rds/aws4_request
    &X-Amz-Date=20140725T162148Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=815910f78c5a9813e1c15300fcf206e04da071b3586770169765292dc6aa2ed4
```

#### Sample Response
<a name="API_DeleteDBCluster_Example_1_Response"></a>

```
<DeleteDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteDBClusterResult>
    <DBCluster>
      <Engine>aurora5.6</Engine>
      <Status>available</Status>
      <BackupRetentionPeriod>0</BackupRetentionPeriod>
      <DBSubnetGroup>my-subgroup</DBSubnetGroup>
      <EngineVersion>5.6.10a</EngineVersion>
      <Endpoint>sample-cluster2.cluster-cbfvmgb0y5fy.us-east-1.rds.amazonaws.com</Endpoint>
      <DBClusterIdentifier>sample-cluster2</DBClusterIdentifier>
      <PreferredBackupWindow>04:45-05:15</PreferredBackupWindow>
      <PreferredMaintenanceWindow>sat:05:56-sat:06:26</PreferredMaintenanceWindow>
      <DBClusterMembers/>
      <AllocatedStorage>15</AllocatedStorage>
      <MasterUsername>awsuser</MasterUsername>
    </DBCluster>
  </DeleteDBClusterResult>
  <ResponseMetadata>
    <RequestId>c72118dc-1417-11e4-8c7b-931a6c1fef28</RequestId>
  </ResponseMetadata>
</DeleteDBClusterResponse>
```

### Deleting a Multi-AZ DB cluster
<a name="API_DeleteDBCluster_Example_2"></a>

This example illustrates one usage of DeleteDBCluster.

#### Sample Request
<a name="API_DeleteDBCluster_Example_2_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DeleteDBCluster
    &DBClusterIdentifier=my-multi-az-cluster
    &SkipFinalSnapshot=true
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140725/us-west-2/rds/aws4_request
    &X-Amz-Date=20211027T000821Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=815910f78c5a9813e1c15300fcf206e04da071b3586770169765292dc6aa2ed4
```

#### Sample Response
<a name="API_DeleteDBCluster_Example_2_Response"></a>

```
<DeleteDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteDBClusterResult>
    <DBCluster>
      <CrossAccountClone>false</CrossAccountClone>
      <AllocatedStorage>1000</AllocatedStorage>
      <AssociatedRoles />
      <AvailabilityZones />
      <ReadReplicaIdentifiers />
      <EngineVersion>8.0.26</EngineVersion>
      <MasterUsername>admin</MasterUsername>
      <DBClusterMembers />
      <HttpEndpointEnabled>false</HttpEndpointEnabled>
      <Port>3066</Port>
      <MonitoringInterval>0</MonitoringInterval>
      <BackupRetentionPeriod>1</BackupRetentionPeriod>
      <DBClusterIdentifier>my-multi-az-cluster</DBClusterIdentifier>
      <DbClusterResourceId>cluster-XDHARXDLDCRL2VZZXKBCFN3RQI</DbClusterResourceId>
      <LatestRestorableTime>2021-08-17T23:15:00Z</LatestRestorableTime>
      <Status>available</Status>
      <PreferredBackupWindow>22:02-22:32</PreferredBackupWindow>
      <DeletionProtection>false</DeletionProtection>
      <Endpoint>my-multi-az-cluster.cluster-123456789012.us-west-2.rds.amazonaws.com</Endpoint>
      <EngineMode>provisioned</EngineMode>
      <Engine>mysql</Engine>
      <ReaderEndpoint>my-multi-az-cluster.cluster-ro-123456789012.us-west-2.rds.amazonaws.com</ReaderEndpoint>
      <PubliclyAccessible>true</PubliclyAccessible>
      <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
      <EarliestRestorableTime>2021-08-16T23:15:00Z</EarliestRestorableTime>
      <ClusterCreateTime>2021-08-10T23:02:10.460Z</ClusterCreateTime>
      <PerformanceInsightsEnabled>false</PerformanceInsightsEnabled>
      <MultiAZ>false</MultiAZ>
      <DomainMemberships />
      <StorageEncrypted>false</StorageEncrypted>
      <DBSubnetGroup>subnetgroup1</DBSubnetGroup>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <VpcSecurityGroupId>sg-6921cc28</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <TagList />
      <HostedZoneId>Z3GZ3VYA3PGHTQ</HostedZoneId>
      <PreferredMaintenanceWindow>mon:23:02-mon:23:32</PreferredMaintenanceWindow>
      <DBClusterParameterGroup>default.mysql8.0</DBClusterParameterGroup>
      <StorageType>io1</StorageType>
      <DBClusterInstanceClass>db.r6gd.xlarge</DBClusterInstanceClass>
      <CopyTagsToSnapshot>false</CopyTagsToSnapshot>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:my-multi-az-cluster</DBClusterArn>
    </DBCluster>
  </DeleteDBClusterResult>
  <ResponseMetadata>
    <RequestId>08b84e67-7e89-4302-8563-642b34026159</RequestId>
  </ResponseMetadata>
</DeleteDBClusterResponse>
```

## See Also
<a name="API_DeleteDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBCluster) 