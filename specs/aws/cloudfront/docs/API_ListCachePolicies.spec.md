---
id: "@specs/aws/cloudfront/docs/API_ListCachePolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCachePolicies"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListCachePolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListCachePolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCachePolicies
<a name="API_ListCachePolicies"></a>

Gets a list of cache policies.

You can optionally apply a filter to return only the managed policies created by AWS, or only the custom policies created in your AWS account.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListCachePolicies_RequestSyntax"></a>

```
GET /2020-05-31/cache-policy?Marker={{Marker}}&MaxItems={{MaxItems}}&Type={{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCachePolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListCachePolicies_RequestSyntax) **   <a name="cloudfront-ListCachePolicies-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListCachePolicies_RequestSyntax) **   <a name="cloudfront-ListCachePolicies-request-uri-MaxItems"></a>
The maximum number of cache policies that you want in the response.

 ** [Type](#API_ListCachePolicies_RequestSyntax) **   <a name="cloudfront-ListCachePolicies-request-uri-Type"></a>
A filter to return only the specified kinds of cache policies. Valid values are:  
+  `managed` – Returns only the managed policies created by AWS.
+  `custom` – Returns only the custom policies created in your AWS account.
Valid Values: `managed | custom` 

## Request Body
<a name="API_ListCachePolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCachePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CachePolicyList>
   <Items>
      <CachePolicySummary>
         <CachePolicy>
            <CachePolicyConfig>
               <Comment>string</Comment>
               <DefaultTTL>long</DefaultTTL>
               <MaxTTL>long</MaxTTL>
               <MinTTL>long</MinTTL>
               <Name>string</Name>
               <ParametersInCacheKeyAndForwardedToOrigin>
                  <CookiesConfig>
                     <CookieBehavior>string</CookieBehavior>
                     <Cookies>
                        <Items>
                           <Name>string</Name>
                        </Items>
                        <Quantity>integer</Quantity>
                     </Cookies>
                  </CookiesConfig>
                  <EnableAcceptEncodingBrotli>boolean</EnableAcceptEncodingBrotli>
                  <EnableAcceptEncodingGzip>boolean</EnableAcceptEncodingGzip>
                  <HeadersConfig>
                     <HeaderBehavior>string</HeaderBehavior>
                     <Headers>
                        <Items>
                           <Name>string</Name>
                        </Items>
                        <Quantity>integer</Quantity>
                     </Headers>
                  </HeadersConfig>
                  <QueryStringsConfig>
                     <QueryStringBehavior>string</QueryStringBehavior>
                     <QueryStrings>
                        <Items>
                           <Name>string</Name>
                        </Items>
                        <Quantity>integer</Quantity>
                     </QueryStrings>
                  </QueryStringsConfig>
               </ParametersInCacheKeyAndForwardedToOrigin>
            </CachePolicyConfig>
            <Id>string</Id>
            <LastModifiedTime>timestamp</LastModifiedTime>
         </CachePolicy>
         <Type>string</Type>
      </CachePolicySummary>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</CachePolicyList>
```

## Response Elements
<a name="API_ListCachePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CachePolicyList](#API_ListCachePolicies_ResponseSyntax) **   <a name="cloudfront-ListCachePolicies-response-CachePolicyList"></a>
Root level tag for the CachePolicyList parameters.  
Required: Yes

 ** [Items](#API_ListCachePolicies_ResponseSyntax) **   <a name="cloudfront-ListCachePolicies-response-Items"></a>
Contains the cache policies in the list.  
Type: Array of [CachePolicySummary](API_CachePolicySummary.md) objects

 ** [MaxItems](#API_ListCachePolicies_ResponseSyntax) **   <a name="cloudfront-ListCachePolicies-response-MaxItems"></a>
The maximum number of cache policies requested.  
Type: Integer

 ** [NextMarker](#API_ListCachePolicies_ResponseSyntax) **   <a name="cloudfront-ListCachePolicies-response-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing cache policies where you left off.  
Type: String

 ** [Quantity](#API_ListCachePolicies_ResponseSyntax) **   <a name="cloudfront-ListCachePolicies-response-Quantity"></a>
The total number of cache policies returned in the response.  
Type: Integer

## Errors
<a name="API_ListCachePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchCachePolicy **   
The cache policy does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_ListCachePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListCachePolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListCachePolicies) 