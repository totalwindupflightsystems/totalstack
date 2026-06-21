---
id: "@specs/aws/lightsail/docs/disable-ipv6"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Disable IPv6 networking for Lightsail resources"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Disable IPv6 networking for Lightsail resources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/disable-ipv6
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Disable IPv6 networking for Lightsail resources
<a name="disable-ipv6"></a>

Complete the following procedure to disable IPv6 for instances, CDN distributions, and load balancers.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Complete one of the following steps depending on the resource for which you want to disable IPv6:
   + To disable IPv6 for an instance, choose the **Instances** tab on the Lightsail home page, and then choose the name of the instance for which you want to disable IPv6.
   + To disable IPv6 for a CDN distribution or a load balancer, choose the **Networking** tab In the left navigation pane, and then choose the name of the CDN distribution or load balancer for which you want to disable IPv6.

1. Choose the **Networking** tab in the resource's management page.

1. In the **IPv6 Networking** section of the page, choose the toggle to disable IPv6 for the resource.  
![Disable IPv6 in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-disable-ipv6.png)