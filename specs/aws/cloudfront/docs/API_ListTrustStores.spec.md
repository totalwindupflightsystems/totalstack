---
id: "@specs/aws/cloudfront/docs/API_ListTrustStores"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTrustStores"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListTrustStores

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListTrustStores
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTrustStores
<a name="API_ListTrustStores"></a>

Lists trust stores.

## Request Syntax
<a name="API_ListTrustStores_RequestSyntax"></a>

```
POST /2020-05-31/trust-stores HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListTrustStoresRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Marker>{{string}}</Marker>
   <MaxItems>{{integer}}</MaxItems>
</ListTrustStoresRequest>
```

## URI Request Parameters
<a name="API_ListTrustStores_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTrustStores_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ListTrustStoresRequest](#API_ListTrustStores_RequestSyntax) **   <a name="cloudfront-ListTrustStores-request-ListTrustStoresRequest"></a>
Root level tag for the ListTrustStoresRequest parameters.  
Required: Yes

 ** [Marker](#API_ListTrustStores_RequestSyntax) **   <a name="cloudfront-ListTrustStores-request-Marker"></a>
Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.  
Type: String  
Required: No

 ** [MaxItems](#API_ListTrustStores_RequestSyntax) **   <a name="cloudfront-ListTrustStores-request-MaxItems"></a>
The maximum number of trust stores that you want returned in the response.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListTrustStores_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListTrustStoresResult>
   <NextMarker>string</NextMarker>
   <TrustStoreList>
      <TrustStoreSummary>
         <Arn>string</Arn>
         <ETag>string</ETag>
         <Id>string</Id>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
         <NumberOfCaCertificates>integer</NumberOfCaCertificates>
         <Reason>string</Reason>
         <Status>string</Status>
      </TrustStoreSummary>
   </TrustStoreList>
</ListTrustStoresResult>
```

## Response Elements
<a name="API_ListTrustStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListTrustStoresResult](#API_ListTrustStores_ResponseSyntax) **   <a name="cloudfront-ListTrustStores-response-ListTrustStoresResult"></a>
Root level tag for the ListTrustStoresResult parameters.  
Required: Yes

 ** [NextMarker](#API_ListTrustStores_ResponseSyntax) **   <a name="cloudfront-ListTrustStores-response-NextMarker"></a>
Indicates the next page of trust stores. To get the next page of the list, use this value in the `Marker` field of your request.  
Type: String

 ** [TrustStoreList](#API_ListTrustStores_ResponseSyntax) **   <a name="cloudfront-ListTrustStores-response-TrustStoreList"></a>
The trust store list.  
Type: Array of [TrustStoreSummary](API_TrustStoreSummary.md) objects

## Errors
<a name="API_ListTrustStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListTrustStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListTrustStores) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListTrustStores) 