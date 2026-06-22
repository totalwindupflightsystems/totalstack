---
id: "@specs/aws/docdb/docs/API_elastic_DeleteCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_DeleteCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCluster
<a name="API_elastic_DeleteCluster"></a>

Delete an elastic cluster.

## Request Syntax
<a name="API_elastic_DeleteCluster_RequestSyntax"></a>

```
DELETE /cluster/{{clusterArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_elastic_DeleteCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterArn](#API_elastic_DeleteCluster_RequestSyntax) **   <a name="documentdb-elastic_DeleteCluster-request-uri-clusterArn"></a>
The ARN identifier of the elastic cluster that is to be deleted.  
Required: Yes

## Request Body
<a name="API_elastic_DeleteCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_elastic_DeleteCluster_ResponseSyntax"></a>

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
<a name="API_elastic_DeleteCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_elastic_DeleteCluster_ResponseSyntax) **   <a name="documentdb-elastic_DeleteCluster-response-cluster"></a>
Returns information about the newly deleted elastic cluster.  
Type: [Cluster](API_elastic_Cluster.md) object

## Errors
<a name="API_elastic_DeleteCluster_Errors"></a>

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
<a name="API_elastic_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/DeleteCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/DeleteCluster) 