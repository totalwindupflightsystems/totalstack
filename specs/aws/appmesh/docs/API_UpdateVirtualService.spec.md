---
id: "@specs/aws/appmesh/docs/API_UpdateVirtualService"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateVirtualService"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# UpdateVirtualService

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_UpdateVirtualService
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateVirtualService
<a name="API_UpdateVirtualService"></a>

Updates an existing virtual service in a specified service mesh.

## Request Syntax
<a name="API_UpdateVirtualService_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualServices/{{virtualServiceName}}?meshOwner={{meshOwner}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "spec": { 
      "provider": { ... }
   }
}
```

## URI Request Parameters
<a name="API_UpdateVirtualService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_UpdateVirtualService_RequestSyntax) **   <a name="appmesh-UpdateVirtualService-request-uri-meshName"></a>
The name of the service mesh that the virtual service resides in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_UpdateVirtualService_RequestSyntax) **   <a name="appmesh-UpdateVirtualService-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualServiceName](#API_UpdateVirtualService_RequestSyntax) **   <a name="appmesh-UpdateVirtualService-request-uri-virtualServiceName"></a>
The name of the virtual service to update.  
Required: Yes

## Request Body
<a name="API_UpdateVirtualService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateVirtualService_RequestSyntax) **   <a name="appmesh-UpdateVirtualService-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_UpdateVirtualService_RequestSyntax) **   <a name="appmesh-UpdateVirtualService-request-spec"></a>
The new virtual service specification to apply. This overwrites the existing data.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateVirtualService_ResponseSyntax"></a>

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
<a name="API_UpdateVirtualService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_UpdateVirtualService_ResponseSyntax) **   <a name="appmesh-UpdateVirtualService-response-meshName"></a>
The name of the service mesh that the virtual service resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_UpdateVirtualService_ResponseSyntax) **   <a name="appmesh-UpdateVirtualService-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_UpdateVirtualService_ResponseSyntax) **   <a name="appmesh-UpdateVirtualService-response-spec"></a>
The specifications of the virtual service.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object

 ** [status](#API_UpdateVirtualService_ResponseSyntax) **   <a name="appmesh-UpdateVirtualService-response-status"></a>
The current status of the virtual service.  
Type: [VirtualServiceStatus](API_VirtualServiceStatus.md) object

 ** [virtualServiceName](#API_UpdateVirtualService_ResponseSyntax) **   <a name="appmesh-UpdateVirtualService-response-virtualServiceName"></a>
The name of the virtual service.  
Type: String

## Errors
<a name="API_UpdateVirtualService_Errors"></a>

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
<a name="API_UpdateVirtualService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateVirtualService_Example_1"></a>

This example updates a virtual service named `colorgateway.default.svc.cluster.local` in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_UpdateVirtualService_Example_1_Request"></a>

```
PUT /v20190125/meshes/ecs-mesh/virtualServices/colorgateway.default.svc.cluster.local HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190228T002829Z
Authorization: AUTHPARAMS

{
  "spec": {
    "provider": {
      "virtualNode": {
        "virtualNodeName": "colorgateway-vn"
      }
    }
  },
  "clientToken": "c207a9a1-5828-4d73-9e8e-1d3b9350b2ac"
}
```

#### Sample Response
<a name="API_UpdateVirtualService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 60d5fb65-ac74-4523-a1df-9e56da84fa84
content-type: application/json
content-length: 456
date: Thu, 28 Feb 2019 00:28:29 GMT
x-envoy-upstream-service-time: 88
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/colorgateway.default.svc.cluster.local",
		"createdAt": 1.551311807444E9,
		"lastUpdatedAt": 1.551313709898E9,
		"uid": "dd06064b-e542-40a9-bbc7-e381a47ea0e0",
		"version": 2
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
<a name="API_UpdateVirtualService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/UpdateVirtualService) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/UpdateVirtualService) 