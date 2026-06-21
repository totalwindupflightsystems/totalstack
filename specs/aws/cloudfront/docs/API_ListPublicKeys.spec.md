---
id: "@specs/aws/cloudfront/docs/API_ListPublicKeys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPublicKeys"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListPublicKeys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListPublicKeys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPublicKeys
<a name="API_ListPublicKeys"></a>

List all public keys that have been added to CloudFront for this account.

## Request Syntax
<a name="API_ListPublicKeys_RequestSyntax"></a>

```
GET /2020-05-31/public-key?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPublicKeys_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListPublicKeys_RequestSyntax) **   <a name="cloudfront-ListPublicKeys-request-uri-Marker"></a>
Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the `Marker` to the value of the `NextMarker` from the current page's response (which is also the ID of the last public key on that page).

 ** [MaxItems](#API_ListPublicKeys_RequestSyntax) **   <a name="cloudfront-ListPublicKeys-request-uri-MaxItems"></a>
The maximum number of public keys you want in the response body.

## Request Body
<a name="API_ListPublicKeys_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPublicKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PublicKeyList>
   <Items>
      <PublicKeySummary>
         <Comment>string</Comment>
         <CreatedTime>timestamp</CreatedTime>
         <EncodedKey>string</EncodedKey>
         <Id>string</Id>
         <Name>string</Name>
      </PublicKeySummary>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</PublicKeyList>
```

## Response Elements
<a name="API_ListPublicKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [PublicKeyList](#API_ListPublicKeys_ResponseSyntax) **   <a name="cloudfront-ListPublicKeys-response-PublicKeyList"></a>
Root level tag for the PublicKeyList parameters.  
Required: Yes

 ** [Items](#API_ListPublicKeys_ResponseSyntax) **   <a name="cloudfront-ListPublicKeys-response-Items"></a>
A list of public keys.  
Type: Array of [PublicKeySummary](API_PublicKeySummary.md) objects

 ** [MaxItems](#API_ListPublicKeys_ResponseSyntax) **   <a name="cloudfront-ListPublicKeys-response-MaxItems"></a>
The maximum number of public keys you want in the response.  
Type: Integer

 ** [NextMarker](#API_ListPublicKeys_ResponseSyntax) **   <a name="cloudfront-ListPublicKeys-response-NextMarker"></a>
If there are more elements to be listed, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your public keys where you left off.  
Type: String

 ** [Quantity](#API_ListPublicKeys_ResponseSyntax) **   <a name="cloudfront-ListPublicKeys-response-Quantity"></a>
The number of public keys in the list.  
Type: Integer

## Errors
<a name="API_ListPublicKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListPublicKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListPublicKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListPublicKeys) 