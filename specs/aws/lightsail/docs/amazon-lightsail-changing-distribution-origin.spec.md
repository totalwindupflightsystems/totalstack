---
id: "@specs/aws/lightsail/docs/amazon-lightsail-changing-distribution-origin"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Change origin"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Change origin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-changing-distribution-origin
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Change content origin for Lightsail distributions
<a name="amazon-lightsail-changing-distribution-origin"></a>

In this guide, we show you how to change the origin of your Amazon Lightsail distribution after you create it. An origin is the definitive source of content for your distribution. When you create your distribution, you choose the Lightsail instance, Lightsail bucket, or Lightsail load balancer (with one or more instances attached to it) that hosts the content of your website or web application. For more information, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

You can change the origin at any time after you create your distribution. When you change the origin, your distribution immediately begins replicating the change to the edge locations. Your distribution will continue to forward requests to the previous origin in a given edge location until the distribution is updated to the new origin in that edge location.

Changing the origin does not require your distribution to repopulate edge caches with content from your new origin. As long as the user requests in your website or web application have not changed, your distribution continues to serve content that is already in an edge cache until the cache lifespan for your content expires.

## Origin protocol policy
<a name="changing-distribution-origin-protocol-policy"></a>

The origin protocol policy is the protocol policy that your distribution uses when pulling content from your origin. After you choose an origin for your distribution, you should determine if your distribution should use Hypertext Transfer Protocol (HTTP) or Hypertext Transfer Protocol Secure (HTTPS) when pulling content from your origin. If your origin is not configured for HTTPS, then you must use HTTP.

You can choose one of the following origin protocol policies for your distribution:
+ **HTTP Only** - Your distribution uses only HTTP to access the origin. This is the default setting.
+ **HTTPS Only** - Your distribution uses only HTTPS to access the origin.

The steps to edit your origin protocol policy are included in the following [Change your distribution's origin](#changing-distribution-origin) section of this guide.

## Origin IP address type
<a name="changing-distribution-origin-ip-address-type"></a>

The origin IP address type determines which Internet Protocol version your distribution uses when communicating with your origin resource. After you choose an origin for your distribution, you can select the IP address type that your distribution should use to connect to the origin.

You can choose one of the following origin IP address types for your distribution:
+ **IPv4-only** - Your distribution uses only IPv4 to communicate with the origin. For instance origins, a static IP must be attached.
+ **Dual-stack** - Your distribution can use either IPv4 or IPv6 to communicate with the origin. For instance origins, a static IP must be attached.
+ **IPv6-only** - Your distribution uses only IPv6 to communicate with the origin. For instance origins, no static IP is required, but the instance must have IPv6 connectivity.

The steps to edit your origin IP address type are included in the following [Change your distribution's origin](#changing-distribution-origin) section of this guide.

## Change your distribution's origin
<a name="changing-distribution-origin"></a>

Complete the following procedure to change your distribution's origin.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to change the origin.

1. Choose the **Details** tab on your distribution's management page, and scroll to the **Choose your origin** section of the page.

   The **Select your origin** section of the page displays your distribution's current origin.

1. Choose **Change origin**.

1. Choose the AWS Region in which your origin resource was created.

   Distributions are global resources. They can reference an origin in any AWS Region, and distribute its content globally.

1. Choose your origin. An origin can be an instance, bucket, or a load balancer (with one or more instances attached to it).

1. Choose **Save** to update your distribution with your new origin.

   After you choose an origin for your distribution, you should determine if your distribution should use Hypertext Transfer Protocol (HTTP) or Hypertext Transfer Protocol Secure (HTTPS) when pulling content from your origin.

1. (Optional) To change your origin protocol policy, choose the pencil icon displayed next to the current origin protocol policy that your distribution uses. For more information, see [Origin protocol policy](#changing-distribution-origin-protocol-policy).

   This option is listed in the **Choose your origin** section of the page, under the origin resource you selected for your distribution.
**Note**  
When you select a Lightsail bucket as the origin of your distribution, the **Origin protocol policy** defaults to **HTTPS only**. You cannot change the origin protocol policy when a bucket is the origin of your distribution.  
![Origin protocol policy](http://docs.aws.amazon.com/lightsail/latest/userguide/images/origin-protocol-policy.png)

1. Choose **HTTP only** or **HTTPS only**, then choose **Save** to save the origin protocol policy.

1. (Optional) To change your origin IP address type, choose the pencil icon displayed next to the current origin IP address type that your distribution uses. For more information, see [Origin IP address type](#changing-distribution-origin-ip-address-type).

   This option is listed in the **Choose your origin** section of the page, under the origin resource you selected for your distribution.
**Note**  
The Origin IP address type setting is only available for instance origins. When you select a bucket, container service, or load balancer as the origin, the **Origin IP address type** defaults to **IPv4-only** and cannot be changed.  
![Origin IP address type](http://docs.aws.amazon.com/lightsail/latest/userguide/images/origin-ip-address-type.png)

1. Choose **IPv4-only**, **Dual-stack**, or **IPv6-only**, then choose **Save** to save the origin IP address type.

When you save changes to your distribution's configuration, your distribution starts to propagate the changes to all edge locations. Until your configuration is updated in an edge location, your distribution continues to serve your content from that location based on the previous configuration. After your configuration is updated in an edge location, your distribution immediately starts to serve your content from that location based on the new configuration.

Your changes don't propagate to every edge location instantaneously. When propagation is complete, the status of your distribution changes from **InProgress** to **Enabled**. While your distribution is propagating your changes, we can't determine whether a given edge location is serving your content based on the previous configuration or the new configuration.