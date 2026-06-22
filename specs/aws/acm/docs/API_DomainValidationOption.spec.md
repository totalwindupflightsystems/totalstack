---
id: "@specs/aws/acm/docs/API_DomainValidationOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainValidationOption"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# DomainValidationOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_DomainValidationOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainValidationOption
<a name="API_DomainValidationOption"></a>

Contains information about the domain names that you want ACM to use to send you emails that enable you to validate domain ownership.

## Contents
<a name="API_DomainValidationOption_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DomainName **   <a name="ACM-Type-DomainValidationOption-DomainName"></a>
A fully qualified domain name (FQDN) in the certificate request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

 ** ValidationDomain **   <a name="ACM-Type-DomainValidationOption-ValidationDomain"></a>
The domain name that you want ACM to use to send you validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the `DomainName` value or a superdomain of the `DomainName` value. For example, if you request a certificate for `testing.example.com`, you can specify `example.com` for this value. In that case, ACM sends domain validation emails to the following five addresses:  
+ admin@example.com
+ administrator@example.com
+ hostmaster@example.com
+ postmaster@example.com
+ webmaster@example.com
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

## See Also
<a name="API_DomainValidationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DomainValidationOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DomainValidationOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DomainValidationOption) 