---
id: "@specs/aws/cloudfront/docs/API_ListInvalidationsForDistributionTenant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInvalidationsForDistributionTenant"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListInvalidationsForDistributionTenant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListInvalidationsForDistributionTenant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInvalidationsForDistributionTenant
<a name="API_ListInvalidationsForDistributionTenant"></a>

Lists the invalidations for a distribution tenant.

## Request Syntax
<a name="API_ListInvalidationsForDistributionTenant_RequestSyntax"></a>

```
GET /2020-05-31/distribution-tenant/{{Id}}/invalidation?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInvalidationsForDistributionTenant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListInvalidationsForDistributionTenant_RequestSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-request-uri-Id"></a>
The ID of the distribution tenant.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [Marker](#API_ListInvalidationsForDistributionTenant_RequestSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-request-uri-Marker"></a>
Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set `Marker` to the value of the `NextMarker` from the current page's response. This value is the same as the ID of the last invalidation batch on that page.

 ** [MaxItems](#API_ListInvalidationsForDistributionTenant_RequestSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-request-uri-MaxItems"></a>
The maximum number of invalidations to return for the distribution tenant.

## Request Body
<a name="API_ListInvalidationsForDistributionTenant_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInvalidationsForDistributionTenant_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<InvalidationList>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <InvalidationSummary>
         <CreateTime>timestamp</CreateTime>
         <Id>string</Id>
         <Status>string</Status>
      </InvalidationSummary>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</InvalidationList>
```

## Response Elements
<a name="API_ListInvalidationsForDistributionTenant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [InvalidationList](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-InvalidationList"></a>
Root level tag for the InvalidationList parameters.  
Required: Yes

 ** [IsTruncated](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-IsTruncated"></a>
A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more invalidation batches in the list.  
Type: Boolean

 ** [Items](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-Items"></a>
A complex type that contains one `InvalidationSummary` element for each invalidation batch created by the current AWS account.  
Type: Array of [InvalidationSummary](API_InvalidationSummary.md) objects

 ** [Marker](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-Marker"></a>
The value that you provided for the `Marker` request parameter.  
Type: String

 ** [MaxItems](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-MaxItems"></a>
The value that you provided for the `MaxItems` request parameter.  
Type: Integer

 ** [NextMarker](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your invalidation batches where they left off.  
Type: String

 ** [Quantity](#API_ListInvalidationsForDistributionTenant_ResponseSyntax) **   <a name="cloudfront-ListInvalidationsForDistributionTenant-response-Quantity"></a>
The number of invalidation batches that were created by the current AWS account.   
Type: Integer

## Errors
<a name="API_ListInvalidationsForDistributionTenant_Errors"></a>

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
<a name="API_ListInvalidationsForDistributionTenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListInvalidationsForDistributionTenant) 