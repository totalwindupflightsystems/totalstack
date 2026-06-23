---
id: "@specs/aws/appmesh/docs/API_ListRoutes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRoutes"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListRoutes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListRoutes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRoutes
<a name="API_ListRoutes"></a>

Returns a list of existing routes in a service mesh.

## Request Syntax
<a name="API_ListRoutes_RequestSyntax"></a>

```
GET /v20190125/meshes/{{meshName}}/virtualRouter/{{virtualRouterName}}/routes?limit={{limit}}&meshOwner={{meshOwner}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRoutes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_ListRoutes_RequestSyntax) **   <a name="appmesh-ListRoutes-request-uri-limit"></a>
The maximum number of results returned by `ListRoutes` in paginated output. When you use this parameter, `ListRoutes` returns only `limit` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListRoutes` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListRoutes` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [meshName](#API_ListRoutes_RequestSyntax) **   <a name="appmesh-ListRoutes-request-uri-meshName"></a>
The name of the service mesh to list routes in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_ListRoutes_RequestSyntax) **   <a name="appmesh-ListRoutes-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [nextToken](#API_ListRoutes_RequestSyntax) **   <a name="appmesh-ListRoutes-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListRoutes` request where `limit` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

 ** [virtualRouterName](#API_ListRoutes_RequestSyntax) **   <a name="appmesh-ListRoutes-request-uri-virtualRouterName"></a>
The name of the virtual router to list routes in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_ListRoutes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRoutes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "routes": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "lastUpdatedAt": number,
         "meshName": "string",
         "meshOwner": "string",
         "resourceOwner": "string",
         "routeName": "string",
         "version": number,
         "virtualRouterName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRoutes_ResponseSyntax) **   <a name="appmesh-ListRoutes-response-nextToken"></a>
The `nextToken` value to include in a future `ListRoutes` request. When the results of a `ListRoutes` request exceed `limit`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [routes](#API_ListRoutes_ResponseSyntax) **   <a name="appmesh-ListRoutes-response-routes"></a>
The list of existing routes for the specified service mesh and virtual router.  
Type: Array of [RouteRef](API_RouteRef.md) objects

## Errors
<a name="API_ListRoutes_Errors"></a>

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
<a name="API_ListRoutes_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListRoutes_Example_1"></a>

The following example lists the routes that are associated with the `colorteller-vr` virtual router in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_ListRoutes_Example_1_Request"></a>

```
GET /v20190125/meshes/ecs-mesh/virtualRouter/colorteller-vr/routes HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T235954Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListRoutes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 5a783529-a278-44d2-b450-4e23898cb180
content-type: application/json
content-length: 236
date: Wed, 27 Feb 2019 23:59:54 GMT
x-envoy-upstream-service-time: 56
server: envoy
Connection: keep-alive

{
  "nextToken": null,
  "routes": [
    {
      "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualRouter/colorteller-vr/route/colorteller-route",
      "meshName": "ecs-mesh",
      "routeName": "colorteller-route",
      "virtualRouterName": "colorteller-vr"
    }
  ]
}
```

## See Also
<a name="API_ListRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/ListRoutes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListRoutes) 