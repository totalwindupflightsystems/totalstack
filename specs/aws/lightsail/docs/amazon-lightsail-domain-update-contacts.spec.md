---
id: "@specs/aws/lightsail/docs/amazon-lightsail-domain-update-contacts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update domain contact information"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Update domain contact information

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-domain-update-contacts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update domain contact information in Lightsail
<a name="amazon-lightsail-domain-update-contacts"></a>

When you register a domain with Amazon Lightsail, you must specify contact information for your domain. Your domain’s contact information is used to verify ownership of your domain and to keep you updated about any information related to your domain name. For more information about the information required during domain registration, see [Provide domain information when you register or transfer a domain in Lightsail](amazon-lightsail-domain-register-values-specify.md).

**Topics**
+ [Who is the owner of a domain?](#who-is-domain-owner)
+ [Update contact information for a domain](#update-contacts-update-domain-contact-info)

## Who is the owner of a domain?
<a name="who-is-domain-owner"></a>

When the contact type is **Person** and you change the **First Name** or **Last Name** fields for the registrant contact, you change the owner of the domain.

When the contact type is any value except **Person** and you change **Organization**, you change the owner of the domain.

The following actions happen when you change the contact information for a domain that is currently registered with Lightsail:
+ If you change contact information for the domain, we send an email notification to the registrant contact about the change. This email comes from **noreply@registrar.amazon**. For most changes, the registrant contact is not required to respond.
+ For changes to contact information that also constitute a change in ownership, we send the registrant contact an additional email. ICANN, the organization that maintains a central database of domain names, requires that the registrant contact confirm receiving the email.

## Update contact information for a domain
<a name="update-contacts-update-domain-contact-info"></a>

To update contact information for a domain, perform the following procedure.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Domains & DNS** tab.

1. Choose the name of the domain that you want to update.

1. Choose the **Contact info** tab. Then, choose **Edit contact**.

1. Update the applicable values. For more information, see [Values that you specify when you register or transfer a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-values-specify.html) in the Amazon Route 53 Developer Guide.

1. Choose **Save**.