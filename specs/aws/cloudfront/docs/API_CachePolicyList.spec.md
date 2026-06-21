---
id: "@specs/aws/cloudfront/docs/API_CachePolicyList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicyList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicyList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicyList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicyList
<a name="API_CachePolicyList"></a>

A list of cache policies.

## Contents
<a name="API_CachePolicyList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-CachePolicyList-MaxItems"></a>
The maximum number of cache policies requested.  
Type: Integer  
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-CachePolicyList-Quantity"></a>
The total number of cache policies returned in the response.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-CachePolicyList-Items"></a>
Contains the cache policies in the list.  
Type: Array of [CachePolicySummary](API_CachePolicySummary.md) objects  
Required: No

 ** NextMarker **   <a name="cloudfront-Type-CachePolicyList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing cache policies where you left off.  
Type: String  
Required: No

## See Also
<a name="API_CachePolicyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyList) 