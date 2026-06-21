---
id: "@specs/aws/cloudfront/docs/API_ListOriginAccessControls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListOriginAccessControls"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListOriginAccessControls

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListOriginAccessControls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListOriginAccessControls
<a name="API_ListOriginAccessControls"></a>

Gets the list of CloudFront origin access controls (OACs) in this AWS account.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the `NextMarker` value from the current response as the `Marker` value in the next request.

**Note**  
If you're not using origin access controls for your AWS account, the `ListOriginAccessControls` operation doesn't return the `Items` element in the response.

## Request Syntax
<a name="API_ListOriginAccessControls_RequestSyntax"></a>

```
GET /2020-05-31/origin-access-control?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOriginAccessControls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListOriginAccessControls_RequestSyntax) **   <a name="cloudfront-ListOriginAccessControls-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListOriginAccessControls_RequestSyntax) **   <a name="cloudfront-ListOriginAccessControls-request-uri-MaxItems"></a>
The maximum number of origin access controls that you want in the response.

## Request Body
<a name="API_ListOriginAccessControls_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOriginAccessControls_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControlList>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <OriginAccessControlSummary>
         <Description>string</Description>
         <Id>string</Id>
         <Name>string</Name>
         <OriginAccessControlOriginType>string</OriginAccessControlOriginType>
         <SigningBehavior>string</SigningBehavior>
         <SigningProtocol>string</SigningProtocol>
      </OriginAccessControlSummary>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</OriginAccessControlList>
```

## Response Elements
<a name="API_ListOriginAccessControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [OriginAccessControlList](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-OriginAccessControlList"></a>
Root level tag for the OriginAccessControlList parameters.  
Required: Yes

 ** [IsTruncated](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-IsTruncated"></a>
If there are more items in the list than are in this response, this value is `true`.  
Type: Boolean

 ** [Items](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-Items"></a>
Contains the origin access controls in the list.  
Type: Array of [OriginAccessControlSummary](API_OriginAccessControlSummary.md) objects

 ** [Marker](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-Marker"></a>
The value of the `Marker` field that was provided in the request.  
Type: String

 ** [MaxItems](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-MaxItems"></a>
The maximum number of origin access controls requested.  
Type: Integer

 ** [NextMarker](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value to use in the `Marker` field of another request to continue listing origin access controls.  
Type: String

 ** [Quantity](#API_ListOriginAccessControls_ResponseSyntax) **   <a name="cloudfront-ListOriginAccessControls-response-Quantity"></a>
The number of origin access controls returned in the response.  
Type: Integer

## Errors
<a name="API_ListOriginAccessControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListOriginAccessControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListOriginAccessControls) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListOriginAccessControls) 