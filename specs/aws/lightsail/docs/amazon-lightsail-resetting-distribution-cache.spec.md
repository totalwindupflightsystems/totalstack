---
id: "@specs/aws/lightsail/docs/amazon-lightsail-resetting-distribution-cache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Reset cache"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Reset cache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-resetting-distribution-cache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Reset the cache of your Lightsail distribution
<a name="amazon-lightsail-resetting-distribution-cache"></a>

The cache lifespan (time to live) setting controls the amount of time your content stays in your Amazon Lightsail distribution's cache. You can also manually reset the cache on your distribution if you need to clear it before the cache lifespan interval. After you clear the cache, the next time a user requests content, your distribution pulls the latest version of your content from your origin and caches it. In this guide, we show you how to manually reset the cache on your distribution. For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

## Reset the cache of your distribution
<a name="reset-distribution-cache"></a>

Complete the following procedure to reset the cache of your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to reset the cache.

1. Choose the **Cache** tab on your distribution's management page.

1. Scroll to the **Reset cache** section of the page, and choose **Reset cache**.

1. At the confirmation prompt, choose **Yes, reset** to confirm that you want to reset your distribution's cache. Or choose **No, cancel** to not reset your distribution's cache.