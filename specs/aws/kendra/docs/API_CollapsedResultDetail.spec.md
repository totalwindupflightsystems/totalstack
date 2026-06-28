---
id: "@specs/aws/kendra/docs/API_CollapsedResultDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CollapsedResultDetail"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# CollapsedResultDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_CollapsedResultDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CollapsedResultDetail
<a name="API_CollapsedResultDetail"></a>

Provides details about a collapsed group of search results.

## Contents
<a name="API_CollapsedResultDetail_Contents"></a>

 ** DocumentAttribute **   <a name="kendra-Type-CollapsedResultDetail-DocumentAttribute"></a>
The value of the document attribute that results are collapsed on.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: Yes

 ** ExpandedResults **   <a name="kendra-Type-CollapsedResultDetail-ExpandedResults"></a>
A list of results in the collapsed group.  
Type: Array of [ExpandedResultItem](API_ExpandedResultItem.md) objects  
Required: No

## See Also
<a name="API_CollapsedResultDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/CollapsedResultDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/CollapsedResultDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/CollapsedResultDetail) 