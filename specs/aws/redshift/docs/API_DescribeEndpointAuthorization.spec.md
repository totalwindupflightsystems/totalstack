---
id: "@specs/aws/redshift/docs/API_DescribeEndpointAuthorization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEndpointAuthorization"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeEndpointAuthorization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeEndpointAuthorization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEndpointAuthorization
<a name="API_DescribeEndpointAuthorization"></a>

Describes an endpoint authorization.

## Request Parameters
<a name="API_DescribeEndpointAuthorization_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Account **   
The AWS account ID of either the cluster owner (grantor) or grantee. If `Grantee` parameter is true, then the `Account` value is of the grantor.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterIdentifier **   
The cluster identifier of the cluster to access.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Grantee **   
Indicates whether to check authorization from a grantor or grantee point of view. If true, Amazon Redshift returns endpoint authorizations that you've been granted. If false (default), checks authorization from a grantor point of view.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeEndpointAuthorization` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a `Marker` is included in the response so that the remaining results can be retrieved.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeEndpointAuthorization_ResponseElements"></a>

The following elements are returned by the service.

 **EndpointAuthorizationList.member.N**   
The authorizations to an endpoint.  
Type: Array of [EndpointAuthorization](API_EndpointAuthorization.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeEndpointAuthorization` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeEndpointAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeEndpointAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeEndpointAuthorization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeEndpointAuthorization) 