---
id: "@specs/aws/rds/docs/API_ModifyDBSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBSnapshot
<a name="API_ModifyDBSnapshot"></a>

Updates a manual DB snapshot with a new engine version. The snapshot can be encrypted or unencrypted, but not shared or public. 

Amazon RDS supports upgrading DB snapshots for MariaDB, MySQL, PostgreSQL, and Oracle. This operation doesn't apply to RDS Custom or RDS for Db2.

## Request Parameters
<a name="API_ModifyDBSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSnapshotIdentifier **   
The identifier of the DB snapshot to modify.  
Type: String  
Required: Yes

 ** EngineVersion **   
The engine version to upgrade the DB snapshot to.  
The following are the database engines and engine versions that are available when you upgrade a DB snapshot.  
 **MariaDB**   
For the list of engine versions that are available for upgrading a DB snapshot, see [ Upgrading a MariaDB DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-upgrade-snapshot.html) in the *Amazon RDS User Guide.*   
 **MySQL**   
For the list of engine versions that are available for upgrading a DB snapshot, see [ Upgrading a MySQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.html) in the *Amazon RDS User Guide.*   
 **Oracle**   
+  `21.0.0.0.ru-2025-04.rur-2025-04.r1` (supported for 21.0.0.0.ru-2022-01.rur-2022-01.r1, 21.0.0.0.ru-2022-04.rur-2022-04.r1, 21.0.0.0.ru-2022-07.rur-2022-07.r1, 21.0.0.0.ru-2022-10.rur-2022-10.r1, 21.0.0.0.ru-2023-01.rur-2023-01.r1 and 21.0.0.0.ru-2023-01.rur-2023-01.r2 DB snapshots)
+  `19.0.0.0.ru-2025-04.rur-2025-04.r1` (supported for 19.0.0.0.ru-2019-07.rur-2019-07.r1, 19.0.0.0.ru-2019-10.rur-2019-10.r1 and 0.0.0.ru-2020-01.rur-2020-01.r1 DB snapshots)
+  `19.0.0.0.ru-2022-01.rur-2022-01.r1` (supported for 12.2.0.1 DB snapshots)
+  `19.0.0.0.ru-2022-07.rur-2022-07.r1` (supported for 12.1.0.2 DB snapshots)
+  `12.1.0.2.v8` (supported for 12.1.0.1 DB snapshots)
+  `11.2.0.4.v12` (supported for 11.2.0.2 DB snapshots)
+  `11.2.0.4.v11` (supported for 11.2.0.3 DB snapshots)
 **PostgreSQL**   
For the list of engine versions that are available for upgrading a DB snapshot, see [ Upgrading a PostgreSQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html) in the *Amazon RDS User Guide.*   
Type: String  
Required: No

 ** OptionGroupName **   
The option group to identify with the upgraded DB snapshot.  
You can specify this parameter when you upgrade an Oracle DB snapshot. The same option group considerations apply when upgrading a DB snapshot as when upgrading a DB instance. For more information, see [Option group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.html#USER_UpgradeDBInstance.Oracle.OGPG.OG) in the *Amazon RDS User Guide.*   
Type: String  
Required: No

## Response Elements
<a name="API_ModifyDBSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBSnapshot **   
Contains the details of an Amazon RDS DB snapshot.  
This data type is used as a response element in the `DescribeDBSnapshots` action.  
Type: [DBSnapshot](API_DBSnapshot.md) object

## Errors
<a name="API_ModifyDBSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** InvalidDBSnapshotState **   
The state of the DB snapshot doesn't allow deletion.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBSnapshot_Examples"></a>

### Example
<a name="API_ModifyDBSnapshot_Example_1"></a>

This example illustrates one usage of ModifyDBSnapshot.

#### Sample Request
<a name="API_ModifyDBSnapshot_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ModifyDBSnapshot
    &DBSnapshotIdentifier=mysnapshot1
    &EngineVersion=5.6.44
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20161228/us-west-2/rds/aws4_request
    &X-Amz-Date=20210628T220515Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=eb44f1ce3dab4e1dbf113d8d2a265d88d17ece1999ffd36be85714ed36cbdbe3
```

#### Sample Response
<a name="API_ModifyDBSnapshot_Example_1_Response"></a>

```
<ModifyDBSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBSnapshotResult>
    <DBSnapshot>
      <Port>3306</Port>
      <OptionGroupName>default:mysql-5-6</OptionGroupName>
      <Engine>mysql</Engine>
      <Status>available</Status>
      <SnapshotType>manual</SnapshotType>
      <LicenseModel>general-public-license</LicenseModel>
      <EngineVersion>5.6.44</EngineVersion>
      <DBInstanceIdentifier>mysqldb-sample</DBInstanceIdentifier>
      <DBSnapshotIdentifier>mysnapshot1</DBSnapshotIdentifier>
      <SnapshotCreateTime>2021-04-20T10:09:15.446Z</SnapshotCreateTime>
      <OriginalSnapshotCreateTime>2021-04-20T10:09:15.446Z</OriginalSnapshotCreateTime>
      <AvailabilityZone>us-west-2b</AvailabilityZone>
      <InstanceCreateTime>2016-12-28T22:24:26.573Z</InstanceCreateTime>
      <PercentProgress>100</PercentProgress>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
    </DBSnapshot>
  </ModifyDBSnapshotResult>
  <ResponseMetadata>
    <RequestId>aa80a25a-af09-11d4-ed11-23c32f9aa7d3</RequestId>
  </ResponseMetadata>
</ModifyDBSnapshotResponse>
```

## See Also
<a name="API_ModifyDBSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBSnapshot) 