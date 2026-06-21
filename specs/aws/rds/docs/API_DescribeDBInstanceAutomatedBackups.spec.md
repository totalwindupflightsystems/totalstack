---
id: "@specs/aws/rds/docs/API_DescribeDBInstanceAutomatedBackups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBInstanceAutomatedBackups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBInstanceAutomatedBackups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBInstanceAutomatedBackups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBInstanceAutomatedBackups
<a name="API_DescribeDBInstanceAutomatedBackups"></a>

Displays backups for both current and deleted instances. For example, use this operation to find details about automated backups for previously deleted instances. Current instances with retention periods greater than zero (0) are returned for both the `DescribeDBInstanceAutomatedBackups` and `DescribeDBInstances` operations.

All parameters are optional.

## Request Parameters
<a name="API_DescribeDBInstanceAutomatedBackups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceAutomatedBackupsArn **   
The Amazon Resource Name (ARN) of the replicated automated backups, for example, `arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`.  
This setting doesn't apply to RDS Custom.  
Type: String  
Required: No

 ** DBInstanceIdentifier **   
(Optional) The user-supplied instance identifier. If this parameter is specified, it must match the identifier of an existing DB instance. It returns information from the specific DB instance's automated backup. This parameter isn't case-sensitive.  
Type: String  
Required: No

 ** DbiResourceId **   
The resource ID of the DB instance that is the source of the automated backup. This parameter isn't case-sensitive.  
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies which resources to return based on status.  
Supported filters are the following:  
+  `status` 
  +  `active` - Automated backups for current instances.
  +  `creating` - Automated backups that are waiting for the first automated snapshot to be available.
  +  `retained` - Automated backups for deleted instances and after backup replication is stopped.
+  `db-instance-id` - Accepts DB instance identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance automated backups identified by these ARNs.
+  `dbi-resource-id` - Accepts DB resource identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance resources identified by these ARNs.
Returns all resources by default. The status for each resource is specified in the response.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBInstanceAutomatedBackups_ResponseElements"></a>

The following elements are returned by the service.

 **DBInstanceAutomatedBackups.DBInstanceAutomatedBackup.N**   
A list of `DBInstanceAutomatedBackup` instances.  
Type: Array of [DBInstanceAutomatedBackup](API_DBInstanceAutomatedBackup.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBInstanceAutomatedBackups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceAutomatedBackupNotFound **   
No automated backup for this DB instance was found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBInstanceAutomatedBackups_Examples"></a>

### Example
<a name="API_DescribeDBInstanceAutomatedBackups_Example_1"></a>

This example illustrates one usage of DescribeDBInstanceAutomatedBackups.

#### Sample Request
<a name="API_DescribeDBInstanceAutomatedBackups_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
?Action=DescribeDBInstanceAutomatedBackups
&MaxRecords=100
&SignatureMethod=HmacSHA256
&SignatureVersion=4
&Version=2014-10-31
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIADQKE4SARGYLE/20140420/us-east-1/rds/aws4_request
&X-Amz-Date=20180912T200207Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=caa44629fa60576c2c282d9b74d47647f9e9f229f6d0e52db1d3be0d095743b0
```

#### Sample Response
<a name="API_DescribeDBInstanceAutomatedBackups_Example_1_Response"></a>

```
<DescribeDBInstanceAutomatedBackupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
<DescribeDBInstanceAutomatedBackupsResult>
<DBInstanceAutomatedBackups>
  <DBInstanceAutomatedBackup>DeleteDBInstanceAutomatedBackupResultDeleteDBInstanceAutomatedBackupResult
    <EngineVersion>11.2.0.4.v13</EngineVersion>
    <MasterUsername>admin</MasterUsername>
    <AllocatedStorage>50</AllocatedStorage>
    <InstanceCreateTime>2018-08-17T21:58:30Z</InstanceCreateTime>
    <DbiResourceId>db-IXRXA2XS7KFFA6JWYYWFZEBJDE</DbiResourceId>
    <DBInstanceArn>arn:aws:rds:us-east-1:1234567890:db:myoracle1</DBInstanceArn>
    <DBInstanceIdentifier>myoracle1</DBInstanceIdentifier>
    <RestoreWindow/>
    <Encrypted>false</Encrypted>
    <Engine>oracle-ee</Engine>
    <Port>1521</Port>
    <LicenseModel>bring-your-own-license</LicenseModel>
    <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
    <StorageType>magnetic</StorageType>
    <OptionGroupName>default:oracle-ee-11-2</OptionGroupName>
    <Region>us-east-1</Region>
    <Status>creating</Status>
  </DBInstanceAutomatedBackup>
  <DBInstanceAutomatedBackup>
    <EngineVersion>11.2.0.4.v12</EngineVersion>
    <MasterUsername>admin</MasterUsername>
    <AllocatedStorage>50</AllocatedStorage>
    <InstanceCreateTime>2018-08-21T00:32:55Z</InstanceCreateTime>
    <AvailabilityZone>us-east-1d</AvailabilityZone>
    <DbiResourceId>db-YVS5NRBNHPGJZ3IT3WADXYSWYU</DbiResourceId>
    <DBInstanceArn>arn:aws:rds:us-east-1:1234567890:db:myoracle2</DBInstanceArn>
    <DBInstanceIdentifier>myoracle1</DBInstanceIdentifier>
    <RestoreWindow>
      <EarliestTime>2018-08-21T00:33:32.648Z</EarliestTime>
      <LatestTime>2018-08-28T20:16:27Z</LatestTime>
    </RestoreWindow>
    <Encrypted>false</Encrypted>
    <Engine>oracle-ee</Engine>
    <Port>1521</Port>
    <LicenseModel>bring-your-own-license</LicenseModel>
    <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
    <StorageType>magnetic</StorageType>
    <OptionGroupName>default:oracle-ee-11-2</OptionGroupName>
    <Region>us-east-1</Region>
    <Status>active</Status>
  </DBInstanceAutomatedBackup>
</DBInstanceAutomatedBackups>
</DescribeDBInstanceAutomatedBackupsResult>
<ResponseMetadata>
<RequestId>298f362b-e14a-4ee0-9840-4546c276014a</RequestId>
</ResponseMetadata>
</DescribeDBInstanceAutomatedBackupsResponse>
```

## See Also
<a name="API_DescribeDBInstanceAutomatedBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBInstanceAutomatedBackups) 