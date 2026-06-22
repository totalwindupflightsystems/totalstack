---
id: "@specs/aws/redshift/docs/API_EndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointAccess
<a name="API_EndpointAccess"></a>

Describes a Redshift-managed VPC endpoint.

## Contents
<a name="API_EndpointAccess_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Address **   
The DNS address of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterIdentifier **   
The cluster identifier of the cluster associated with the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EndpointCreateTime **   
The time (UTC) that the endpoint was created.  
Type: Timestamp  
Required: No

 ** EndpointName **   
The name of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EndpointStatus **   
The status of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Port **   
The port number on which the cluster accepts incoming connections.  
Type: Integer  
Required: No

 ** ResourceOwner **   
The AWS account ID of the owner of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SubnetGroupName **   
The subnet group name where Amazon Redshift chooses to deploy the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** VpcEndpoint **   
The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.  
Type: [VpcEndpoint](API_VpcEndpoint.md) object  
Required: No

 ** VpcSecurityGroups.VpcSecurityGroup.N **   
The security groups associated with the endpoint.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects  
Required: No

## See Also
<a name="API_EndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EndpointAccess) 