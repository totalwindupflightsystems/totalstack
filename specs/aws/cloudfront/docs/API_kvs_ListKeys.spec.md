---
id: "@specs/aws/cloudfront/docs/API_kvs_ListKeys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListKeys"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListKeys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_kvs_ListKeys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListKeys
<a name="API_kvs_ListKeys"></a>

Returns a list of key-value pairs.

## Request Syntax
<a name="API_kvs_ListKeys_RequestSyntax"></a>

```
GET /key-value-stores/{{KvsARN}}/keys?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_kvs_ListKeys_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KvsARN](#API_kvs_ListKeys_RequestSyntax) **   <a name="cloudfront-kvs_ListKeys-request-uri-KvsARN"></a>
The Amazon Resource Name (ARN) of the key value store.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [MaxResults](#API_kvs_ListKeys_RequestSyntax) **   <a name="cloudfront-kvs_ListKeys-request-uri-MaxResults"></a>
Maximum number of results that are returned per call. The default is 10 and maximum allowed page is 50.  
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_kvs_ListKeys_RequestSyntax) **   <a name="cloudfront-kvs_ListKeys-request-uri-NextToken"></a>
If `nextToken` is returned in the response, there are more results available. Make the next call using the returned token to retrieve the next page.

## Request Body
<a name="API_kvs_ListKeys_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_kvs_ListKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_kvs_ListKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_kvs_ListKeys_ResponseSyntax) **   <a name="cloudfront-kvs_ListKeys-response-Items"></a>
The key-value pairs.  
Type: Array of [ListKeysResponseListItem](API_kvs_ListKeysResponseListItem.md) objects

 ** [NextToken](#API_kvs_ListKeys_ResponseSyntax) **   <a name="cloudfront-kvs_ListKeys-response-NextToken"></a>
If `nextToken` is returned in the response, there are more results available. Make the next call using the returned token to retrieve the next page.  
Type: String

## Errors
<a name="API_kvs_ListKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
Access denied.  
HTTP Status Code: 403

 ** ConflictException **   
Resource is not in expected state.  
HTTP Status Code: 409

 ** InternalServerException **   
Internal server error.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
Resource was not found.  
HTTP Status Code: 404

 ** ValidationException **   
Validation failed.  
HTTP Status Code: 400

## See Also
<a name="API_kvs_ListKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/ListKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/ListKeys) 