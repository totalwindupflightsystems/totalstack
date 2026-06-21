---
id: "@specs/aws/rds/docs/API_DescribeDBClusterEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterEndpoints"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterEndpoints
<a name="API_DescribeDBClusterEndpoints"></a>

Returns information about endpoints for an Amazon Aurora DB cluster.

**Note**  
This action only applies to Aurora DB clusters.

## Request Parameters
<a name="API_DescribeDBClusterEndpoints_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterEndpointIdentifier **   
The identifier of the endpoint to describe. This parameter is stored as a lowercase string.  
Type: String  
Required: No

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String  
Required: No

 **Filters.Filter.N**   
A set of name-value pairs that define which endpoints to include in the output. The filters are specified as name-value pairs, in the format `Name=endpoint_type,Values=endpoint_type1,endpoint_type2,...`. `Name` can be one of: `db-cluster-endpoint-type`, `db-cluster-endpoint-custom-type`, `db-cluster-endpoint-id`, `db-cluster-endpoint-status`. `Values` for the ` db-cluster-endpoint-type` filter can be one or more of: `reader`, `writer`, `custom`. `Values` for the `db-cluster-endpoint-custom-type` filter can be one or more of: `reader`, `any`. `Values` for the `db-cluster-endpoint-status` filter can be one or more of: `available`, `creating`, `deleting`, `inactive`, `modifying`.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterEndpoints` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBClusterEndpoints_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterEndpoints.DBClusterEndpointList.N**   
Contains the details of the endpoints associated with the cluster and matching any filter conditions.  
Type: Array of [DBClusterEndpoint](API_DBClusterEndpoint.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterEndpoints` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBClusterEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterEndpoints) 