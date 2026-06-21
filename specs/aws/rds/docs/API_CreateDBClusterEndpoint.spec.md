---
id: "@specs/aws/rds/docs/API_CreateDBClusterEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBClusterEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBClusterEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBClusterEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBClusterEndpoint
<a name="API_CreateDBClusterEndpoint"></a>

Creates a new custom endpoint and associates it with an Amazon Aurora DB cluster.

**Note**  
This action applies only to Aurora DB clusters.

## Request Parameters
<a name="API_CreateDBClusterEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterEndpointIdentifier **   
The identifier to use for the new endpoint. This parameter is stored as a lowercase string.  
Type: String  
Required: Yes

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String  
Required: Yes

 ** EndpointType **   
The type of the endpoint, one of: `READER`, `WRITER`, `ANY`.  
Type: String  
Required: Yes

 **ExcludedMembers.member.N**   
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. This parameter is relevant only if the list of static members is empty.  
Type: Array of strings  
Required: No

 **StaticMembers.member.N**   
List of DB instance identifiers that are part of the custom endpoint group.  
Type: Array of strings  
Required: No

 **Tags.Tag.N**   
The tags to be assigned to the Amazon RDS resource.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBClusterEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 ** CustomEndpointType **   
The type associated with a custom endpoint. One of: `READER`, `WRITER`, `ANY`.  
Type: String

 ** DBClusterEndpointArn **   
The Amazon Resource Name (ARN) for the endpoint.  
Type: String

 ** DBClusterEndpointIdentifier **   
The identifier associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String

 ** DBClusterEndpointResourceIdentifier **   
A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.  
Type: String

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String

 ** Endpoint **   
The DNS address of the endpoint.  
Type: String

 ** EndpointType **   
The type of the endpoint. One of: `READER`, `WRITER`, `CUSTOM`.  
Type: String

 **ExcludedMembers.member.N**   
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.  
Type: Array of strings

 **StaticMembers.member.N**   
List of DB instance identifiers that are part of the custom endpoint group.  
Type: Array of strings

 ** Status **   
The current status of the endpoint. One of: `creating`, `available`, `deleting`, `inactive`, `modifying`. The `inactive` state applies to an endpoint that can't be used for a certain kind of cluster, such as a `writer` endpoint for a read-only secondary cluster in a global database.  
Type: String

## Errors
<a name="API_CreateDBClusterEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterEndpointAlreadyExistsFault **   
The specified custom endpoint can't be created because it already exists.  
HTTP Status Code: 400

 ** DBClusterEndpointQuotaExceededFault **   
The cluster already has the maximum number of custom endpoints.  
HTTP Status Code: 403

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

## See Also
<a name="API_CreateDBClusterEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBClusterEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBClusterEndpoint) 