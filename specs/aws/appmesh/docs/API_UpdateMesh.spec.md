---
id: "@specs/aws/appmesh/docs/API_UpdateMesh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateMesh"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# UpdateMesh

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_UpdateMesh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateMesh
<a name="API_UpdateMesh"></a>

Updates an existing service mesh.

## Request Syntax
<a name="API_UpdateMesh_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "spec": { 
      "egressFilter": { 
         "type": "{{string}}"
      },
      "serviceDiscovery": { 
         "ipPreference": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateMesh_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_UpdateMesh_RequestSyntax) **   <a name="appmesh-UpdateMesh-request-uri-meshName"></a>
The name of the service mesh to update.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_UpdateMesh_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateMesh_RequestSyntax) **   <a name="appmesh-UpdateMesh-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_UpdateMesh_RequestSyntax) **   <a name="appmesh-UpdateMesh-request-spec"></a>
The service mesh specification to apply.  
Type: [MeshSpec](API_MeshSpec.md) object  
Required: No

## Response Syntax
<a name="API_UpdateMesh_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "meshName": "string",
   "metadata": { 
      "arn": "string",
      "createdAt": number,
      "lastUpdatedAt": number,
      "meshOwner": "string",
      "resourceOwner": "string",
      "uid": "string",
      "version": number
   },
   "spec": { 
      "egressFilter": { 
         "type": "string"
      },
      "serviceDiscovery": { 
         "ipPreference": "string"
      }
   },
   "status": { 
      "status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateMesh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_UpdateMesh_ResponseSyntax) **   <a name="appmesh-UpdateMesh-response-meshName"></a>
The name of the service mesh.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_UpdateMesh_ResponseSyntax) **   <a name="appmesh-UpdateMesh-response-metadata"></a>
The associated metadata for the service mesh.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_UpdateMesh_ResponseSyntax) **   <a name="appmesh-UpdateMesh-response-spec"></a>
The associated specification for the service mesh.  
Type: [MeshSpec](API_MeshSpec.md) object

 ** [status](#API_UpdateMesh_ResponseSyntax) **   <a name="appmesh-UpdateMesh-response-status"></a>
The status of the service mesh.  
Type: [MeshStatus](API_MeshStatus.md) object

## Errors
<a name="API_UpdateMesh_Errors"></a>

 ** BadRequestException **   
The request syntax was malformed. Check your request syntax and try again.  
HTTP Status Code: 400

 ** ConflictException **   
The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.  
HTTP Status Code: 409

 ** ForbiddenException **   
You don't have permissions to perform this action.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
The request processing has failed because of an unknown error, exception, or failure.  
HTTP Status Code: 500

 ** NotFoundException **   
The specified resource doesn't exist. Check your request syntax and try again.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## See Also
<a name="API_UpdateMesh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/UpdateMesh) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/UpdateMesh) 