---
id: "@specs/aws/sesv2/docs/API_EmailAddressInsightsMailboxEvaluations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EmailAddressInsightsMailboxEvaluations"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EmailAddressInsightsMailboxEvaluations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EmailAddressInsightsMailboxEvaluations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EmailAddressInsightsMailboxEvaluations
<a name="API_EmailAddressInsightsMailboxEvaluations"></a>

Contains individual validation checks performed on an email address.

## Contents
<a name="API_EmailAddressInsightsMailboxEvaluations_Contents"></a>

 ** HasValidDnsRecords **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-HasValidDnsRecords"></a>
Checks that the domain exists, has valid DNS records, and is conﬁgured to receive email.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

 ** HasValidSyntax **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-HasValidSyntax"></a>
Checks that the email address follows proper RFC standards and contains valid characters in the correct format.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

 ** IsDisposable **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-IsDisposable"></a>
Checks disposable or temporary email addresses that could negatively impact your sender reputation.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

 ** IsRandomInput **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-IsRandomInput"></a>
Checks if the input appears to be random text.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

 ** IsRoleAddress **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-IsRoleAddress"></a>
Identiﬁes role-based addresses (such as admin@, support@, or info@) that may have lower engagement rates.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

 ** MailboxExists **   <a name="SES-Type-EmailAddressInsightsMailboxEvaluations-MailboxExists"></a>
Checks that the mailbox exists and can receive messages without actually sending an email.  
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object  
Required: No

## See Also
<a name="API_EmailAddressInsightsMailboxEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EmailAddressInsightsMailboxEvaluations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EmailAddressInsightsMailboxEvaluations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EmailAddressInsightsMailboxEvaluations) 