---
id: "@specs/aws/appmesh/docs/API_ListGatewayRoutes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListGatewayRoutes"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListGatewayRoutes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListGatewayRoutes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListGatewayRoutes
<a name="API_ListGatewayRoutes"></a>

Returns a list of existing gateway routes that are associated to a virtual gateway.

## Request Syntax
<a name="API_ListGatewayRoutes_RequestSyntax"></a>

```
GET /v20190125/meshes/{{meshName}}/virtualGateway/{{virtualGatewayName}}/gatewayRoutes?limit={{limit}}&meshOwner={{meshOwner}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGatewayRoutes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_ListGatewayRoutes_RequestSyntax) **   <a name="appmesh-ListGatewayRoutes-request-uri-limit"></a>
The maximum number of results returned by `ListGatewayRoutes` in paginated output. When you use this parameter, `ListGatewayRoutes` returns only `limit` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListGatewayRoutes` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListGatewayRoutes` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [meshName](#API_ListGatewayRoutes_RequestSyntax) **   <a name="appmesh-ListGatewayRoutes-request-uri-meshName"></a>
The name of the service mesh to list gateway routes in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_ListGatewayRoutes_RequestSyntax) **   <a name="appmesh-ListGatewayRoutes-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [nextToken](#API_ListGatewayRoutes_RequestSyntax) **   <a name="appmesh-ListGatewayRoutes-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListGatewayRoutes` request where `limit` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

 ** [virtualGatewayName](#API_ListGatewayRoutes_RequestSyntax) **   <a name="appmesh-ListGatewayRoutes-request-uri-virtualGatewayName"></a>
The name of the virtual gateway to list gateway routes in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_ListGatewayRoutes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGatewayRoutes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayRoutes": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "gatewayRouteName": "string",
         "lastUpdatedAt": number,
         "meshName": "string",
         "meshOwner": "string",
         "resourceOwner": "string",
         "version": number,
         "virtualGatewayName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGatewayRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayRoutes](#API_ListGatewayRoutes_ResponseSyntax) **   <a name="appmesh-ListGatewayRoutes-response-gatewayRoutes"></a>
The list of existing gateway routes for the specified service mesh and virtual gateway.  
Type: Array of [GatewayRouteRef](API_GatewayRouteRef.md) objects

 ** [nextToken](#API_ListGatewayRoutes_ResponseSyntax) **   <a name="appmesh-ListGatewayRoutes-response-nextToken"></a>
The `nextToken` value to include in a future `ListGatewayRoutes` request. When the results of a `ListGatewayRoutes` request exceed `limit`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListGatewayRoutes_Errors"></a>

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
<a name="API_ListGatewayRoutes_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListGatewayRoutes_Example_1"></a>

The following example lists gateway routes that are associated with the virtual gateway named `myVirtualGateway` in the `apps` service mesh. 

#### Sample Request
<a name="API_ListGatewayRoutes_Example_1_Request"></a>

```
GET /v20190125/meshes/apps/virtualGateway/myVirtualGateway/gatewayRoutes HTTP/1.1
Host: appmesh.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200608T190053Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListGatewayRoutes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: b82c3691-a7a9-4d99-acf6-0f9a81db9beb
content-type: application/json
content-length: 393
date: Mon, 08 Jun 2020 20:52:25 GMT
x-envoy-upstream-service-time: 26
server: envoy
Connection: keep-alive

{
	"gatewayRoutes": [{
		"arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualGateway/myVirtualGateway/gatewayRoute/myGatewayRoute",
		"createdAt": 1.591642091122E9,
		"gatewayRouteName": "myGatewayRoute",
		"lastUpdatedAt": 1.591642091122E9,
		"meshName": "myApps",
		"meshOwner": "123456789012",
		"resourceOwner": "123456789012",
		"version": 1,
		"virtualGatewayName": "myVirtualGateway"
	}],
	"nextToken": null
}
```

## See Also
<a name="API_ListGatewayRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/ListGatewayRoutes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListGatewayRoutes) 