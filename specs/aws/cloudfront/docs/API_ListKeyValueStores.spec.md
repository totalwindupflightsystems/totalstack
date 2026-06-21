---
id: "@specs/aws/cloudfront/docs/API_ListKeyValueStores"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListKeyValueStores"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListKeyValueStores

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListKeyValueStores
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListKeyValueStores
<a name="API_ListKeyValueStores"></a>

Specifies the key value stores to list.

## Request Syntax
<a name="API_ListKeyValueStores_RequestSyntax"></a>

```
GET /2020-05-31/key-value-store?Marker={{Marker}}&MaxItems={{MaxItems}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListKeyValueStores_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListKeyValueStores_RequestSyntax) **   <a name="cloudfront-ListKeyValueStores-request-uri-Marker"></a>
The marker associated with the key value stores list.

 ** [MaxItems](#API_ListKeyValueStores_RequestSyntax) **   <a name="cloudfront-ListKeyValueStores-request-uri-MaxItems"></a>
The maximum number of items in the key value stores list.

 ** [Status](#API_ListKeyValueStores_RequestSyntax) **   <a name="cloudfront-ListKeyValueStores-request-uri-Status"></a>
The status of the request for the key value stores list.

## Request Body
<a name="API_ListKeyValueStores_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListKeyValueStores_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<KeyValueStoreList>
   <Items>
      <KeyValueStore>
         <ARN>string</ARN>
         <Comment>string</Comment>
         <Id>string</Id>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
         <Status>string</Status>
      </KeyValueStore>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</KeyValueStoreList>
```

## Response Elements
<a name="API_ListKeyValueStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [KeyValueStoreList](#API_ListKeyValueStores_ResponseSyntax) **   <a name="cloudfront-ListKeyValueStores-response-KeyValueStoreList"></a>
Root level tag for the KeyValueStoreList parameters.  
Required: Yes

 ** [Items](#API_ListKeyValueStores_ResponseSyntax) **   <a name="cloudfront-ListKeyValueStores-response-Items"></a>
The items of the key value store list.  
Type: Array of [KeyValueStore](API_KeyValueStore.md) objects

 ** [MaxItems](#API_ListKeyValueStores_ResponseSyntax) **   <a name="cloudfront-ListKeyValueStores-response-MaxItems"></a>
The maximum number of items in the key value store list.  
Type: Integer

 ** [NextMarker](#API_ListKeyValueStores_ResponseSyntax) **   <a name="cloudfront-ListKeyValueStores-response-NextMarker"></a>
The next marker associated with the key value store list.  
Type: String

 ** [Quantity](#API_ListKeyValueStores_ResponseSyntax) **   <a name="cloudfront-ListKeyValueStores-response-Quantity"></a>
The quantity of the key value store list.  
Type: Integer

## Errors
<a name="API_ListKeyValueStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_ListKeyValueStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListKeyValueStores) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListKeyValueStores) 