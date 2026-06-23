---
id: "@specs/aws/appmesh/docs/API_DeleteMesh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteMesh"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DeleteMesh

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DeleteMesh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteMesh
<a name="API_DeleteMesh"></a>

Deletes an existing service mesh.

You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.

## Request Syntax
<a name="API_DeleteMesh_RequestSyntax"></a>

```
DELETE /v20190125/meshes/{{meshName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMesh_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_DeleteMesh_RequestSyntax) **   <a name="appmesh-DeleteMesh-request-uri-meshName"></a>
The name of the service mesh to delete.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_DeleteMesh_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMesh_ResponseSyntax"></a>

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
<a name="API_DeleteMesh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_DeleteMesh_ResponseSyntax) **   <a name="appmesh-DeleteMesh-response-meshName"></a>
The name of the service mesh.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_DeleteMesh_ResponseSyntax) **   <a name="appmesh-DeleteMesh-response-metadata"></a>
The associated metadata for the service mesh.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_DeleteMesh_ResponseSyntax) **   <a name="appmesh-DeleteMesh-response-spec"></a>
The associated specification for the service mesh.  
Type: [MeshSpec](API_MeshSpec.md) object

 ** [status](#API_DeleteMesh_ResponseSyntax) **   <a name="appmesh-DeleteMesh-response-status"></a>
The status of the service mesh.  
Type: [MeshStatus](API_MeshStatus.md) object

## Errors
<a name="API_DeleteMesh_Errors"></a>

 ** BadRequestException **   
The request syntax was malformed. Check your request syntax and try again.  
HTTP Status Code: 400

 ** ForbiddenException **   
You don't have permissions to perform this action.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
The request processing has failed because of an unknown error, exception, or failure.  
HTTP Status Code: 500

 ** NotFoundException **   
The specified resource doesn't exist. Check your request syntax and try again.  
HTTP Status Code: 404

 ** ResourceInUseException **   
You can't delete the specified resource because it's in use or required by another resource.  
HTTP Status Code: 409

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## Examples
<a name="API_DeleteMesh_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteMesh_Example_1"></a>

This example command deletes a service mesh named `ecs-mesh` in your default region.

#### Sample Request
<a name="API_DeleteMesh_Example_1_Request"></a>

```
DELETE /v20190125/meshes/ecs-mesh HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T203825Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteMesh_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 5b4e49f2-dac7-4782-8be3-1e81c8599e14
content-type: application/json
content-length: 246
date: Wed, 27 Feb 2019 20:38:25 GMT
x-envoy-upstream-service-time: 35
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh",
		"createdAt": 1.551295405298E9,
		"lastUpdatedAt": 1.551299905963E9,
		"uid": "2d29a11c-f2dd-44a6-b620-33661cfdfe97",
		"version": 1
	},
	"status": {
		"status": "DELETED"
	}
}
```

## See Also
<a name="API_DeleteMesh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/DeleteMesh) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DeleteMesh) 