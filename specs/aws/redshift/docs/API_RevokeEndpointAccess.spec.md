---
id: "@specs/aws/redshift/docs/API_RevokeEndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeEndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RevokeEndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RevokeEndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeEndpointAccess
<a name="API_RevokeEndpointAccess"></a>

Revokes access to a cluster.

## Request Parameters
<a name="API_RevokeEndpointAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Account **   
The AWS account ID whose access is to be revoked.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterIdentifier **   
The cluster to revoke access from.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Force **   
Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.  
Type: Boolean  
Required: No

 **VpcIds.VpcIdentifier.N**   
The virtual private cloud (VPC) identifiers for which access is to be revoked.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_RevokeEndpointAccess_ResponseElements"></a>

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
<a name="API_RevokeEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** EndpointAuthorizationNotFound **   
The authorization for this endpoint can't be found.  
HTTP Status Code: 404

 ** EndpointNotFound **   
The endpoint name doesn't refer to an existing endpoint.  
HTTP Status Code: 404

 ** InvalidAuthorizationState **   
The status of the authorization is not valid.  
HTTP Status Code: 400

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidEndpointState **   
The status of the endpoint is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_RevokeEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RevokeEndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RevokeEndpointAccess) 