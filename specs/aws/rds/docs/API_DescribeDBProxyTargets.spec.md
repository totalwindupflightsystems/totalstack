---
id: "@specs/aws/rds/docs/API_DescribeDBProxyTargets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBProxyTargets"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBProxyTargets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBProxyTargets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBProxyTargets
<a name="API_DescribeDBProxyTargets"></a>

Returns information about `DBProxyTarget` objects. This API supports pagination.

## Request Parameters
<a name="API_DescribeDBProxyTargets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyName **   
The identifier of the `DBProxyTarget` to describe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
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
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Valid Range: Minimum value of 20. Maximum value of 100.  
Required: No

 ** TargetGroupName **   
The identifier of the `DBProxyTargetGroup` to describe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

## Response Elements
<a name="API_DescribeDBProxyTargets_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **Targets.member.N**   
An arbitrary number of `DBProxyTarget` objects, containing details of the corresponding targets.  
Type: Array of [DBProxyTarget](API_DBProxyTarget.md) objects

## Errors
<a name="API_DescribeDBProxyTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetGroupNotFoundFault **   
The specified target group isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetNotFoundFault **   
The specified RDS DB instance or Aurora DB cluster isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeDBProxyTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBProxyTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBProxyTargets) 