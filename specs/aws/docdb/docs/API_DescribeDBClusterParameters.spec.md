---
id: "@specs/aws/docdb/docs/API_DescribeDBClusterParameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterParameters"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeDBClusterParameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeDBClusterParameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterParameters
<a name="API_DescribeDBClusterParameters"></a>

Returns the detailed parameter list for a particular cluster parameter group.

## Request Parameters
<a name="API_DescribeDBClusterParameters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of a specific cluster parameter group to return parameter details for.  
Constraints:  
+ If provided, must match the name of an existing `DBClusterParameterGroup`.
Type: String  
Required: Yes

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
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

 ** Source **   
 A value that indicates to return only parameters for a specific source. Parameter sources can be `engine`, `service`, or `customer`.   
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBClusterParameters_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **Parameters.Parameter.N**   
Provides a list of parameters for the cluster parameter group.  
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeDBClusterParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing parameter group.   
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterParameters) 