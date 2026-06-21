---
id: "@specs/aws/lightsail/docs/amazon-lightsail-domain-register-values-specify"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Registration information"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Registration information

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-domain-register-values-specify
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Provide domain information when you register or transfer a domain in Lightsail
<a name="amazon-lightsail-domain-register-values-specify"></a>

When you use Amazon Lightsail to register a domain, you provide domain information such as the registration period (*term*) and domain contact information. You also configure automatic domain renewal and privacy protection.

You can also change information for a domain that is currently registered with Lightsail.

**Note**  
If you change contact information for the domain, we send an email notification to the registrant contact about the change. This email comes from **noreply@registrar.amazon**. For most changes, the registrant contact is not required to respond.
For changes to contact information that also constitute a change in ownership, we send the registrant contact an additional email. ICANN, the organization that maintains a central database of domain names, requires that the registrant contact confirm receiving the email. For more information, see [First name, last name](#first-name-last-name) and [Organization](#organization) later in this section.

For more information about changing contact information for an existing domain, see [Update contact information for a domain](amazon-lightsail-domain-update-contacts.md).

**Topics**
+ [Term](#term)
+ [Automatic domain renewal](#automatic-domain-renewal)
+ [Registrant, administrative, technical, and billing contacts](#registrant-admin-tech)
+ [Contact type](#contact-type)
+ [First name, last name](#first-name-last-name)
+ [Organization](#organization)
+ [Email](#email)
+ [Phone](#phone)
+ [Address 1](#address-1)
+ [Address 2](#address-2)
+ [Country](#country)
+ [State](#state)
+ [City](#city)
+ [Postal/zip code](#postal-code)
+ [Privacy protection](#privacy-protection)

## Term
<a name="term"></a>

The registration period for the domain. The term is typically one year, although you can increase the term up to ten years while registering the domain.

## Automatic domain renewal
<a name="automatic-domain-renewal"></a>

When you register a domain with Lightsail, we configure the domain to renew automatically. The automatic renewal period is typically one year. Choose whether to have Lightsail automatically renew the domain before it expires. The registration fee is charged to your AWS account. For more information, see [Domain registration renewal](amazon-lightsail-domain-manage-auto-renew.md).

**Important**  
If you deactivate automatic domain renewal, registration for the domain will not be renewed when the expiration date passes. As a result, you might lose control of the domain name. 

## Registrant, administrative, technical, and billing contacts
<a name="registrant-admin-tech"></a>

The following contacts are required when you register your domain:
+ **Registrant** – The owner of the domain.
+ **Administrator** – The point-of-contact responsible for administering the domain.
+ **Technical** – The point-of-contact responsible for making technical changes to the domain.
+ **Billing** – The point-of-contact responsible for billing inquiries about the domain.

**Note**  
By default, we use the same information that you specify for the registrant and apply it to the other contacts. To enter different information for a contact, clear the **Same as registrant** selection.

## Contact type
<a name="contact-type"></a>

The category for this contact.

**Note**  
If you choose the **Company** or **Association** option, you must enter an organization name.
For some top-level domains (TLDs), privacy protection availability depends on the value that you choose for **Contact type**. For the privacy protection settings for your TLD, see [Domains that you can register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html#registrar-tld-list-index-generic)

## First name, last name
<a name="first-name-last-name"></a>

The first and last names of the contact. For **First name** and **Last name**, we recommend that you use the name on your official ID. For some changes to domain settings, you must provide proof of identity. In those cases, the name on your ID must match the name of the registrant contact for the domain.

If you change the email address of the registrant contact, this email is sent to both the former and new email addresses.

## Organization
<a name="organization"></a>

The organization that is associated with the contact, if any. For the registrant and administrative contacts, this is typically the organization that is registering the domain. For the technical contact, this might be the organization that manages the domain.

When the contact type is any value except **Person** and you change the **Organization** field for the registrant contact, you change the domain owner. ICANN requires that we email the registrant contact to get approval. The email comes from one of the following email addresses:
+ **noreply@registrar.amazon** – For domains with Amazon Registrar as the registrar.
+ **noreply@domainnameverification.net** – For domains with our registrar associate, Gandi, as the registrar.

To determine who the registrar is for your TLD, see [Domains that you can register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html#registrar-tld-list-index-generic).

If you change the email address of the registrant contact, this email is sent to both the former and new email addresses.

## Email
<a name="email"></a>

The email address for the contact.

**Note**  
If you change the email address for the registrant contact, we send notification emails to both the former and new email addresses. This email comes from **noreply@registrar.amazon**.

## Phone
<a name="phone"></a>

The phone number for the contact:
+ If you're entering a phone number for locations in the United States or Canada, enter 1 followed by the 10-digit phone number with area code.
+ If you're entering a phone number for any other location, enter the country code followed by rest of the phone number. For a list of country calling codes, see [List of country calling codes](https://en.wikipedia.org/wiki/List_of_country_calling_codes) on *Wikipedia*.

## Address 1
<a name="address-1"></a>

The street address or P.O. box for the contact. 

## Address 2
<a name="address-2"></a>

Additional address information for the contact, such as apartment, suite, unit, building, floor, or mail stop.

## Country
<a name="country"></a>

The country for the contact.

## State
<a name="state"></a>

The state or province for the contact, if any.

## City
<a name="city"></a>

The city for the contact.

## Postal/zip code
<a name="postal-code"></a>

The postal or zip code for the contact.

## Privacy protection
<a name="privacy-protection"></a>

Choose whether to conceal your contact information from WHOIS queries. If you activate privacy protection for your domain’s contact information, WHOIS ("who is") queries will return contact information for the domain registrar instead of your personal information. The domain registrar is the company that manages domain name registrations.

**Note**  
The same privacy setting applies to the administrative, registrant, and technical contacts.

If you deactivate privacy protection for your domain’s contact information, you will get more email spam at the email address that you specified.

Anyone can send a WHOIS query for a domain and get back all of the contact information for that domain. The WHOIS command is available in many operating systems, and it's also available as a web application on many websites.

**Important**  
Although there are legitimate users for your domain contact information, the most common users are spammers, who target domain contacts with unwanted email and bogus offers. In general, we recommend leaving **Privacy protection** activated for **Contact information**.

For more information about privacy protection, see the following topics:
+ [Manage privacy protection for a domain](amazon-lightsail-domain-privacy-protection.md)
+ [Domains that you can register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html#registrar-tld-list-index-generic)