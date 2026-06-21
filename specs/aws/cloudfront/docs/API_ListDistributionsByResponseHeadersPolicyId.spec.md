---
id: "@specs/aws/cloudfront/docs/API_ListDistributionsByResponseHeadersPolicyId"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDistributionsByResponseHeadersPolicyId"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListDistributionsByResponseHeadersPolicyId

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListDistributionsByResponseHeadersPolicyId
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDistributionsByResponseHeadersPolicyId
<a name="API_ListDistributionsByResponseHeadersPolicyId"></a>

Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified response headers policy.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListDistributionsByResponseHeadersPolicyId_RequestSyntax"></a>

```
GET /2020-05-31/distributionsByResponseHeadersPolicyId/{{ResponseHeadersPolicyId}}?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDistributionsByResponseHeadersPolicyId_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListDistributionsByResponseHeadersPolicyId_RequestSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListDistributionsByResponseHeadersPolicyId_RequestSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-request-uri-MaxItems"></a>
The maximum number of distribution IDs that you want to get in the response.

 ** [ResponseHeadersPolicyId](#API_ListDistributionsByResponseHeadersPolicyId_RequestSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-request-uri-ResponseHeadersPolicyId"></a>
The ID of the response headers policy whose associated distribution IDs you want to list.  
Required: Yes

## Request Body
<a name="API_ListDistributionsByResponseHeadersPolicyId_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionIdList>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <DistributionId>string</DistributionId>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</DistributionIdList>
```

## Response Elements
<a name="API_ListDistributionsByResponseHeadersPolicyId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DistributionIdList](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-DistributionIdList"></a>
Root level tag for the DistributionIdList parameters.  
Required: Yes

 ** [IsTruncated](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-IsTruncated"></a>
A flag that indicates whether more distribution IDs remain to be listed. If your results were truncated, you can make a subsequent request using the `Marker` request field to retrieve more distribution IDs in the list.  
Type: Boolean

 ** [Items](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-Items"></a>
Contains the distribution IDs in the list.  
Type: Array of strings

 ** [Marker](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-Marker"></a>
The value provided in the `Marker` request field.  
Type: String

 ** [MaxItems](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-MaxItems"></a>
The maximum number of distribution IDs requested.  
Type: Integer

 ** [NextMarker](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-NextMarker"></a>
Contains the value that you should use in the `Marker` field of a subsequent request to continue listing distribution IDs where you left off.  
Type: String

 ** [Quantity](#API_ListDistributionsByResponseHeadersPolicyId_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByResponseHeadersPolicyId-response-Quantity"></a>
The total number of distribution IDs returned in the response.  
Type: Integer

## Errors
<a name="API_ListDistributionsByResponseHeadersPolicyId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchResponseHeadersPolicy **   
The response headers policy does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_ListDistributionsByResponseHeadersPolicyId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByResponseHeadersPolicyId) 