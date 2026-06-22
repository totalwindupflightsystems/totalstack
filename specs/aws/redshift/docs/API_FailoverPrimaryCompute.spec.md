---
id: "@specs/aws/redshift/docs/API_FailoverPrimaryCompute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailoverPrimaryCompute"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# FailoverPrimaryCompute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_FailoverPrimaryCompute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailoverPrimaryCompute
<a name="API_FailoverPrimaryCompute"></a>

Fails over the primary compute unit of the specified Multi-AZ cluster to another Availability Zone.

## Request Parameters
<a name="API_FailoverPrimaryCompute_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster for which the primary compute unit will be failed over to another Availability Zone.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_FailoverPrimaryCompute_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_FailoverPrimaryCompute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_FailoverPrimaryCompute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/FailoverPrimaryCompute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/FailoverPrimaryCompute) 