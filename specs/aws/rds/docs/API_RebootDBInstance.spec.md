---
id: "@specs/aws/rds/docs/API_RebootDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RebootDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RebootDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RebootDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RebootDBInstance
<a name="API_RebootDBInstance"></a>

You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.

Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.

For more information about rebooting, see [Rebooting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html) in the *Amazon RDS User Guide.* 

This command doesn't apply to RDS Custom.

If your DB instance is part of a Multi-AZ DB cluster, you can reboot the DB cluster with the `RebootDBCluster` operation.

## Request Parameters
<a name="API_RebootDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The DB instance identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must match the identifier of an existing DBInstance.
Type: String  
Required: Yes

 ** ForceFailover **   
Specifies whether the reboot is conducted through a Multi-AZ failover.  
Constraint: You can't enable force failover if the instance isn't configured for Multi-AZ.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_RebootDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_RebootDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

## Examples
<a name="API_RebootDBInstance_Examples"></a>

### Example
<a name="API_RebootDBInstance_Example_1"></a>

This example illustrates one usage of RebootDBInstance.

#### Sample Request
<a name="API_RebootDBInstance_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=RebootDBInstance
   &DBInstanceIdentifier=mysqldb
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T222011Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=1c48f44c14183cff26fde7d912946f87f3bb9d715f66448f457a8f9e99602af5
```

#### Sample Response
<a name="API_RebootDBInstance_Example_1_Response"></a>

```
<RebootDBInstanceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RebootDBInstanceResult>
    <DBInstance>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
      <DBInstanceStatus>rebooting</DBInstanceStatus>
      <MultiAZ>false</MultiAZ>
      <VpcSecurityGroups/>
      <DBInstanceIdentifier>mysqldb</DBInstanceIdentifier>
      <PreferredBackupWindow>08:14-08:44</PreferredBackupWindow>
      <PreferredMaintenanceWindow>fri:04:50-fri:05:20</PreferredMaintenanceWindow>
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <ReadReplicaDBInstanceIdentifiers/>
      <LatestRestorableTime>2014-04-28T22:15:00Z</LatestRestorableTime>
      <Engine>mysql</Engine>
      <PendingModifiedValues/>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.13</EngineVersion>
      <Endpoint>
        <Port>3306</Port>
        <Address>mysqldb.cb036hpkmopt.us-east-1.rds.amazonaws.com</Address>
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
      <InstanceCreateTime>2014-04-21T22:24:26.573Z</InstanceCreateTime>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
      <DBInstanceClass>db.m1.medium</DBInstanceClass>
    </DBInstance>
  </RebootDBInstanceResult>
  <ResponseMetadata>
    <RequestId>33c99cd2-be22-11d3-abdb-7cb19376fb1c</RequestId>
  </ResponseMetadata>
</RebootDBInstanceResponse>
```

## See Also
<a name="API_RebootDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RebootDBInstance) 