---
id: "@specs/aws/appmesh/docs/API_ListVirtualServices"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVirtualServices"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListVirtualServices

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListVirtualServices
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVirtualServices
<a name="API_ListVirtualServices"></a>

Returns a list of existing virtual services in a service mesh.

## Request Syntax
<a name="API_ListVirtualServices_RequestSyntax"></a>

```
GET /v20190125/meshes/{{meshName}}/virtualServices?limit={{limit}}&meshOwner={{meshOwner}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVirtualServices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_ListVirtualServices_RequestSyntax) **   <a name="appmesh-ListVirtualServices-request-uri-limit"></a>
The maximum number of results returned by `ListVirtualServices` in paginated output. When you use this parameter, `ListVirtualServices` returns only `limit` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListVirtualServices` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListVirtualServices` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [meshName](#API_ListVirtualServices_RequestSyntax) **   <a name="appmesh-ListVirtualServices-request-uri-meshName"></a>
The name of the service mesh to list virtual services in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_ListVirtualServices_RequestSyntax) **   <a name="appmesh-ListVirtualServices-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [nextToken](#API_ListVirtualServices_RequestSyntax) **   <a name="appmesh-ListVirtualServices-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListVirtualServices` request where `limit` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

## Request Body
<a name="API_ListVirtualServices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVirtualServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "virtualServices": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "lastUpdatedAt": number,
         "meshName": "string",
         "meshOwner": "string",
         "resourceOwner": "string",
         "version": number,
         "virtualServiceName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVirtualServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVirtualServices_ResponseSyntax) **   <a name="appmesh-ListVirtualServices-response-nextToken"></a>
The `nextToken` value to include in a future `ListVirtualServices` request. When the results of a `ListVirtualServices` request exceed `limit`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [virtualServices](#API_ListVirtualServices_ResponseSyntax) **   <a name="appmesh-ListVirtualServices-response-virtualServices"></a>
The list of existing virtual services for the specified service mesh.  
Type: Array of [VirtualServiceRef](API_VirtualServiceRef.md) objects

## Errors
<a name="API_ListVirtualServices_Errors"></a>

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
<a name="API_ListVirtualServices_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListVirtualServices_Example_1"></a>

This example lists the virtual services in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_ListVirtualServices_Example_1_Request"></a>

```
GET /v20190125/meshes/ecs-mesh/virtualServices HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T235746Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListVirtualServices_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 1e2ccc92-46aa-4541-ae10-9790266e7436
content-type: application/json
content-length: 629
date: Wed, 27 Feb 2019 23:57:46 GMT
x-envoy-upstream-service-time: 9
server: envoy
Connection: keep-alive

{
  "nextToken": null,
  "virtualServices": [
    {
      "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/tcpecho.default.svc.cluster.local",
      "meshName": "ecs-mesh",
      "virtualServiceName": "tcpecho.default.svc.cluster.local"
    },
    {
      "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/colorteller.default.svc.cluster.local",
      "meshName": "ecs-mesh",
      "virtualServiceName": "colorteller.default.svc.cluster.local"
    },
    {
      "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualService/colorgateway.default.svc.cluster.local",
      "meshName": "ecs-mesh",
      "virtualServiceName": "colorgateway.default.svc.cluster.local"
    }
  ]
}
```

## See Also
<a name="API_ListVirtualServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/ListVirtualServices) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListVirtualServices) 