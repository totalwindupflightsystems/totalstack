---
id: "@specs/aws/appmesh/docs/API_CreateVirtualService"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVirtualService"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# CreateVirtualService

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_CreateVirtualService
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVirtualService
<a name="API_CreateVirtualService"></a>

Creates a virtual service within a service mesh.

A virtual service is an abstraction of a real service that is provided by a virtual node directly or indirectly by means of a virtual router. Dependent services call your virtual service by its `virtualServiceName`, and those requests are routed to the virtual node or virtual router that is specified as the provider for the virtual service.

For more information about virtual services, see [Virtual services](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html).

## Request Syntax
<a name="API_CreateVirtualService_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualServices?meshOwner={{meshOwner}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "spec": { 
      "provider": { ... }
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "virtualServiceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVirtualService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-uri-meshName"></a>
The name of the service mesh to create the virtual service in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

## Request Body
<a name="API_CreateVirtualService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-spec"></a>
The virtual service specification to apply.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object  
Required: Yes

 ** [tags](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-tags"></a>
Optional metadata that you can apply to the virtual service to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [virtualServiceName](#API_CreateVirtualService_RequestSyntax) **   <a name="appmesh-CreateVirtualService-request-virtualServiceName"></a>
The name to use for the virtual service.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CreateVirtualService_ResponseSyntax"></a>

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
      "provider": { ... }
   },
   "status": { 
      "status": "string"
   },
   "virtualServiceName": "string"
}
```

## Response Elements
<a name="API_CreateVirtualService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_CreateVirtualService_ResponseSyntax) **   <a name="appmesh-CreateVirtualService-response-meshName"></a>
The name of the service mesh that the virtual service resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_CreateVirtualService_ResponseSyntax) **   <a name="appmesh-CreateVirtualService-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_CreateVirtualService_ResponseSyntax) **   <a name="appmesh-CreateVirtualService-response-spec"></a>
The specifications of the virtual service.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object

 ** [status](#API_CreateVirtualService_ResponseSyntax) **   <a name="appmesh-CreateVirtualService-response-status"></a>
The current status of the virtual service.  
Type: [VirtualServiceStatus](API_VirtualServiceStatus.md) object

 ** [virtualServiceName](#API_CreateVirtualService_ResponseSyntax) **   <a name="appmesh-CreateVirtualService-response-virtualServiceName"></a>
The name of the virtual service.  
Type: String

## Errors
<a name="API_CreateVirtualService_Errors"></a>

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
<a name="API_CreateVirtualService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateVirtualService_Example_1"></a>

This example creates a virtual service named `colorgateway.default.svc.cluster.local` in the `ecs-mesh` service mesh. 

#### Sample Request
<a name="API_CreateVirtualService_Example_1_Request"></a>

```
PUT /v20190125/meshes/ecs-mesh/virtualServices HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T192448Z
Authorization: AUTHPARAMS

{
  "spec": {
    "provider": {
      "virtualNode": {
        "virtualNodeName": "colorgateway-vn"
      }
    }
  },
  "virtualServiceName": "colorgateway.default.svc.cluster.local",
  "clientToken": "0a263779-366d-400f-9c4c-0ab7ff0ef392"
}
```

#### Sample Response
<a name="API_CreateVirtualService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 6418af7b-e02b-4f0e-bb96-a3b4aab428c8
content-type: application/json
content-length: 456
date: Wed, 27 Feb 2019 19:24:48 GMT
x-envoy-upstream-service-time: 67
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/colorgateway.default.svc.cluster.local",
		"createdAt": 1.551295488701E9,
		"lastUpdatedAt": 1.551295488701E9,
		"uid": "f1b0ed85-7648-4be2-a0fc-c97865029c48",
		"version": 1
	},
	"spec": {
		"provider": {
			"virtualNode": {
				"virtualNodeName": "colorgateway-vn"
			},
			"virtualRouter": null
		}
	},
	"status": {
		"status": "ACTIVE"
	},
	"virtualServiceName": "colorgateway.default.svc.cluster.local"
}
```

## See Also
<a name="API_CreateVirtualService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/CreateVirtualService) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/CreateVirtualService) 