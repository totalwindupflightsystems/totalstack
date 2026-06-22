---
id: "@specs/aws/redshift/docs/API_AuthorizeEndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthorizeEndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AuthorizeEndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AuthorizeEndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthorizeEndpointAccess
<a name="API_AuthorizeEndpointAccess"></a>

Grants access to a cluster.

## Request Parameters
<a name="API_AuthorizeEndpointAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Account **   
The AWS account ID to grant access to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ClusterIdentifier **   
The cluster identifier of the cluster to grant access to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **VpcIds.VpcIdentifier.N**   
The virtual private cloud (VPC) identifiers to grant access to.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_AuthorizeEndpointAccess_ResponseElements"></a>

The following elements are returned by the service.

 ** AllowedAllVPCs **   
Indicates whether all VPCs in the grantee account are allowed access to the cluster.  
Type: Boolean

 **AllowedVPCs.VpcIdentifier.N**   
The VPCs allowed access to the cluster.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 ** AuthorizeTime **   
The time (UTC) when the authorization was created.  
Type: Timestamp

 ** ClusterIdentifier **   
The cluster identifier.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ClusterStatus **   
The status of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** EndpointCount **   
The number of Redshift-managed VPC endpoints created for the authorization.  
Type: Integer

 ** Grantee **   
The AWS account ID of the grantee of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** Grantor **   
The AWS account ID of the cluster owner.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** Status **   
The status of the authorization action.  
Type: String  
Valid Values: `Authorized | Revoking` 

## Errors
<a name="API_AuthorizeEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** EndpointAuthorizationAlreadyExists **   
The authorization already exists for this endpoint.  
HTTP Status Code: 400

 ** EndpointAuthorizationsPerClusterLimitExceeded **   
The number of endpoint authorizations per cluster has exceeded its limit.  
HTTP Status Code: 400

 ** InvalidAuthorizationState **   
The status of the authorization is not valid.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_AuthorizeEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AuthorizeEndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthorizeEndpointAccess) 