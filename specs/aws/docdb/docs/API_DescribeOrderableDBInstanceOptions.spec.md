---
id: "@specs/aws/docdb/docs/API_DescribeOrderableDBInstanceOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOrderableDBInstanceOptions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeOrderableDBInstanceOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeOrderableDBInstanceOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOrderableDBInstanceOptions
<a name="API_DescribeOrderableDBInstanceOptions"></a>

Returns a list of orderable instance options for the specified engine.

## Request Parameters
<a name="API_DescribeOrderableDBInstanceOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **   
The name of the engine to retrieve instance options for.  
Type: String  
Required: Yes

 ** DBInstanceClass **   
The instance class filter value. Specify this parameter to show only the available offerings that match the specified instance class.  
Type: String  
Required: No

 ** EngineVersion **   
The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.  
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** LicenseModel **   
The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.  
Type: String  
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

 ** Vpc **   
The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DescribeOrderableDBInstanceOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **OrderableDBInstanceOptions.OrderableDBInstanceOption.N**   
The options that are available for a particular orderable instance.  
Type: Array of [OrderableDBInstanceOption](API_OrderableDBInstanceOption.md) objects

## Errors
<a name="API_DescribeOrderableDBInstanceOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeOrderableDBInstanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions) 