---
id: "@specs/aws/rds/docs/API_DescribeDBSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBSnapshots"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBSnapshots
<a name="API_DescribeDBSnapshots"></a>

Returns information about DB snapshots. This API action supports pagination.

## Request Parameters
<a name="API_DescribeDBSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The ID of the DB instance to retrieve the list of DB snapshots for. This parameter isn't case-sensitive.  
Constraints:  
+ If supplied, must match the identifier of an existing DBInstance.
Type: String  
Required: No

 ** DbiResourceId **   
A specific DB resource ID to describe.  
Type: String  
Required: No

 ** DBSnapshotIdentifier **   
A specific DB snapshot identifier to describe. This value is stored as a lowercase string.  
Constraints:  
+ If supplied, must match the identifier of an existing DBSnapshot.
+ If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more DB snapshots to describe.  
Supported filters:  
+  `db-instance-id` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).
+  `db-snapshot-id` - Accepts DB snapshot identifiers.
+  `dbi-resource-id` - Accepts identifiers of source DB instances.
+  `snapshot-type` - Accepts types of DB snapshots.
+  `engine` - Accepts names of database engines.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IncludePublic **   
Specifies whether to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account. By default, the public snapshots are not included.  
You can share a manual DB snapshot as public by using the [ModifyDBSnapshotAttribute](API_ModifyDBSnapshotAttribute.md) API.  
This setting doesn't apply to RDS Custom.  
Type: Boolean  
Required: No

 ** IncludeShared **   
Specifies whether to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore. By default, these snapshots are not included.  
You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the `ModifyDBSnapshotAttribute` API action.  
This setting doesn't apply to RDS Custom.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBSnapshots` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SnapshotType **   
The type of snapshots to be returned. You can specify one of the following values:  
+  `automated` - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account.
+  `manual` - Return all DB snapshots that have been taken by my AWS account.
+  `shared` - Return all manual DB snapshots that have been shared to my AWS account.
+  `public` - Return all DB snapshots that have been marked as public.
+  `awsbackup` - Return the DB snapshots managed by the AWS Backup service.

  For information about AWS Backup, see the [https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 

  The `awsbackup` type does not apply to Aurora.
If you don't specify a `SnapshotType` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by enabling the `IncludeShared` parameter. You can include public snapshots with these results by enabling the `IncludePublic` parameter.  
The `IncludeShared` and `IncludePublic` parameters don't apply for `SnapshotType` values of `manual` or `automated`. The `IncludePublic` parameter doesn't apply when `SnapshotType` is set to `shared`. The `IncludeShared` parameter doesn't apply when `SnapshotType` is set to `public`.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **DBSnapshots.DBSnapshot.N**   
A list of `DBSnapshot` instances.  
Type: Array of [DBSnapshot](API_DBSnapshot.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBSnapshots_Examples"></a>

### Example
<a name="API_DescribeDBSnapshots_Example_1"></a>

This example illustrates one usage of DescribeDBSnapshots.

#### Sample Request
<a name="API_DescribeDBSnapshots_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBSnapshots
   &IncludePublic=false
   &IncludeShared=true
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20210621/us-west-2/rds/aws4_request
   &X-Amz-Date=20210621T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=4aa31bdcf7b5e00dadffbd6dc8448a31871e283ffe270e77890e15487354bcca
```

#### Sample Response
<a name="API_DescribeDBSnapshots_Example_1_Response"></a>

```
<DescribeDBSnapshotsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBSnapshotsResult>
    <DBSnapshots>
      <DBSnapshot>
        <Port>3306</Port>
        <OptionGroupName>default:mysql-5-6</OptionGroupName>
        <Engine>mysql</Engine>
        <Status>available</Status>
        <SnapshotType>manual</SnapshotType>
        <LicenseModel>general-public-license</LicenseModel>
        <EngineVersion>5.6.44</EngineVersion>
        <DBInstanceIdentifier>my-mysqlexampledb</DBInstanceIdentifier>
        <DBSnapshotIdentifier>my-test-restore-snapshot</DBSnapshotIdentifier>
        <SnapshotCreateTime>2021-03-28T19:57:16.707Z</SnapshotCreateTime>
        <OriginalSnapshotCreateTime>2021-03-28T19:57:16.707Z</OriginalSnapshotCreateTime>
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <InstanceCreateTime>2021-01-29T22:58:24.231Z</InstanceCreateTime>
        <PercentProgress>100</PercentProgress>
        <AllocatedStorage>5</AllocatedStorage>
        <MasterUsername>awsmyuser</MasterUsername>
      </DBSnapshot>
      <DBSnapshot>
        <Port>3306</Port>
        <OptionGroupName>default:mysql-5-6</OptionGroupName>
        <Engine>mysql</Engine>
        <Status>available</Status>
        <SnapshotType>automated</SnapshotType>
        <LicenseModel>general-public-license</LicenseModel>
         <EngineVersion>5.6.44</EngineVersion>
        <DBInstanceIdentifier>my-mysqlexampledb</DBInstanceIdentifier>
        <DBSnapshotIdentifier>rds:my-mysqlexampledb-2021-04-19-10-08</DBSnapshotIdentifier>
        <SnapshotCreateTime>2021-05-11T06:02:03.422Z</SnapshotCreateTime>
        <OriginalSnapshotCreateTime>2021-04-27T08:16:05.356Z</OriginalSnapshotCreateTime>      
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <InstanceCreateTime>2021-01-29T22:58:24.231Z</InstanceCreateTime>
        <PercentProgress>100</PercentProgress>
        <AllocatedStorage>5</AllocatedStorage>
        <MasterUsername>awsmyuser</MasterUsername>
      </DBSnapshot>
      <DBSnapshot>
        <Port>3306</Port>
        <OptionGroupName>default:mysql-5-6</OptionGroupName>
        <Engine>mysql</Engine>
        <Status>available</Status>
        <SnapshotType>automated</SnapshotType>
        <LicenseModel>general-public-license</LicenseModel>
        <EngineVersion>5.6.44</EngineVersion>
        <DBInstanceIdentifier>my-mysqlexampledb</DBInstanceIdentifier>
        <DBSnapshotIdentifier>rds:my-mysqlexampledb-2021-04-20-10-09</DBSnapshotIdentifier>
        <SnapshotCreateTime>2021-04-20T10:09:15.446Z</SnapshotCreateTime>
        <OriginalSnapshotCreateTime>2021-04-20T10:09:15.446Z</OriginalSnapshotCreateTime>
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <InstanceCreateTime>2021-01-29T22:58:24.231Z</InstanceCreateTime>
        <PercentProgress>100</PercentProgress>
        <AllocatedStorage>5</AllocatedStorage>
        <MasterUsername>awsmyuser</MasterUsername>
      </DBSnapshot>
    </DBSnapshots>
  </DescribeDBSnapshotsResult>
  <ResponseMetadata>
    <RequestId>b7769930-b98c-11d3-f272-7cd6cce12cc5</RequestId>
  </ResponseMetadata>
</DescribeDBSnapshotsResponse>
```

## See Also
<a name="API_DescribeDBSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBSnapshots) 