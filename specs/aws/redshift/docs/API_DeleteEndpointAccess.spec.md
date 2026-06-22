---
id: "@specs/aws/redshift/docs/API_DeleteEndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteEndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteEndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEndpointAccess
<a name="API_DeleteEndpointAccess"></a>

Deletes a Redshift-managed VPC endpoint.

## Request Parameters
<a name="API_DeleteEndpointAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EndpointName **   
The Redshift-managed VPC endpoint to delete.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_DeleteEndpointAccess_ResponseElements"></a>

The following elements are returned by the service.

 ** Address **   
The DNS address of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ClusterIdentifier **   
The cluster identifier of the cluster associated with the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** EndpointCreateTime **   
The time (UTC) that the endpoint was created.  
Type: Timestamp

 ** EndpointName **   
The name of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** EndpointStatus **   
The status of the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** Port **   
The port number on which the cluster accepts incoming connections.  
Type: Integer

 ** ResourceOwner **   
The AWS account ID of the owner of the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** SubnetGroupName **   
The subnet group name where Amazon Redshift chooses to deploy the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** VpcEndpoint **   
The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.  
Type: [VpcEndpoint](API_VpcEndpoint.md) object

 **VpcSecurityGroups.VpcSecurityGroup.N**   
The security groups associated with the endpoint.  
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects

## Errors
<a name="API_DeleteEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** EndpointNotFound **   
The endpoint name doesn't refer to an existing endpoint.  
HTTP Status Code: 404

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
<a name="API_DeleteEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteEndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteEndpointAccess) 