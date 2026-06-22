---
id: "@specs/aws/docdb/docs/API_DescribeDBInstances"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBInstances"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeDBInstances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeDBInstances
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBInstances
<a name="API_DescribeDBInstances"></a>

Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.

## Request Parameters
<a name="API_DescribeDBInstances_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The user-provided instance identifier. If this parameter is specified, information from only the specific instance is returned. This parameter isn't case sensitive.  
Constraints:  
+ If provided, must match the identifier of an existing `DBInstance`.
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more instances to describe.  
Supported filters:  
+  `db-cluster-id` - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only the information about the instances that are associated with the clusters that are identified by these ARNs.
+  `db-instance-id` - Accepts instance identifiers and instance ARNs. The results list includes only the information about the instances that are identified by these ARNs.
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

## Response Elements
<a name="API_DescribeDBInstances_ResponseElements"></a>

The following elements are returned by the service.

 **DBInstances.DBInstance.N**   
Detailed information about one or more instances.   
Type: Array of [DBInstance](API_DBInstance.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing instance.   
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeDBInstances) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBInstances) 