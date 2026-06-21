---
id: "@specs/aws/lightsail/docs/amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use Route 53"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Use Route 53

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Point a domain to your Lightsail instance using Amazon Route 53
<a name="amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance"></a>

The DNS zone in Amazon Lightsail makes it easy to point a registered domain name, like `example.com`, to your website running on a Lightsail instance. You can create up to six Lightsail DNS zones, and not all DNS record types are supported. For more information about Lightsail DNS zones, see [DNS](understanding-dns-in-amazon-lightsail.md).

If the Lightsail DNS zone is too limited for you, then we recommend using an Amazon Route 53 hosted zone to manage your domain’s DNS records. You can manage the DNS for up to 500 domains using Route 53, and it supports a greater variety of DNS record types. Or, you might already be using Route 53 to manage your domain’s DNS records and prefer to continue using it. This guide shows you how to edit the DNS records for a domain managed in Route 53 to point to your Lightsail instance.

## Prerequisites
<a name="using-amazon-route-53-prerequisites"></a>

Complete the following prerequisites if you haven’t already done so:
+ Register a domain name using Route 53. For more information, see [Registering a New Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html) in the Route 53 documentation.
+ If you already registered a domain but you’re not using Route 53 to manage its records, then you must transfer management of the DNS records for your domain to Route 53. For more information, see [Making Amazon Route 53 the DNS Service for an Existing Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the Route 53 documentation.
+ Create a public hosted zone for your domain in Route 53. For more information, see [Creating a Public Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the Route 53 documentation.
+ Create a static IP and attach it to your Lightsail instance. In this guide, you create a DNS record in your domain’s Route 53 hosted zone that resolves to the static IP address (public IP address) of your instance. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

## Point a domain to a Lightsail instance using Route 53
<a name="pointing-a-domain-to-a-lightsail-instance-using-route-53"></a>

Complete the following steps to create an address (A) record in Route 53 to point your domain to a Lightsail instance.

**Note**  
This procedure is also documented in the Route 53 Developer Guide. For more information, see [Creating Records by Using the Amazon Route 53 Console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) in the Route 53 documentation.

1. Sign in to the [Route 53 console](https://console.aws.amazon.com/route53).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the hosted zone for the domain name that you want to use to route traffic to your load balancer.

1. Choose **Create record**.

   The **Quick create record** page appears.  
![Create a record in Route 53 to point an alias to your Lightsail load balancer](http://docs.aws.amazon.com/lightsail/latest/userguide/images/create-record-set-alias-record-route-53-blank.png)
**Note**  
If you see the **Choose routing policy** page, then choose **Switch to quick create** to switch to the quick create wizard before continuing with the following steps.

1. Keep the **Record name** text box empty to point the apex of your domain, such as `example.com`, to an IP address, or enter a subdomain.

1. For **Record type**, choose **A - Routes traffic to an IPv4 address and some AWS resources**.

1. Enter the static IP address (public IP address) of your Lightsail instance in the **Value** text box.

1. Keep the TTL of 300, and the routing policy as **Simple routing**.  
![Address record example in a Route 53 hosted zone.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-route-53-hosted-zone-a-record.png)

1. Choose **Create records** to add the record to your hosted zone.
**Note**  
Allow time for the change to propagate through the internet's DNS. This may take a few minutes to several hours.

   To edit an existing record set in the Route 53 hosted zone, choose the record to edit, enter your changes, and then choose **Save**.