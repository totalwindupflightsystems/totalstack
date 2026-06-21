---
id: "@specs/aws/lightsail/docs/enable-ipv6"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable IPv6 networking for Lightsail resources"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Enable IPv6 networking for Lightsail resources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/enable-ipv6
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable IPv6 networking for Lightsail resources
<a name="enable-ipv6"></a>

Complete the following procedure to enable IPv6 for instances, CDN distributions, and load balancers.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Complete one of the following steps depending on the resource for which you want to enable IPv6:
   + To enable IPv6 for an instance, choose the **Instances** tab on the Lightsail home page, and then choose the name of the instance for which you want to enable IPv6.
   + To enable IPv6 for a CDN distribution or a load balancer, choose the **Networking** tab In the left navigation pane, and then choose the name of the CDN distribution or load balancer for which you want to enable IPv6.

1. Choose the **Networking** tab in the resource's management page.

1. In the **IPv6 Networking** section of the page, choose the toggle to enable IPv6 for the resource.  
![Enable IPv6 in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-enable-ipv6.png)

   Be aware of the following items after you enable IPv6 for a resource:
   + If you enable IPv6 for a CDN distribution or load balancer, then that resource begins accepting IPv6 traffic. If you enable IPv6 for an instance, then an IPv6 address is assigned to it, and the IPv6 firewall becomes available, as shown in the following example.  
![The instance IPv6 firewall in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-ipv6-firewall.png)
   + Instances that use the following blueprints require additional steps after enabling IPv6 to ensure the instance becomes aware of its new IPv6 address:
     + **cPanel** – For more information, see [Configure IPv6 for cPanel instances](amazon-lightsail-configure-ipv6-on-cpanel.md).
     + **GitLab** – For more information, see [Configure IPv6 for GitLab instances](amazon-lightsail-configure-ipv6-on-gitlab.md).
     + **Nginx** – For more information, see [Configure IPv6 for Nginx instances](amazon-lightsail-configure-ipv6-on-nginx.md).
     + **Plesk** – For more information, see [Configure IPv6 for Plesk instances](amazon-lightsail-configure-ipv6-on-plesk.md).
   + If you have a registered domain name directing traffic to you instance, container service, CDN distribution, or load balancer, then make sure to create an IPv6 address record (AAAA) in the DNS of your domain to route IPv6 traffic to your resource.