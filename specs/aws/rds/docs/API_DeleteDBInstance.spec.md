---
id: "@specs/aws/rds/docs/API_DeleteDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBInstance
<a name="API_DeleteDBInstance"></a>

Deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can't be recovered. However, manual DB snapshots of the DB instance aren't deleted.

If you request a final DB snapshot, the status of the Amazon RDS DB instance is `deleting` until the DB snapshot is created. This operation can't be canceled or reverted after it begins. To monitor the status of this operation, use `DescribeDBInstance`.

When a DB instance is in a failure state and has a status of `failed`, `incompatible-restore`, or `incompatible-network`, you can only delete it when you skip creation of the final snapshot with the `SkipFinalSnapshot` parameter.

If the specified DB instance is part of an Amazon Aurora DB cluster, you can't delete the DB instance if both of the following conditions are true:
+ The DB cluster is a read replica of another Amazon Aurora DB cluster.
+ The DB instance is the only instance in the DB cluster.

To delete a DB instance in this case, first use the `PromoteReadReplicaDBCluster` operation to promote the DB cluster so that it's no longer a read replica. After the promotion completes, use the `DeleteDBInstance` operation to delete the final instance in the DB cluster.

**Important**  
For RDS Custom DB instances, deleting the DB instance permanently deletes the EC2 instance and the associated EBS volumes. Make sure that you don't terminate or delete these resources before you delete the DB instance. Otherwise, deleting the DB instance and creation of the final snapshot might fail.

## Request Parameters
<a name="API_DeleteDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the name of an existing DB instance.
Type: String  
Required: Yes

 ** DeleteAutomatedBackups **   
Specifies whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.  
Type: Boolean  
Required: No

 ** FinalDBSnapshotIdentifier **   
The `DBSnapshotIdentifier` of the new `DBSnapshot` created when the `SkipFinalSnapshot` parameter is disabled.  
If you enable this parameter and also enable SkipFinalShapshot, the command results in an error.
This setting doesn't apply to RDS Custom.  
Constraints:  
+ Must be 1 to 255 letters or numbers.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
+ Can't be specified when deleting a read replica.
Type: String  
Required: No

 ** SkipFinalSnapshot **   
Specifies whether to skip the creation of a final DB snapshot before deleting the instance. If you enable this parameter, RDS doesn't create a DB snapshot. If you don't enable this parameter, RDS creates a DB snapshot before the DB instance is deleted. By default, skip isn't enabled, and the DB snapshot is created.  
If you don't enable this parameter, you must specify the `FinalDBSnapshotIdentifier` parameter.
When a DB instance is in a failure state and has a status of `failed`, `incompatible-restore`, or `incompatible-network`, RDS can delete the instance only if you enable this parameter.  
If you delete a read replica or an RDS Custom instance, you must enable this setting.  
This setting is required for RDS Custom.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_DeleteDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceAutomatedBackupQuotaExceeded **   
The quota for retained automated backups was exceeded. This prevents you from retaining any additional automated backups. The retained automated backups quota is the same as your DB instance quota.  
HTTP Status Code: 400

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **   
 `DBSnapshotIdentifier` is already used by an existing snapshot.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB snapshots.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBInstance_Examples"></a>

### Example
<a name="API_DeleteDBInstance_Example_1"></a>

This example illustrates one usage of DeleteDBInstance.

#### Sample Request
<a name="API_DeleteDBInstance_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteDBInstance
   &DBInstanceIdentifier=mydatabase
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SkipFinalSnapshot=true
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20131109/us-east-1/rds/aws4_request
   &X-Amz-Date=20131109T001924Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=70e774e243c0fbb7ffe84029637005bf543e9e321cdf432c0b272be5687d32d8
```

#### Sample Response
<a name="API_DeleteDBInstance_Example_1_Response"></a>

```
<DeleteDBInstanceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteDBInstanceResult>
    <DBInstance>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
      <DBInstanceStatus>deleting</DBInstanceStatus>
      <MultiAZ>false</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>mydatabase</DBInstanceIdentifier>
      <PreferredBackupWindow>08:14-08:44</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:04:50-fri:05:20</PreferredMaintenanceWindow>
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <ReadReplicaDBInstanceIdentifiers/>
      <LatestRestorableTime>2013-11-09T00:15:00Z</LatestRestorableTime>
      <Engine>mysql</Engine>
      <PendingModifiedValues/>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.13</EngineVersion>
      <Endpoint>
        <Port>3306</Port>
        <Address>mydatabase.cf037hpkuvjt.us-east-1.rds.amazonaws.com</Address>
      </Endpoint>
      <DBParameterGroups>
        <DBParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
        </DBParameterGroup>
      </DBParameterGroups>
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
      <DBName>mysqldb</DBName>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <InstanceCreateTime>2011-04-28T23:33:54.909Z</InstanceCreateTime>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
      <DBInstanceClass>db.m1.medium</DBInstanceClass>
    </DBInstance>
  </DeleteDBInstanceResult>
  <ResponseMetadata>
    <RequestId>7369556f-b70d-11c3-faca-6ba18376ea1b</RequestId>
  </ResponseMetadata>
</DeleteDBInstanceResponse>
```

## See Also
<a name="API_DeleteDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBInstance) 