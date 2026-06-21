---
id: "@specs/aws/rds/docs/API_RebootDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RebootDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RebootDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RebootDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RebootDBCluster
<a name="API_RebootDBCluster"></a>

You might need to reboot your DB cluster, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB cluster parameter group associated with the DB cluster, reboot the DB cluster for the changes to take effect.

Rebooting a DB cluster restarts the database engine service. Rebooting a DB cluster results in a momentary outage, during which the DB cluster status is set to rebooting.

Use this operation only for a non-Aurora Multi-AZ DB cluster.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_RebootDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must match the identifier of an existing DBCluster.
Type: String  
Required: Yes

## Response Elements
<a name="API_RebootDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_RebootDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

## Examples
<a name="API_RebootDBCluster_Examples"></a>

### Example
<a name="API_RebootDBCluster_Example_1"></a>

This example illustrates one usage of RebootDBCluster.

#### Sample Request
<a name="API_RebootDBCluster_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=RebootDBCluster
   &DBClusterIdentifier=my-multi-az-cluster
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20211014/us-west-2/rds/aws4_request
   &X-Amz-Date=20211020T204924Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=1c48f44c14183cff26fde7d912946f87f3bb9d715f66448f457a8f9e99602af5
```

#### Sample Response
<a name="API_RebootDBCluster_Example_1_Response"></a>

```
<RebootDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RebootDBClusterResult>
    <DBCluster>
      <CrossAccountClone>false</CrossAccountClone>
      <AllocatedStorage>100</AllocatedStorage>
      <DatabaseName>mydb</DatabaseName>
      <AssociatedRoles />
      <AvailabilityZones>
        <AvailabilityZone>us-west-2a</AvailabilityZone>
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <AvailabilityZone>us-west-2c</AvailabilityZone>
      </AvailabilityZones>
      <ReadReplicaIdentifiers />
      <Iops>1000</Iops>
      <PerformanceInsightsKMSKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</PerformanceInsightsKMSKeyId>
      <PerformanceInsightsRetentionPeriod>7</PerformanceInsightsRetentionPeriod>
      <EngineVersion>8.0.26</EngineVersion>
      <MasterUsername>admin</MasterUsername>
      <DBClusterMembers>
        <DBClusterMember>
          <DBInstanceIdentifier>my-multi-az-cluster-instance-3</DBInstanceIdentifier>
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
          <PromotionTier>1</PromotionTier>
          <IsClusterWriter>false</IsClusterWriter>
        </DBClusterMember>
        <DBClusterMember>
          <DBInstanceIdentifier>my-multi-az-cluster-instance-2</DBInstanceIdentifier>
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
          <PromotionTier>1</PromotionTier>
          <IsClusterWriter>false</IsClusterWriter>
        </DBClusterMember>
        <DBClusterMember>
          <DBInstanceIdentifier>my-multi-az-cluster-instance-1</DBInstanceIdentifier>
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus>
          <PromotionTier>1</PromotionTier>
          <IsClusterWriter>true</IsClusterWriter>
        </DBClusterMember>
      </DBClusterMembers>
      <HttpEndpointEnabled>false</HttpEndpointEnabled>
      <Port>3306</Port>
      <MonitoringInterval>30</MonitoringInterval>
      <BackupRetentionPeriod>2</BackupRetentionPeriod>
      <KmsKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</KmsKeyId>
      <DBClusterIdentifier>my-multi-az-cluster</DBClusterIdentifier>
      <DbClusterResourceId>cluster-RCPGZXFNIHCTBQLDRJX6CP62VQ</DbClusterResourceId>
      <LatestRestorableTime>2021-10-20T20:45:00Z</LatestRestorableTime>
      <Status>available</Status>
      <PreferredBackupWindow>11:34-12:04</PreferredBackupWindow>
      <DeletionProtection>false</DeletionProtection>
      <Endpoint>my-multi-az-cluster.cluster-123456789012.us-west-2.rds.amazonaws.com</Endpoint>
      <EngineMode>provisioned</EngineMode>
      <Engine>mysql</Engine>
      <ReaderEndpoint>my-multi-az-cluster.cluster-ro-123456789012.us-west-2.rds.amazonaws.com</ReaderEndpoint>
      <PubliclyAccessible>true</PubliclyAccessible>
      <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
      <EarliestRestorableTime>2021-10-20T00:21:43.013Z</EarliestRestorableTime>
      <ClusterCreateTime>2021-10-20T00:12:00.867Z</ClusterCreateTime>
      <PerformanceInsightsEnabled>true</PerformanceInsightsEnabled>
      <MultiAZ>true</MultiAZ>
      <DomainMemberships />
      <MonitoringRoleArn>arn:aws:iam::123456789012:role/enhance-monitoring-role</MonitoringRoleArn>
      <StorageEncrypted>true</StorageEncrypted>
      <DBSubnetGroup>mysubnet1</DBSubnetGroup>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <VpcSecurityGroupId>sg-6921cc28</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <TagList />
      <HostedZoneId>Z3GZ3VYA3PGHTQ</HostedZoneId>
      <PreferredMaintenanceWindow>sat:07:05-sat:07:35</PreferredMaintenanceWindow>
      <DBClusterParameterGroup>my-multi-az-cluster-cpg</DBClusterParameterGroup>
      <StorageType>io1</StorageType>
      <DBClusterInstanceClass>db.r6gd.large</DBClusterInstanceClass>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <CopyTagsToSnapshot>false</CopyTagsToSnapshot>
      <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:my-multi-az-cluster</DBClusterArn>
    </DBCluster>
  </RebootDBClusterResult>
  <ResponseMetadata>
    <RequestId>056383d9-2d62-415d-b1bb-098b4cc86b5d</RequestId>
  </ResponseMetadata>
</RebootDBClusterResponse>
```

## See Also
<a name="API_RebootDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RebootDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RebootDBCluster) 