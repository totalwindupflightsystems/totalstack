---
id: "@specs/aws/shield/docs/API_EmergencyContact"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EmergencyContact"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# EmergencyContact

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_EmergencyContact
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EmergencyContact
<a name="API_EmergencyContact"></a>

Contact information that the SRT can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.

## Contents
<a name="API_EmergencyContact_Contents"></a>

 ** EmailAddress **   <a name="AWSShield-Type-EmergencyContact-EmailAddress"></a>
The email address for the contact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 150.  
Pattern: `^\S+@\S+\.\S+$`   
Required: Yes

 ** ContactNotes **   <a name="AWSShield-Type-EmergencyContact-ContactNotes"></a>
Additional notes regarding the contact.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[\w\s\.\-,:/()+@]*$`   
Required: No

 ** PhoneNumber **   <a name="AWSShield-Type-EmergencyContact-PhoneNumber"></a>
The phone number for the contact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16.  
Pattern: `^\+[1-9]\d{1,14}$`   
Required: No

## See Also
<a name="API_EmergencyContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/EmergencyContact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/EmergencyContact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/EmergencyContact) 