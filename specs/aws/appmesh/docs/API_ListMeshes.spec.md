---
id: "@specs/aws/appmesh/docs/API_ListMeshes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListMeshes"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListMeshes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListMeshes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListMeshes
<a name="API_ListMeshes"></a>

Returns a list of existing service meshes.

## Request Syntax
<a name="API_ListMeshes_RequestSyntax"></a>

```
GET /v20190125/meshes?limit={{limit}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMeshes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_ListMeshes_RequestSyntax) **   <a name="appmesh-ListMeshes-request-uri-limit"></a>
The maximum number of results returned by `ListMeshes` in paginated output. When you use this parameter, `ListMeshes` returns only `limit` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListMeshes` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListMeshes` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListMeshes_RequestSyntax) **   <a name="appmesh-ListMeshes-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListMeshes` request where `limit` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.

## Request Body
<a name="API_ListMeshes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMeshes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "meshes": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "lastUpdatedAt": number,
         "meshName": "string",
         "meshOwner": "string",
         "resourceOwner": "string",
         "version": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMeshes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshes](#API_ListMeshes_ResponseSyntax) **   <a name="appmesh-ListMeshes-response-meshes"></a>
The list of existing service meshes.  
Type: Array of [MeshRef](API_MeshRef.md) objects

 ** [nextToken](#API_ListMeshes_ResponseSyntax) **   <a name="appmesh-ListMeshes-response-nextToken"></a>
The `nextToken` value to include in a future `ListMeshes` request. When the results of a `ListMeshes` request exceed `limit`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListMeshes_Errors"></a>

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
<a name="API_ListMeshes_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListMeshes_Example_1"></a>

This example lists the service meshes for an account in the `us-east-1` Region.

#### Sample Request
<a name="API_ListMeshes_Example_1_Request"></a>

```
GET /v20190125/meshes HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T235715Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListMeshes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 572dcc56-18d6-4f86-b596-8e182f81afce
content-type: application/json
content-length: 114
date: Wed, 27 Feb 2019 23:57:15 GMT
x-envoy-upstream-service-time: 67
server: envoy
Connection: keep-alive

{
  "meshes": [
    {
      "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh",
      "meshName": "ecs-mesh"
    }
  ],
  "nextToken": null
}
```

## See Also
<a name="API_ListMeshes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/ListMeshes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListMeshes) 