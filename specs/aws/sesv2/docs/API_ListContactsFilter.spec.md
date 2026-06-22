---
id: "@specs/aws/sesv2/docs/API_ListContactsFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListContactsFilter"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListContactsFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListContactsFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListContactsFilter
<a name="API_ListContactsFilter"></a>

A filter that can be applied to a list of contacts.

## Contents
<a name="API_ListContactsFilter_Contents"></a>

 ** FilteredStatus **   <a name="SES-Type-ListContactsFilter-FilteredStatus"></a>
The status by which you are filtering: `OPT_IN` or `OPT_OUT`.  
Type: String  
Valid Values: `OPT_IN | OPT_OUT`   
Required: No

 ** TopicFilter **   <a name="SES-Type-ListContactsFilter-TopicFilter"></a>
Used for filtering by a specific topic preference.  
Type: [TopicFilter](API_TopicFilter.md) object  
Required: No

## See Also
<a name="API_ListContactsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListContactsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListContactsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListContactsFilter) 