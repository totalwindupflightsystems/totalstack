---
id: "@specs/aws/appmesh/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

List the tags for an App Mesh resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /v20190125/tags?limit={{limit}}&nextToken={{nextToken}}&resourceArn={{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_ListTagsForResource_RequestSyntax) **   <a name="appmesh-ListTagsForResource-request-uri-limit"></a>
The maximum number of tag results returned by `ListTagsForResource` in paginated output. When this parameter is used, `ListTagsForResource` returns only `limit` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListTagsForResource` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListTagsForResource` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="appmesh-ListTagsForResource-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListTagsForResource` request where `limit` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="appmesh-ListTagsForResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) that identifies the resource to list the tags for.  
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tags": [ 
      { 
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="appmesh-ListTagsForResource-response-nextToken"></a>
The `nextToken` value to include in a future `ListTagsForResource` request. When the results of a `ListTagsForResource` request exceed `limit`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="appmesh-ListTagsForResource-response-tags"></a>
The tags for the resource.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListTagsForResource) 