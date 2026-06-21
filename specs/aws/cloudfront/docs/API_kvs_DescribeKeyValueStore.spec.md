---
id: "@specs/aws/cloudfront/docs/API_kvs_DescribeKeyValueStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeKeyValueStore"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DescribeKeyValueStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_kvs_DescribeKeyValueStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeKeyValueStore
<a name="API_kvs_DescribeKeyValueStore"></a>

Returns metadata information about the key value store.

## Request Syntax
<a name="API_kvs_DescribeKeyValueStore_RequestSyntax"></a>

```
GET /key-value-stores/{{KvsARN}} HTTP/1.1
```

## URI Request Parameters
<a name="API_kvs_DescribeKeyValueStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KvsARN](#API_kvs_DescribeKeyValueStore_RequestSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-request-uri-KvsARN"></a>
The Amazon Resource Name (ARN) of the key value store.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## Request Body
<a name="API_kvs_DescribeKeyValueStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_kvs_DescribeKeyValueStore_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{ETag}}
Content-type: application/json

{
   "Created": number,
   "FailureReason": "string",
   "ItemCount": number,
   "KvsARN": "string",
   "LastModified": number,
   "Status": "string",
   "TotalSizeInBytes": number
}
```

## Response Elements
<a name="API_kvs_DescribeKeyValueStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-ETag"></a>
The version identifier for the current version of the key value store.

The following data is returned in JSON format by the service.

 ** [Created](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-Created"></a>
Date and time when the key value store was created.  
Type: Timestamp

 ** [FailureReason](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-FailureReason"></a>
The reason why the key value store wasn't created.  
Type: String

 ** [ItemCount](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-ItemCount"></a>
Number of key-value pairs in the key value store.  
Type: Integer

 ** [KvsARN](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-KvsARN"></a>
The Amazon Resource Name (ARN) of the key value store.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LastModified](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-LastModified"></a>
Date and time when the key-value pairs in the key value store was last modified.  
Type: Timestamp

 ** [Status](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-Status"></a>
The current status of the key value store.  
Type: String

 ** [TotalSizeInBytes](#API_kvs_DescribeKeyValueStore_ResponseSyntax) **   <a name="cloudfront-kvs_DescribeKeyValueStore-response-TotalSizeInBytes"></a>
Total size of the key value store in bytes.  
Type: Long

## Errors
<a name="API_kvs_DescribeKeyValueStore_Errors"></a>

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

## See Also
<a name="API_kvs_DescribeKeyValueStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore) 