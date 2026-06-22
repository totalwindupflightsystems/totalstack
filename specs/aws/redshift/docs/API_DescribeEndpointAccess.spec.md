---
id: "@specs/aws/redshift/docs/API_DescribeEndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeEndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeEndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEndpointAccess
<a name="API_DescribeEndpointAccess"></a>

Describes a Redshift-managed VPC endpoint.

## Request Parameters
<a name="API_DescribeEndpointAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The cluster identifier associated with the described endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EndpointName **   
The name of the endpoint to be described.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeEndpointAccess` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a `Marker` is included in the response so that the remaining results can be retrieved.  
Type: Integer  
Required: No

 ** ResourceOwner **   
The AWS account ID of the owner of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** VpcId **   
The virtual private cloud (VPC) identifier with access to the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeEndpointAccess_ResponseElements"></a>

The following elements are returned by the service.

 **EndpointAccessList.member.N**   
The list of endpoints with access to the cluster.  
Type: Array of [EndpointAccess](API_EndpointAccess.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeEndpointAccess` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** EndpointNotFound **   
The endpoint name doesn't refer to an existing endpoint.  
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

## See Also
<a name="API_DescribeEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeEndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeEndpointAccess) 