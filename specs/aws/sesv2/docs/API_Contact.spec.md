---
id: "@specs/aws/sesv2/docs/API_Contact"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Contact"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Contact

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Contact
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Contact
<a name="API_Contact"></a>

A contact is the end-user who is receiving the email.

## Contents
<a name="API_Contact_Contents"></a>

 ** EmailAddress **   <a name="SES-Type-Contact-EmailAddress"></a>
The contact's email address.  
Type: String  
Required: No

 ** LastUpdatedTimestamp **   <a name="SES-Type-Contact-LastUpdatedTimestamp"></a>
A timestamp noting the last time the contact's information was updated.  
Type: Timestamp  
Required: No

 ** TopicDefaultPreferences **   <a name="SES-Type-Contact-TopicDefaultPreferences"></a>
The default topic preferences applied to the contact.  
Type: Array of [TopicPreference](API_TopicPreference.md) objects  
Required: No

 ** TopicPreferences **   <a name="SES-Type-Contact-TopicPreferences"></a>
The contact's preference for being opted-in to or opted-out of a topic.  
Type: Array of [TopicPreference](API_TopicPreference.md) objects  
Required: No

 ** UnsubscribeAll **   <a name="SES-Type-Contact-UnsubscribeAll"></a>
A boolean value status noting if the contact is unsubscribed from all contact list topics.  
Type: Boolean  
Required: No

## See Also
<a name="API_Contact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Contact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Contact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Contact) 