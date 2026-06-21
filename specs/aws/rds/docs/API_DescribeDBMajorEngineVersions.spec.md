---
id: "@specs/aws/rds/docs/API_DescribeDBMajorEngineVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBMajorEngineVersions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBMajorEngineVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBMajorEngineVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBMajorEngineVersions
<a name="API_DescribeDBMajorEngineVersions"></a>

Describes the properties of specific major versions of DB engines.

## Request Parameters
<a name="API_DescribeDBMajorEngineVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **   
The database engine to return major version details for.  
Valid Values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
+  `custom-sqlserver-ee` 
+  `custom-sqlserver-se` 
+  `custom-sqlserver-web` 
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
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: No

 ** MajorEngineVersion **   
A specific database major engine version to return details for.  
Example: `8.4`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 340.  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more than the `MaxRecords` value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Type: Integer  
Valid Range: Minimum value of 20. Maximum value of 100.  
Required: No

## Response Elements
<a name="API_DescribeDBMajorEngineVersions_ResponseElements"></a>

The following elements are returned by the service.

 **DBMajorEngineVersions.DBMajorEngineVersion.N**   
A list of `DBMajorEngineVersion` elements.  
Type: Array of [DBMajorEngineVersion](API_DBMajorEngineVersion.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBMajorEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeDBMajorEngineVersions_Examples"></a>

### Example
<a name="API_DescribeDBMajorEngineVersions_Example_1"></a>

This example illustrates one usage of DescribeDBMajorEngineVersions.

#### Sample Request
<a name="API_DescribeDBMajorEngineVersions_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBMajorEngineVersions
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
<a name="API_DescribeDBMajorEngineVersions_Example_1_Response"></a>

```
<DescribeDBMajorEngineVersionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBMajorEngineVersionsResult>
    <DBMajorEngineVersions>
      <DBMajorEngineVersion>
        <Engine>mysql</Engine>
        <MajorEngineVersion>8.0</MajorEngineVersion>
      </DBMajorEngineVersion>
      <DBMajorEngineVersion>
        <Engine>mysql</Engine>
        <MajorEngineVersion>8.0</MajorEngineVersion>
        <SupportedEngineLifecycles>
          <LifecycleSupportName>open-source-rds-standard-support</LifecycleSupportName>
          <LifecycleSupportStartDate>2021-08-26T00:00:00+00:00</LifecycleSupportStartDate>
          <LifecycleSupportEndDate>2026-02-28T23:59:59.999000+00:00</LifecycleSupportEndDate>
        </SupportedEngineLifecycles>
      </DBMajorEngineVersion>
  </DescribeDBMajorEngineVersionsResult>
  <ResponseMetadata>
    <RequestId>b74d2635-b98c-11d3-fbc7-5c0aad74da7c</RequestId>
  </ResponseMetadata>
</DescribeDBMajorEngineVersionsResponse>
```

## See Also
<a name="API_DescribeDBMajorEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBMajorEngineVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBMajorEngineVersions) 