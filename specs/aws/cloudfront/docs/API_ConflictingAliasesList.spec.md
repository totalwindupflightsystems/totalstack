---
id: "@specs/aws/cloudfront/docs/API_ConflictingAliasesList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConflictingAliasesList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ConflictingAliasesList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ConflictingAliasesList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConflictingAliasesList
<a name="API_ConflictingAliasesList"></a>

A list of aliases (also called CNAMEs) and the CloudFront standard distributions and AWS accounts that they are associated with. In the list, the standard distribution and account IDs are partially hidden, which allows you to identify the standard distributions and accounts that you own, but helps to protect the information of ones that you don't own.

## Contents
<a name="API_ConflictingAliasesList_Contents"></a>

 ** Items **   <a name="cloudfront-Type-ConflictingAliasesList-Items"></a>
Contains the conflicting aliases in the list.  
Type: Array of [ConflictingAlias](API_ConflictingAlias.md) objects  
Required: No

 ** MaxItems **   <a name="cloudfront-Type-ConflictingAliasesList-MaxItems"></a>
The maximum number of conflicting aliases requested.  
Type: Integer  
Required: No

 ** NextMarker **   <a name="cloudfront-Type-ConflictingAliasesList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing conflicting aliases where you left off.  
Type: String  
Required: No

 ** Quantity **   <a name="cloudfront-Type-ConflictingAliasesList-Quantity"></a>
The number of conflicting aliases returned in the response.  
Type: Integer  
Required: No

## See Also
<a name="API_ConflictingAliasesList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConflictingAliasesList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConflictingAliasesList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConflictingAliasesList) 