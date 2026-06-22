---
id: "@specs/aws/docdb/docs/API_DescribeDBEngineVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBEngineVersions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeDBEngineVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeDBEngineVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBEngineVersions
<a name="API_DescribeDBEngineVersions"></a>

Returns a list of the available engines.

## Request Parameters
<a name="API_DescribeDBEngineVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupFamily **   
The name of a specific parameter group family to return details for.  
Constraints:  
+ If provided, must match an existing `DBParameterGroupFamily`.
Type: String  
Required: No

 ** DefaultOnly **   
Indicates that only the default version of the specified engine or engine and major version combination is returned.  
Type: Boolean  
Required: No

 ** Engine **   
The database engine to return.  
Type: String  
Required: No

 ** EngineVersion **   
The database engine version to return.  
Example: `3.6.0`   
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** ListSupportedCharacterSets **   
If this parameter is specified and the requested engine supports the `CharacterSetName` parameter for `CreateDBInstance`, the response includes a list of supported character sets for each engine version.   
Type: Boolean  
Required: No

 ** ListSupportedTimezones **   
If this parameter is specified and the requested engine supports the `TimeZone` parameter for `CreateDBInstance`, the response includes a list of supported time zones for each engine version.   
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBEngineVersions_ResponseElements"></a>

The following elements are returned by the service.

 **DBEngineVersions.DBEngineVersion.N**   
Detailed information about one or more engine versions.  
Type: Array of [DBEngineVersion](API_DBEngineVersion.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeDBEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeDBEngineVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBEngineVersions) 