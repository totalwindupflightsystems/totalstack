---
id: "@specs/aws/appmesh/docs/API_DeleteVirtualService"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteVirtualService"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DeleteVirtualService

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DeleteVirtualService
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteVirtualService
<a name="API_DeleteVirtualService"></a>

Deletes an existing virtual service.

## Request Syntax
<a name="API_DeleteVirtualService_RequestSyntax"></a>

```
DELETE /v20190125/meshes/{{meshName}}/virtualServices/{{virtualServiceName}}?meshOwner={{meshOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteVirtualService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_DeleteVirtualService_RequestSyntax) **   <a name="appmesh-DeleteVirtualService-request-uri-meshName"></a>
The name of the service mesh to delete the virtual service in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_DeleteVirtualService_RequestSyntax) **   <a name="appmesh-DeleteVirtualService-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualServiceName](#API_DeleteVirtualService_RequestSyntax) **   <a name="appmesh-DeleteVirtualService-request-uri-virtualServiceName"></a>
The name of the virtual service to delete.  
Required: Yes

## Request Body
<a name="API_DeleteVirtualService_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteVirtualService_ResponseSyntax"></a>

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
<a name="API_DeleteVirtualService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_DeleteVirtualService_ResponseSyntax) **   <a name="appmesh-DeleteVirtualService-response-meshName"></a>
The name of the service mesh that the virtual service resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_DeleteVirtualService_ResponseSyntax) **   <a name="appmesh-DeleteVirtualService-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_DeleteVirtualService_ResponseSyntax) **   <a name="appmesh-DeleteVirtualService-response-spec"></a>
The specifications of the virtual service.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object

 ** [status](#API_DeleteVirtualService_ResponseSyntax) **   <a name="appmesh-DeleteVirtualService-response-status"></a>
The current status of the virtual service.  
Type: [VirtualServiceStatus](API_VirtualServiceStatus.md) object

 ** [virtualServiceName](#API_DeleteVirtualService_ResponseSyntax) **   <a name="appmesh-DeleteVirtualService-response-virtualServiceName"></a>
The name of the virtual service.  
Type: String

## Errors
<a name="API_DeleteVirtualService_Errors"></a>

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
<a name="API_DeleteVirtualService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteVirtualService_Example_1"></a>

This example deletes a virtual service named `colorgateway.default.svc.cluster.local` in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_DeleteVirtualService_Example_1_Request"></a>

```
DELETE /v20190125/meshes/ecs-mesh/virtualServices/colorgateway.default.svc.cluster.local HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T231318Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVirtualService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 8a5c10db-aebc-4341-8b15-4003e87150e8
content-type: application/json
content-length: 456
date: Wed, 27 Feb 2019 23:13:18 GMT
x-envoy-upstream-service-time: 78
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/colorgateway.default.svc.cluster.local",
		"createdAt": 1.551307250696E9,
		"lastUpdatedAt": 1.55130919872E9,
		"uid": "90849766-3af0-40bc-9a83-a7b932d64fb6",
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
		"status": "DELETED"
	},
	"virtualServiceName": "colorgateway.default.svc.cluster.local"
}
```

## See Also
<a name="API_DeleteVirtualService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/DeleteVirtualService) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DeleteVirtualService) 