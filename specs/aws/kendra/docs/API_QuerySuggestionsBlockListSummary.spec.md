---
id: "@specs/aws/kendra/docs/API_QuerySuggestionsBlockListSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuerySuggestionsBlockListSummary"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# QuerySuggestionsBlockListSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_QuerySuggestionsBlockListSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuerySuggestionsBlockListSummary
<a name="API_QuerySuggestionsBlockListSummary"></a>

Summary information on a query suggestions block list.

This includes information on the block list ID, block list name, when the block list was created, when the block list was last updated, and the count of block words/phrases in the block list.

For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).

## Contents
<a name="API_QuerySuggestionsBlockListSummary_Contents"></a>

 ** CreatedAt **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-CreatedAt"></a>
The Unix timestamp when the block list was created.  
Type: Timestamp  
Required: No

 ** Id **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-Id"></a>
The identifier of a block list.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: No

 ** ItemCount **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-ItemCount"></a>
The number of items in the block list file.  
Type: Integer  
Required: No

 ** Name **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-Name"></a>
The name of the block list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** Status **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-Status"></a>
The status of the block list.  
Type: String  
Valid Values: `ACTIVE | CREATING | DELETING | UPDATING | ACTIVE_BUT_UPDATE_FAILED | FAILED`   
Required: No

 ** UpdatedAt **   <a name="kendra-Type-QuerySuggestionsBlockListSummary-UpdatedAt"></a>
The Unix timestamp when the block list was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_QuerySuggestionsBlockListSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/QuerySuggestionsBlockListSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/QuerySuggestionsBlockListSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/QuerySuggestionsBlockListSummary) 