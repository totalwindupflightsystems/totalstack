---
id: "@specs/aws/lightsail/docs/amazon-lightsail-domain-privacy-protection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Privacy protection"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Privacy protection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-domain-privacy-protection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Manage privacy protection for domain contacts in Lightsail
<a name="amazon-lightsail-domain-privacy-protection"></a>

When you register a domain on Amazon Lightsail, we activate privacy protection by default for all the domain contacts. This typically hides most of your contact information from WHOIS ("Who is") queries and reduces the amount of spam that you receive. Your contact information is replaced with either the contact information for the registrar or with the phrase "REDACTED FOR PRIVACY." There are no charges for using privacy protection.

If you choose to deactivate privacy protection, anyone can send a WHOIS query for the domain and, for most top-level domains (TLDs), they might be able to get all the contact information that you provided when you registered the domain. This information includes name, address, phone number, and email address. The WHOIS command is widely available. It's included in many operating systems, and it's also available as a web application on many websites.

To manage privacy protection for a domain that you registered by using Lightsail, perform the following procedure.

**Contents**
+ [Complete the prerequisites](#privacy-protection-prerequisites)
+ [Manage privacy protection for your domain](#manage-domain-privacy-protection)

## Complete the prerequisites
<a name="privacy-protection-prerequisites"></a>

Register a domain with Lightsail. For more information, see [Register a new domain](amazon-lightsail-register-new-domain.md).

## Manage privacy protection for your domain
<a name="manage-domain-privacy-protection"></a>

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Domains & DNS** tab.

1. Choose the name of the domain that you want to change the privacy protection for.

1. Choose **Contact info**.

1. You can manage privacy protection for your contact information by turning the **Privacy protection** toggle switch on or off.