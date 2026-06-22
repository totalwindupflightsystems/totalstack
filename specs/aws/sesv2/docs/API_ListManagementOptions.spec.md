---
id: "@specs/aws/sesv2/docs/API_ListManagementOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListManagementOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListManagementOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListManagementOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListManagementOptions
<a name="API_ListManagementOptions"></a>

An object used to specify a list or topic to which an email belongs, which will be used when a contact chooses to unsubscribe.

## Contents
<a name="API_ListManagementOptions_Contents"></a>

 ** ContactListName **   <a name="SES-Type-ListManagementOptions-ContactListName"></a>
The name of the contact list.  
Type: String  
Required: Yes

 ** TopicName **   <a name="SES-Type-ListManagementOptions-TopicName"></a>
The name of the topic.  
Type: String  
Required: No

## See Also
<a name="API_ListManagementOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListManagementOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListManagementOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListManagementOptions) 