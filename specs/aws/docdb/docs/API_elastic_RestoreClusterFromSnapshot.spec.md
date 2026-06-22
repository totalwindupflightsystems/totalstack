---
id: "@specs/aws/docdb/docs/API_elastic_RestoreClusterFromSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreClusterFromSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RestoreClusterFromSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_RestoreClusterFromSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreClusterFromSnapshot
<a name="API_elastic_RestoreClusterFromSnapshot"></a>

Restores an elastic cluster from a snapshot.

## Request Syntax
<a name="API_elastic_RestoreClusterFromSnapshot_RequestSyntax"></a>

```
POST /cluster-snapshot/{{snapshotArn}}/restore HTTP/1.1
Content-type: application/json

{
   "clusterName": "{{string}}",
   "kmsKeyId": "{{string}}",
   "shardCapacity": {{number}},
   "shardInstanceCount": {{number}},
   "subnetIds": [ "{{string}}" ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "vpcSecurityGroupIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_elastic_RestoreClusterFromSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [snapshotArn](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-uri-snapshotArn"></a>
The ARN identifier of the elastic cluster snapshot.  
Required: Yes

## Request Body
<a name="API_elastic_RestoreClusterFromSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clusterName](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-clusterName"></a>
The name of the elastic cluster.  
Type: String  
Required: Yes

 ** [kmsKeyId](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-kmsKeyId"></a>
The KMS key identifier to use to encrypt the new Amazon DocumentDB elastic clusters cluster.  
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.  
If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.  
Type: String  
Required: No

 ** [shardCapacity](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-shardCapacity"></a>
The capacity of each shard in the new restored elastic cluster.  
Type: Integer  
Required: No

 ** [shardInstanceCount](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-shardInstanceCount"></a>
The number of replica instances applying to all shards in the elastic cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.  
Type: Integer  
Required: No

 ** [subnetIds](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-subnetIds"></a>
The Amazon EC2 subnet IDs for the elastic cluster.  
Type: Array of strings  
Required: No

 ** [tags](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-tags"></a>
A list of the tag names to be assigned to the restored elastic cluster, in the form of an array of key-value pairs in which the key is the tag name and the value is the key value.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** [vpcSecurityGroupIds](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-request-vpcSecurityGroupIds"></a>
A list of EC2 VPC security groups to associate with the elastic cluster.  
Type: Array of strings  
Required: No

## Response Syntax
<a name="API_elastic_RestoreClusterFromSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cluster": { 
      "adminUserName": "string",
      "authType": "string",
      "backupRetentionPeriod": number,
      "clusterArn": "string",
      "clusterEndpoint": "string",
      "clusterName": "string",
      "createTime": "string",
      "kmsKeyId": "string",
      "preferredBackupWindow": "string",
      "preferredMaintenanceWindow": "string",
      "shardCapacity": number,
      "shardCount": number,
      "shardInstanceCount": number,
      "shards": [ 
         { 
            "createTime": "string",
            "shardId": "string",
            "status": "string"
         }
      ],
      "status": "string",
      "subnetIds": [ "string" ],
      "vpcSecurityGroupIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_elastic_RestoreClusterFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_elastic_RestoreClusterFromSnapshot_ResponseSyntax) **   <a name="documentdb-elastic_RestoreClusterFromSnapshot-response-cluster"></a>
Returns information about a the restored elastic cluster.  
Type: [Cluster](API_elastic_Cluster.md) object

## Errors
<a name="API_elastic_RestoreClusterFromSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
An exception that occurs when there are not sufficient permissions to perform an action.    
 ** message **   
An error message explaining why access was denied.
HTTP Status Code: 403

 ** ConflictException **   
There was an access conflict.    
 ** resourceId **   
The ID of the resource where there was an access conflict.  
 ** resourceType **   
The type of the resource where there was an access conflict.
HTTP Status Code: 409

 ** InternalServerException **   
There was an internal server error.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource could not be located.    
 ** message **   
An error message describing the failure.  
 ** resourceId **   
The ID of the resource that could not be located.  
 ** resourceType **   
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The service quota for the action was exceeded.  
HTTP Status Code: 402

 ** ThrottlingException **   
ThrottlingException will be thrown when request was denied due to request throttling.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **   
A structure defining a validation exception.    
 ** fieldList **   
A list of the fields in which the validation exception occurred.  
 ** message **   
An error message describing the validation exception.  
 ** reason **   
The reason why the validation exception occurred (one of `unknownOperation`, `cannotParse`, `fieldValidationFailed`, or `other`).
HTTP Status Code: 400

## See Also
<a name="API_elastic_RestoreClusterFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot) 