---
id: "@specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentityList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudFrontOriginAccessIdentityList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CloudFrontOriginAccessIdentityList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CloudFrontOriginAccessIdentityList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudFrontOriginAccessIdentityList
<a name="API_CloudFrontOriginAccessIdentityList"></a>

Lists the origin access identities for CloudFront.Send a `GET` request to the `/CloudFront API version/origin-access-identity/cloudfront` resource. The response includes a `CloudFrontOriginAccessIdentityList` element with zero or more `CloudFrontOriginAccessIdentitySummary` child elements. By default, your entire list of origin access identities is returned in one single page. If the list is long, you can paginate it using the `MaxItems` and `Marker` parameters.

## Contents
<a name="API_CloudFrontOriginAccessIdentityList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-IsTruncated"></a>
A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more items in the list.  
Type: Boolean  
Required: Yes

 ** Marker **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-Marker"></a>
Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the `Marker` to the value of the `NextMarker` from the current page's response (which is also the ID of the last identity on that page).  
Type: String  
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-MaxItems"></a>
The maximum number of origin access identities you want in the response body.  
Type: Integer  
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-Quantity"></a>
The number of CloudFront origin access identities that were created by the current AWS account.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-Items"></a>
A complex type that contains one `CloudFrontOriginAccessIdentitySummary` element for each origin access identity that was created by the current AWS account.  
Type: Array of [CloudFrontOriginAccessIdentitySummary](API_CloudFrontOriginAccessIdentitySummary.md) objects  
Required: No

 ** NextMarker **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentityList-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value you can use for the `Marker` request parameter to continue listing your origin access identities where they left off.  
Type: String  
Required: No

## See Also
<a name="API_CloudFrontOriginAccessIdentityList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CloudFrontOriginAccessIdentityList) 