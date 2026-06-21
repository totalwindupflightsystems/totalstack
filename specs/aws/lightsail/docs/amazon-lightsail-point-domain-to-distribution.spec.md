---
id: "@specs/aws/lightsail/docs/amazon-lightsail-point-domain-to-distribution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Point your domain to a distribution"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Point your domain to a distribution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-point-domain-to-distribution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Point custom domains to Lightsail distributions
<a name="amazon-lightsail-point-domain-to-distribution"></a>

You must point your registered domain names to your Amazon Lightsail distribution after you enabled custom domains for your distribution. You do this by adding an alias record to the DNS zone of each of the domains specified on the certificate that you're using with your distribution. All of the records that you add should point to the default domain (e.g., `123456abcdef.cloudfront.net`) of your distribution.

In this guide, we provide you with the procedure to point your domains to your distribution using a Lightsail DNS zone. The procedure to point your domains to your distribution using a different DNS hosting provider, like Domain.com or GoDaddy, may be similar. For more information about Lightsail DNS zones, see [DNS](understanding-dns-in-amazon-lightsail.md).

For more information about distributions, see [Create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

**Contents**
+ [Step 1: Complete the prerequisite](#point-domain-to-distribution-prerequisite)
+ [Step 2: Get the default domain of your distribution](#get-distribution-default-domain-name)
+ [Step 3: Add a record to your domain's DNS zone](#add-distribution-alias-record-to-dns-zone)

## Step 1: Complete the prerequisite
<a name="point-domain-to-distribution-prerequisite"></a>

Before you get started, you should enable custom domains for your Lightsail distribution. For more information, see [Enable custom domains for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md).

## Step 2: Get the default domain of your distribution
<a name="get-distribution-default-domain-name"></a>

Complete the following procedure to get default domain name of your distribution, which you specify when you add an alias record to the DNS of your domain.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which want get the default domain name.

1. In the header section of your distribution's management page, make note of your distribution's default domain name. Your distribution's default domain name is similar to `123456abcdef.cloudfront.net`.

   You must add this value as part of an alias record in the DNS of your domains. We recommend that you copy and paste this value into a text file that you can refer to later. Continue to the next [Step 3: Add a record to your domain's DNS zone](#add-distribution-alias-record-to-dns-zone) section of this tutorial.

## Step 3: Add a record to your domain's DNS zone
<a name="add-distribution-alias-record-to-dns-zone"></a>

Complete the following procedure to add a record to your domain's DNS zone.

1. In the left navigation pane, choose **Domains & DNS**.

1. Under the **DNS zones** section of the page, choose the domain name to which you want to add the record that will direct traffic for your domain to your distribution.

1. Choose the **DNS records** tab. Then, choose **Add record**.

1. Complete one of the following steps depending on the type of domain that you want to point to your distribution:
   + Choose an address (A) record to point an apex domain (e.g., `example.com`) to your distribution.

     If an A record for the apex of your domain is already present in your DNS zone, then you will need to edit that existing record instead of adding another A record.
   + Choose a canonical name (CNAME) to point a sub domain, such as `website.example.com`, to your distribution.

1. If you're adding an A record, then in the **Resolves to** text box choose the name of your distribution. If you're adding a CNAME record, then in the **Maps to** text box enter the default domain name of your distribution.
**Note**  
When you add an A record to your DNS zone, and choose the name of your distribution, you are in fact adding an alias record, which is different than an address record. Lightsail makes it easy for you to add alias records without the additional steps that are typically required at other DNS hosting providers.

1. Choose the save icon to save the record to your DNS zone.

   Repeat these steps to add additional DNS records for domains on your certificate that you are using with your distribution. Allow time for changes to propagate through the Internet’s DNS. After a few minutes, you should see if your domain is pointing to your distribution. You should also test your distribution. For more information, see the following [Test your distribution](amazon-lightsail-testing-distribution.md).