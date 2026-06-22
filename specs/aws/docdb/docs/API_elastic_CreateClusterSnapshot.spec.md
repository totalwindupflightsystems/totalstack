---
id: "@specs/aws/docdb/docs/API_elastic_CreateClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CreateClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_CreateClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateClusterSnapshot
<a name="API_elastic_CreateClusterSnapshot"></a>

Creates a snapshot of an elastic cluster.

## Request Syntax
<a name="API_elastic_CreateClusterSnapshot_RequestSyntax"></a>

```
POST /cluster-snapshot HTTP/1.1
Content-type: application/json

{
   "clusterArn": "{{string}}",
   "snapshotName": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_elastic_CreateClusterSnapshot_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_elastic_CreateClusterSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clusterArn](#API_elastic_CreateClusterSnapshot_RequestSyntax) **   <a name="documentdb-elastic_CreateClusterSnapshot-request-clusterArn"></a>
The ARN identifier of the elastic cluster of which you want to create a snapshot.  
Type: String  
Required: Yes

 ** [snapshotName](#API_elastic_CreateClusterSnapshot_RequestSyntax) **   <a name="documentdb-elastic_CreateClusterSnapshot-request-snapshotName"></a>
The name of the new elastic cluster snapshot.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: Yes

 ** [tags](#API_elastic_CreateClusterSnapshot_RequestSyntax) **   <a name="documentdb-elastic_CreateClusterSnapshot-request-tags"></a>
The tags to be assigned to the new elastic cluster snapshot.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_elastic_CreateClusterSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "snapshot": { 
      "adminUserName": "string",
      "clusterArn": "string",
      "clusterCreationTime": "string",
      "kmsKeyId": "string",
      "snapshotArn": "string",
      "snapshotCreationTime": "string",
      "snapshotName": "string",
      "snapshotType": "string",
      "status": "string",
      "subnetIds": [ "string" ],
      "vpcSecurityGroupIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_elastic_CreateClusterSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshot](#API_elastic_CreateClusterSnapshot_ResponseSyntax) **   <a name="documentdb-elastic_CreateClusterSnapshot-response-snapshot"></a>
Returns information about the new elastic cluster snapshot.  
Type: [ClusterSnapshot](API_elastic_ClusterSnapshot.md) object

## Errors
<a name="API_elastic_CreateClusterSnapshot_Errors"></a>

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
<a name="API_elastic_CreateClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/CreateClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/CreateClusterSnapshot) 