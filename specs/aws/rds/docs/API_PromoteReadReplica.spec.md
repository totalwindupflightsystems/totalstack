---
id: "@specs/aws/rds/docs/API_PromoteReadReplica"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PromoteReadReplica"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# PromoteReadReplica

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_PromoteReadReplica
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PromoteReadReplica
<a name="API_PromoteReadReplica"></a>

Promotes a read replica DB instance to a standalone DB instance.

**Note**  
Backup duration is a function of the amount of changes to the database since the previous backup. If you plan to promote a read replica to a standalone instance, we recommend that you enable backups and complete at least one backup prior to promotion. In addition, a read replica cannot be promoted to a standalone instance when it is in the `backing-up` status. If you have enabled backups on your read replica, configure the automated backup window so that daily backups do not interfere with read replica promotion.
This command doesn't apply to Aurora MySQL, Aurora PostgreSQL, or RDS Custom.

## Request Parameters
<a name="API_PromoteReadReplica_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The DB instance identifier. This value is stored as a lowercase string.  
Constraints:  
+ Must match the identifier of an existing read replica DB instance.
Example: `mydbinstance`   
Type: String  
Required: Yes

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.  
Default: 1  
Constraints:  
+ Must be a value from 0 to 35.
+ Can't be set to 0 if the DB instance is a source to read replicas.
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter.  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see [ Adjusting the Preferred Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB instance.  
Valid Values:   
+  `auto-backup` - The DB instance's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

## Response Elements
<a name="API_PromoteReadReplica_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_PromoteReadReplica_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

## Examples
<a name="API_PromoteReadReplica_Examples"></a>

### Example
<a name="API_PromoteReadReplica_Example_1"></a>

This example illustrates one usage of PromoteReadReplica.

#### Sample Request
<a name="API_PromoteReadReplica_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=PromoteReadReplica
   &BackupRetentionPeriod=7
   &DBInstanceIdentifier=mysqldb-rr
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T221536Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=c0b2cfc3db8334b6ef86922f664e05ab306754e30e408d9fd3c8e58069a9b386
```

#### Sample Response
<a name="API_PromoteReadReplica_Example_1_Response"></a>

```
<PromoteReadReplicaResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <PromoteReadReplicaResult>
    <DBInstance>
      <BackupRetentionPeriod>0</BackupRetentionPeriod>
      <DBInstanceStatus>modifying</DBInstanceStatus>
      <MultiAZ>false</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>mysqldb-rr</DBInstanceIdentifier>
      <PreferredBackupWindow>08:25-08:55</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:04:50-fri:05:20</PreferredMaintenanceWindow>
      <StatusInfos>
        <DBInstanceStatusInfo>
          <Status>replicating</Status>
          <StatusType>read replication</StatusType>
          <Normal>true</Normal>
        </DBInstanceStatusInfo>
      </StatusInfos>
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <ReadReplicaDBInstanceIdentifiers/>
      <Engine>mysql</Engine>
      <PendingModifiedValues>
        <BackupRetentionPeriod>7</BackupRetentionPeriod>
      </PendingModifiedValues>
      <LicenseModel>general-public-license</LicenseModel>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
      <Endpoint>
        <Port>3306</Port>
        <Address>mysqldb-rr.cg029hpkxcjt.us-east-1.rds.amazonaws.com</Address>
      </Endpoint>
      <EngineVersion>5.6.13</EngineVersion>
      <ReadReplicaSourceDBInstanceIdentifier>mysqldb</ReadReplicaSourceDBInstanceIdentifier>
      <OptionGroupMemberships>
        <OptionGroupMembership>
          <OptionGroupName>default:mysql-5-6</OptionGroupName>
          <Status>in-sync</Status>
        </OptionGroupMembership>
      </OptionGroupMemberships>
      <PubliclyAccessible>true</PubliclyAccessible>
      <DBSecurityGroups>
        <DBSecurityGroup>
          <Status>active</Status>
          <DBSecurityGroupName>default</DBSecurityGroupName>
        </DBSecurityGroup>
      </DBSecurityGroups>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <DBName>mysqldb</DBName>
      <InstanceCreateTime>2014-04-25T17:12:34.460Z</InstanceCreateTime>
      <AllocatedStorage>100</AllocatedStorage>
      <DBInstanceClass>db.m1.medium</DBInstanceClass>
      <MasterUsername>myawsuser</MasterUsername>
    </DBInstance>
  </PromoteReadReplicaResult>
  <ResponseMetadata>
    <RequestId>8e8c0d64-be21-11d3-a71c-13dc2f771e41</RequestId>
  </ResponseMetadata>
</PromoteReadReplicaResponse>
```

## See Also
<a name="API_PromoteReadReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/PromoteReadReplica) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PromoteReadReplica) 