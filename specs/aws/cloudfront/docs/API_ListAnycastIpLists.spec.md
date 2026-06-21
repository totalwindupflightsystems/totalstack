---
id: "@specs/aws/cloudfront/docs/API_ListAnycastIpLists"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAnycastIpLists"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListAnycastIpLists

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListAnycastIpLists
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAnycastIpLists
<a name="API_ListAnycastIpLists"></a>

Lists your Anycast static IP lists.

## Request Syntax
<a name="API_ListAnycastIpLists_RequestSyntax"></a>

```
GET /2020-05-31/anycast-ip-list?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnycastIpLists_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListAnycastIpLists_RequestSyntax) **   <a name="cloudfront-ListAnycastIpLists-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListAnycastIpLists_RequestSyntax) **   <a name="cloudfront-ListAnycastIpLists-request-uri-MaxItems"></a>
The maximum number of Anycast static IP lists that you want returned in the response.

## Request Body
<a name="API_ListAnycastIpLists_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnycastIpLists_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<AnycastIpListCollection>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <AnycastIpListSummary>
         <Arn>string</Arn>
         <ETag>string</ETag>
         <Id>string</Id>
         <IpAddressType>string</IpAddressType>
         <IpamConfig>
            <IpamCidrConfigs>
               <IpamCidrConfig>
                  <AnycastIp>string</AnycastIp>
                  <Cidr>string</Cidr>
                  <IpamPoolArn>string</IpamPoolArn>
                  <Status>string</Status>
               </IpamCidrConfig>
            </IpamCidrConfigs>
            <Quantity>integer</Quantity>
         </IpamConfig>
         <IpCount>integer</IpCount>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
         <Status>string</Status>
      </AnycastIpListSummary>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</AnycastIpListCollection>
```

## Response Elements
<a name="API_ListAnycastIpLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [AnycastIpListCollection](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-AnycastIpLists"></a>
Root level tag for the AnycastIpListCollection parameters.  
Required: Yes

 ** [IsTruncated](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-IsTruncated"></a>
If there are more items in the list collection than are in this response, this value is `true`.  
Type: Boolean

 ** [Items](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-Items"></a>
Items in the Anycast static IP list collection. Each item is of the [AnycastIpListSummary](API_AnycastIpListSummary.md) structure type.  
Type: Array of [AnycastIpListSummary](API_AnycastIpListSummary.md) objects

 ** [Marker](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-Marker"></a>
Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.  
Type: String

 ** [MaxItems](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-MaxItems"></a>
The maximum number of Anycast static IP list collections that you want returned in the response.  
Type: Integer

 ** [NextMarker](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-NextMarker"></a>
Indicates the next page of the Anycast static IP list collection. To get the next page of the list, use this value in the `Marker` field of your request.  
Type: String

 ** [Quantity](#API_ListAnycastIpLists_ResponseSyntax) **   <a name="cloudfront-ListAnycastIpLists-response-Quantity"></a>
The quantity of Anycast static IP lists in the collection.  
Type: Integer

## Errors
<a name="API_ListAnycastIpLists_Errors"></a>

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

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_ListAnycastIpLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListAnycastIpLists) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListAnycastIpLists) 