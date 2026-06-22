---
id: "@specs/aws/redshift/docs/API_EndpointAuthorization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointAuthorization"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EndpointAuthorization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EndpointAuthorization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointAuthorization
<a name="API_EndpointAuthorization"></a>

Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.

## Contents
<a name="API_EndpointAuthorization_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowedAllVPCs **   
Indicates whether all VPCs in the grantee account are allowed access to the cluster.  
Type: Boolean  
Required: No

 ** AllowedVPCs.VpcIdentifier.N **   
The VPCs allowed access to the cluster.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AuthorizeTime **   
The time (UTC) when the authorization was created.  
Type: Timestamp  
Required: No

 ** ClusterIdentifier **   
The cluster identifier.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterStatus **   
The status of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EndpointCount **   
The number of Redshift-managed VPC endpoints created for the authorization.  
Type: Integer  
Required: No

 ** Grantee **   
The AWS account ID of the grantee of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Grantor **   
The AWS account ID of the cluster owner.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
The status of the authorization action.  
Type: String  
Valid Values: `Authorized | Revoking`   
Required: No

## See Also
<a name="API_EndpointAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EndpointAuthorization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EndpointAuthorization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EndpointAuthorization) 