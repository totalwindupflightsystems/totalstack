---
id: "@specs/aws/redshift/docs/API_CreateEndpointAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateEndpointAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateEndpointAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateEndpointAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateEndpointAccess
<a name="API_CreateEndpointAccess"></a>

Creates a Redshift-managed VPC endpoint.

## Request Parameters
<a name="API_CreateEndpointAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EndpointName **   
The Redshift-managed VPC endpoint name.  
An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SubnetGroupName **   
The subnet group from which Amazon Redshift chooses the subnet to deploy the endpoint.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ClusterIdentifier **   
The cluster identifier of the cluster to access.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ResourceOwner **   
The AWS account ID of the owner of the cluster. This is only required if the cluster is in another AWS account.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_CreateEndpointAccess_ResponseElements"></a>

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
<a name="API_CreateEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessToClusterDenied **   
You are not authorized to access the cluster.  
HTTP Status Code: 400

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSubnetGroupNotFoundFault **   
The cluster subnet group name does not refer to an existing cluster subnet group.  
HTTP Status Code: 400

 ** EndpointAlreadyExists **   
The account already has a Redshift-managed VPC endpoint with the given identifier.  
HTTP Status Code: 400

 ** EndpointsPerAuthorizationLimitExceeded **   
The number of Redshift-managed VPC endpoints per authorization has exceeded its limit.  
HTTP Status Code: 400

 ** EndpointsPerClusterLimitExceeded **   
The number of Redshift-managed VPC endpoints per cluster has exceeded its limit.  
HTTP Status Code: 400

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

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
<a name="API_CreateEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateEndpointAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateEndpointAccess) 