---
id: "@specs/aws/appmesh/docs/API_DescribeVirtualRouter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVirtualRouter"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DescribeVirtualRouter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DescribeVirtualRouter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVirtualRouter
<a name="API_DescribeVirtualRouter"></a>

Describes an existing virtual router.

## Request Syntax
<a name="API_DescribeVirtualRouter_RequestSyntax"></a>

```
GET /v20190125/meshes/{{meshName}}/virtualRouters/{{virtualRouterName}}?meshOwner={{meshOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVirtualRouter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_DescribeVirtualRouter_RequestSyntax) **   <a name="appmesh-DescribeVirtualRouter-request-uri-meshName"></a>
The name of the service mesh that the virtual router resides in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_DescribeVirtualRouter_RequestSyntax) **   <a name="appmesh-DescribeVirtualRouter-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualRouterName](#API_DescribeVirtualRouter_RequestSyntax) **   <a name="appmesh-DescribeVirtualRouter-request-uri-virtualRouterName"></a>
The name of the virtual router to describe.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_DescribeVirtualRouter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVirtualRouter_ResponseSyntax"></a>

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
      "listeners": [ 
         { 
            "portMapping": { 
               "port": number,
               "protocol": "string"
            }
         }
      ]
   },
   "status": { 
      "status": "string"
   },
   "virtualRouterName": "string"
}
```

## Response Elements
<a name="API_DescribeVirtualRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_DescribeVirtualRouter_ResponseSyntax) **   <a name="appmesh-DescribeVirtualRouter-response-meshName"></a>
The name of the service mesh that the virtual router resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_DescribeVirtualRouter_ResponseSyntax) **   <a name="appmesh-DescribeVirtualRouter-response-metadata"></a>
The associated metadata for the virtual router.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_DescribeVirtualRouter_ResponseSyntax) **   <a name="appmesh-DescribeVirtualRouter-response-spec"></a>
The specifications of the virtual router.  
Type: [VirtualRouterSpec](API_VirtualRouterSpec.md) object

 ** [status](#API_DescribeVirtualRouter_ResponseSyntax) **   <a name="appmesh-DescribeVirtualRouter-response-status"></a>
The current status of the virtual router.  
Type: [VirtualRouterStatus](API_VirtualRouterStatus.md) object

 ** [virtualRouterName](#API_DescribeVirtualRouter_ResponseSyntax) **   <a name="appmesh-DescribeVirtualRouter-response-virtualRouterName"></a>
The name of the virtual router.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DescribeVirtualRouter_Errors"></a>

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

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## Examples
<a name="API_DescribeVirtualRouter_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeVirtualRouter_Example_1"></a>

This example describes a virtual router named `colorteller-vr` in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_DescribeVirtualRouter_Example_1_Request"></a>

```
GET /v20190125/meshes/ecs-mesh/virtualRouters/colorteller-vr HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190228T000509Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVirtualRouter_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: e7e0fbe8-2015-429c-bbb5-c736c09b2500
content-type: application/json
content-length: 337
date: Thu, 28 Feb 2019 00:05:10 GMT
x-envoy-upstream-service-time: 68
server: envoy
Connection: keep-alive

{
  "meshName": "ecs-mesh",
  "metadata": {
    "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualRouter/colorteller-vr",
    "createdAt": 1551311805.476,
    "lastUpdatedAt": 1551311805.476,
    "uid": "79628d34-8c17-42ba-83a5-8a42fd17ec5a",
    "version": 1
  },
  "spec": {
    "listeners": [
      {
        "portMapping": {
          "port": 9080,
          "protocol": "http"
        }
      }
    ]
  },
  "status": {
    "status": "ACTIVE"
  },
  "virtualRouterName": "colorteller-vr"
}
```

## See Also
<a name="API_DescribeVirtualRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/DescribeVirtualRouter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DescribeVirtualRouter) 