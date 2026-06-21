---
id: "@specs/aws/lightsail/docs/amazon-lightsail-domain-register-other-dns-service-procedure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Transfer DNS management"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Transfer DNS management

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-domain-register-other-dns-service-procedure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Transfer DNS management for your Lightsail domain
<a name="amazon-lightsail-domain-register-other-dns-service-procedure"></a>

You can use an Amazon Lightsail DNS zone to manage the DNS records for a domain that you registered using Lightsail. Or, if you'd like, you can transfer management of DNS records for the domain to another DNS hosting provider. In this guide, we show you how to transfer management of DNS records for a domain you registered with Lightsail to another DNS hosting provider.

**Important**  
Any changes you make to the DNS of your domain might require several hours to propagate through the internet’s DNS. Because of this, you should keep the DNS records of your domain in place at your current DNS hosting provider until the transfer of management is done. This ensures that traffic for your domain continues to route to your resources uninterrupted while the transfer takes place.

**Contents**
+ [Complete the prerequisites](#other-dns-service-prerequisites)
+ [Add records to the DNS zone](#other-dns-service-add-records-dns-zone)

## Complete the prerequisites
<a name="other-dns-service-prerequisites"></a>

Complete the following prerequisites if you haven’t already done so:

1. Register a domain name. You can register a domain name using Lightsail. For more information, see [Register a new domain](amazon-lightsail-register-new-domain.md).

1. Use the process that’s provided by your DNS service to get the name servers for your domain.

## Add records to the DNS zone
<a name="other-dns-service-add-records-dns-zone"></a>

Complete the following procedure to add the name servers for another DNS hosting provider into your registered domain in Lightsail.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Domains & DNS** tab.

1. Choose the name of the domain that you want to configure to use another DNS service.

1. Choose **Edit Name Servers**.

1. Change the names of the name servers to the name servers that you got from your DNS service when you completed the prerequisites.

1. Choose **Save**.