---
id: "@specs/aws/sesv2/docs/API_AccountDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccountDetails"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# AccountDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_AccountDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccountDetails
<a name="API_AccountDetails"></a>

An object that contains information about your account details.

## Contents
<a name="API_AccountDetails_Contents"></a>

 ** AdditionalContactEmailAddresses **   <a name="SES-Type-AccountDetails-AdditionalContactEmailAddresses"></a>
Additional email addresses where updates are sent about your account review process.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 4 items.  
Length Constraints: Minimum length of 6. Maximum length of 254.  
Pattern: `^(.+)@(.+)$`   
Required: No

 ** ContactLanguage **   <a name="SES-Type-AccountDetails-ContactLanguage"></a>
The language you would prefer for the case. The contact language can be one of `ENGLISH` or `JAPANESE`.  
Type: String  
Valid Values: `EN | JA`   
Required: No

 ** MailType **   <a name="SES-Type-AccountDetails-MailType"></a>
The type of email your account is sending. The mail type can be one of the following:  
+  `MARKETING` – Most of your sending traffic is to keep your customers informed of your latest offering.
+  `TRANSACTIONAL` – Most of your sending traffic is to communicate during a transaction with a customer.
Type: String  
Valid Values: `MARKETING | TRANSACTIONAL`   
Required: No

 ** ReviewDetails **   <a name="SES-Type-AccountDetails-ReviewDetails"></a>
Information about the review of the latest details you submitted.  
Type: [ReviewDetails](API_ReviewDetails.md) object  
Required: No

 ** UseCaseDescription **   <a name="SES-Type-AccountDetails-UseCaseDescription"></a>
 *This member has been deprecated.*   
A description of the types of email that you plan to send.  
Type: String  
Length Constraints: Maximum length of 5000.  
Required: No

 ** WebsiteURL **   <a name="SES-Type-AccountDetails-WebsiteURL"></a>
The URL of your website. This information helps us better understand the type of content that you plan to send.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?`   
Required: No

## See Also
<a name="API_AccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/AccountDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/AccountDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/AccountDetails) 