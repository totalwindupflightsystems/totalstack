---
id: "@specs/aws/cloudfront/docs/API_kvs_PutKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutKey"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# PutKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_kvs_PutKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutKey
<a name="API_kvs_PutKey"></a>

Creates a new key-value pair or replaces the value of an existing key.

## Request Syntax
<a name="API_kvs_PutKey_RequestSyntax"></a>

```
PUT /key-value-stores/{{KvsARN}}/keys/{{Key}} HTTP/1.1
If-Match: {{IfMatch}}
Content-type: application/json

{
   "Value": "{{string}}"
}
```

## URI Request Parameters
<a name="API_kvs_PutKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IfMatch](#API_kvs_PutKey_RequestSyntax) **   <a name="cloudfront-kvs_PutKey-request-IfMatch"></a>
The current version (`ETag`) of the key value store that you are putting keys into, which you can get by using the `DescribeKeyValueStore` API operation.  
Required: Yes

 ** [Key](#API_kvs_PutKey_RequestSyntax) **   <a name="cloudfront-kvs_PutKey-request-uri-Key"></a>
The key to put.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** [KvsARN](#API_kvs_PutKey_RequestSyntax) **   <a name="cloudfront-kvs_PutKey-request-uri-KvsARN"></a>
The Amazon Resource Name (ARN) of the key value store.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## Request Body
<a name="API_kvs_PutKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Value](#API_kvs_PutKey_RequestSyntax) **   <a name="cloudfront-kvs_PutKey-request-Value"></a>
The value to put.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_kvs_PutKey_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{ETag}}
Content-type: application/json

{
   "ItemCount": number,
   "TotalSizeInBytes": number
}
```

## Response Elements
<a name="API_kvs_PutKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_kvs_PutKey_ResponseSyntax) **   <a name="cloudfront-kvs_PutKey-response-ETag"></a>
The current version identifier of the key value store after the successful put.

The following data is returned in JSON format by the service.

 ** [ItemCount](#API_kvs_PutKey_ResponseSyntax) **   <a name="cloudfront-kvs_PutKey-response-ItemCount"></a>
Number of key-value pairs in the key value store after the successful put.  
Type: Integer

 ** [TotalSizeInBytes](#API_kvs_PutKey_ResponseSyntax) **   <a name="cloudfront-kvs_PutKey-response-TotalSizeInBytes"></a>
Total size of the key value store after the successful put, in bytes.  
Type: Long

## Errors
<a name="API_kvs_PutKey_Errors"></a>

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

 ** ServiceQuotaExceededException **   
Limit exceeded.  
HTTP Status Code: 402

 ** ValidationException **   
Validation failed.  
HTTP Status Code: 400

## See Also
<a name="API_kvs_PutKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/PutKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/PutKey) 