---
id: "@specs/aws/rds/docs/API_DBClusterEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterEndpoint
<a name="API_DBClusterEndpoint"></a>

This data type represents the information you need to connect to an Amazon Aurora DB cluster. This data type is used as a response element in the following actions:
+  `CreateDBClusterEndpoint` 
+  `DescribeDBClusterEndpoints` 
+  `ModifyDBClusterEndpoint` 
+  `DeleteDBClusterEndpoint` 

For the data structure that represents Amazon RDS DB instance endpoints, see `Endpoint`.

## Contents
<a name="API_DBClusterEndpoint_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CustomEndpointType **   
The type associated with a custom endpoint. One of: `READER`, `WRITER`, `ANY`.  
Type: String  
Required: No

 ** DBClusterEndpointArn **   
The Amazon Resource Name (ARN) for the endpoint.  
Type: String  
Required: No

 ** DBClusterEndpointIdentifier **   
The identifier associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String  
Required: No

 ** DBClusterEndpointResourceIdentifier **   
A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.  
Type: String  
Required: No

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.  
Type: String  
Required: No

 ** Endpoint **   
The DNS address of the endpoint.  
Type: String  
Required: No

 ** EndpointType **   
The type of the endpoint. One of: `READER`, `WRITER`, `CUSTOM`.  
Type: String  
Required: No

 ** ExcludedMembers.member.N **   
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.  
Type: Array of strings  
Required: No

 ** StaticMembers.member.N **   
List of DB instance identifiers that are part of the custom endpoint group.  
Type: Array of strings  
Required: No

 ** Status **   
The current status of the endpoint. One of: `creating`, `available`, `deleting`, `inactive`, `modifying`. The `inactive` state applies to an endpoint that can't be used for a certain kind of cluster, such as a `writer` endpoint for a read-only secondary cluster in a global database.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterEndpoint) 