---
id: "@specs/aws/appmesh/docs/API_CreateMesh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateMesh"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# CreateMesh

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_CreateMesh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateMesh
<a name="API_CreateMesh"></a>

Creates a service mesh.

 A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.

For more information about service meshes, see [Service meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html).

## Request Syntax
<a name="API_CreateMesh_RequestSyntax"></a>

```
PUT /v20190125/meshes HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "meshName": "{{string}}",
   "spec": { 
      "egressFilter": { 
         "type": "{{string}}"
      },
      "serviceDiscovery": { 
         "ipPreference": "{{string}}"
      }
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMesh_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMesh_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateMesh_RequestSyntax) **   <a name="appmesh-CreateMesh-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [meshName](#API_CreateMesh_RequestSyntax) **   <a name="appmesh-CreateMesh-request-meshName"></a>
The name to use for the service mesh.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [spec](#API_CreateMesh_RequestSyntax) **   <a name="appmesh-CreateMesh-request-spec"></a>
The service mesh specification to apply.  
Type: [MeshSpec](API_MeshSpec.md) object  
Required: No

 ** [tags](#API_CreateMesh_RequestSyntax) **   <a name="appmesh-CreateMesh-request-tags"></a>
Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateMesh_ResponseSyntax"></a>

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
<a name="API_CreateMesh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_CreateMesh_ResponseSyntax) **   <a name="appmesh-CreateMesh-response-meshName"></a>
The name of the service mesh.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_CreateMesh_ResponseSyntax) **   <a name="appmesh-CreateMesh-response-metadata"></a>
The associated metadata for the service mesh.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_CreateMesh_ResponseSyntax) **   <a name="appmesh-CreateMesh-response-spec"></a>
The associated specification for the service mesh.  
Type: [MeshSpec](API_MeshSpec.md) object

 ** [status](#API_CreateMesh_ResponseSyntax) **   <a name="appmesh-CreateMesh-response-status"></a>
The status of the service mesh.  
Type: [MeshStatus](API_MeshStatus.md) object

## Errors
<a name="API_CreateMesh_Errors"></a>

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

 ** LimitExceededException **   
You have exceeded a service limit for your account. For more information, see [Service Limits](https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html) in the * AWS App Mesh User Guide*.  
HTTP Status Code: 400

 ** NotFoundException **   
The specified resource doesn't exist. Check your request syntax and try again.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## Examples
<a name="API_CreateMesh_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateMesh_Example_1"></a>

The following example creates a service mesh named `ecs-mesh`.

#### Sample Request
<a name="API_CreateMesh_Example_1_Request"></a>

```
PUT /v20190125/meshes HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T192324Z
Authorization: AUTHPARAMS

{
  "meshName": "ecs-mesh",
  "clientToken": "34a20934-da3a-43a0-9d1b-390308a7393b"
}
```

#### Sample Response
<a name="API_CreateMesh_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 5c2f774d-da0b-40f3-80c5-d8711eb15dce
content-type: application/json
content-length: 245
date: Wed, 27 Feb 2019 19:23:24 GMT
x-envoy-upstream-service-time: 76
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh",
		"createdAt": 1.551295405298E9,
		"lastUpdatedAt": 1.551295405298E9,
		"uid": "2d29a11c-f2dd-44a6-b620-33661cfdfe97",
		"version": 1
	},
	"status": {
		"status": "ACTIVE"
	}
}
```

## See Also
<a name="API_CreateMesh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/CreateMesh) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/CreateMesh) 