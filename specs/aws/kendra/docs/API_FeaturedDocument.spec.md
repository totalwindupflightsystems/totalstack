---
id: "@specs/aws/kendra/docs/API_FeaturedDocument"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FeaturedDocument"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# FeaturedDocument

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_FeaturedDocument
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FeaturedDocument
<a name="API_FeaturedDocument"></a>

A featured document. This document is displayed at the top of the search results page, placed above all other results for certain queries. If there's an exact match of a query, then the document is featured in the search results.

## Contents
<a name="API_FeaturedDocument_Contents"></a>

 ** Id **   <a name="kendra-Type-FeaturedDocument-Id"></a>
The identifier of the document to feature in the search results. You can use the [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) API to search for specific documents with their document IDs included in the result items, or you can use the console.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_FeaturedDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/FeaturedDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/FeaturedDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/FeaturedDocument) 