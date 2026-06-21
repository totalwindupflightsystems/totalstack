---
id: "@specs/aws/rds/docs/API_DescribeDBEngineVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBEngineVersions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBEngineVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBEngineVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBEngineVersions
<a name="API_DescribeDBEngineVersions"></a>

Describes the properties of specific versions of DB engines.

## Request Parameters
<a name="API_DescribeDBEngineVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupFamily **   
The name of a specific DB parameter group family to return details for.  
Constraints:  
+ If supplied, must match an existing DB parameter group family.
Type: String  
Required: No

 ** DefaultOnly **   
Specifies whether to return only the default version of the specified engine or the engine and major version combination.  
Type: Boolean  
Required: No

 ** Engine **   
The database engine to return version details for.  
Valid Values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
+  `custom-oracle-ee` 
+  `custom-oracle-ee-cdb` 
+  `custom-oracle-se2` 
+  `custom-oracle-se2-cdb` 
+  `db2-ae` 
+  `db2-ce` 
+  `db2-se` 
+  `mariadb` 
+  `mysql` 
+  `oracle-ee` 
+  `oracle-ee-cdb` 
+  `oracle-se2` 
+  `oracle-se2-cdb` 
+  `postgres` 
+  `sqlserver-ee` 
+  `sqlserver-se` 
+  `sqlserver-ex` 
+  `sqlserver-web` 
+  `sqlserver-dev-ee` 
Type: String  
Required: No

 ** EngineVersion **   
A specific database engine version to return details for.  
Example: `5.1.49`   
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more DB engine versions to describe.  
Supported filters:  
+  `db-parameter-group-family` - Accepts parameter groups family names. The results list only includes information about the DB engine versions for these parameter group families.
+  `engine` - Accepts engine names. The results list only includes information about the DB engine versions for these engines.
+  `engine-mode` - Accepts DB engine modes. The results list only includes information about the DB engine versions for these engine modes. Valid DB engine modes are the following:
  +  `global` 
  +  `multimaster` 
  +  `parallelquery` 
  +  `provisioned` 
  +  `serverless` 
+  `engine-version` - Accepts engine versions. The results list only includes information about the DB engine versions for these engine versions.
+  `status` - Accepts engine version statuses. The results list only includes information about the DB engine versions for these statuses. Valid statuses are the following:
  +  `available` 
  +  `deprecated` 
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IncludeAll **   
Specifies whether to also list the engine versions that aren't available. The default is to list only available engine versions.  
Type: Boolean  
Required: No

 ** ListSupportedCharacterSets **   
Specifies whether to list the supported character sets for each engine version.  
If this parameter is enabled and the requested engine supports the `CharacterSetName` parameter for `CreateDBInstance`, the response includes a list of supported character sets for each engine version.  
For RDS Custom, the default is not to list supported character sets. If you enable this parameter, RDS Custom returns no results.  
Type: Boolean  
Required: No

 ** ListSupportedTimezones **   
Specifies whether to list the supported time zones for each engine version.  
If this parameter is enabled and the requested engine supports the `TimeZone` parameter for `CreateDBInstance`, the response includes a list of supported time zones for each engine version.  
For RDS Custom, the default is not to list supported time zones. If you enable this parameter, RDS Custom returns no results.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more than the `MaxRecords` value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBEngineVersions_ResponseElements"></a>

The following elements are returned by the service.

 **DBEngineVersions.DBEngineVersion.N**   
A list of `DBEngineVersion` elements.  
Type: Array of [DBEngineVersion](API_DBEngineVersion.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeDBEngineVersions_Examples"></a>

### Example
<a name="API_DescribeDBEngineVersions_Example_1"></a>

This example illustrates one usage of DescribeDBEngineVersions.

#### Sample Request
<a name="API_DescribeDBEngineVersions_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBEngineVersions
   &MaxRecords=100 
   &SignatureMethod=HmacSHA256 
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=4772d17a4c43bcd209ff42a0778dd23e73f8434253effd7ac53b89ade3dad45f
```

#### Sample Response
<a name="API_DescribeDBEngineVersions_Example_1_Response"></a>

```
<DescribeDBEngineVersionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBEngineVersionsResult>
    <DBEngineVersions>
      <DBEngineVersion>
        <Engine>mysql</Engine>
        <DBParameterGroupFamily>mysql5.1</DBParameterGroupFamily>
        <DBEngineDescription>MySQL Community Edition</DBEngineDescription>
        <EngineVersion>5.1.57</EngineVersion>
        <DBEngineVersionDescription>MySQL 5.1.57</DBEngineVersionDescription>
      </DBEngineVersion>
      <DBEngineVersion>
        <Engine>mysql</Engine>
        <DBParameterGroupFamily>mysql5.1</DBParameterGroupFamily>
        <DBEngineDescription>MySQL Community Edition</DBEngineDescription>
        <EngineVersion>5.1.61</EngineVersion>
        <DBEngineVersionDescription>MySQL 5.1.61</DBEngineVersionDescription>
      </DBEngineVersion>
      <DBEngineVersion>
        <Engine>mysql</Engine>
        <DBParameterGroupFamily>mysql5.1</DBParameterGroupFamily>
        <DBEngineDescription>MySQL Community Edition</DBEngineDescription>
        <EngineVersion>5.1.62</EngineVersion>
        <DBEngineVersionDescription>MySQL 5.1.62</DBEngineVersionDescription>
      </DBEngineVersion>
  </DescribeDBEngineVersionsResult>
  <ResponseMetadata>
    <RequestId>b74d2635-b98c-11d3-fbc7-5c0aad74da7c</RequestId>
  </ResponseMetadata>
</DescribeDBEngineVersionsResponse>
```

## See Also
<a name="API_DescribeDBEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBEngineVersions) 