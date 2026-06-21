---
id: "@specs/aws/lightsail/docs/amazon-lighstail-changing-distribution-plan"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Change plan"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Change plan

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lighstail-changing-distribution-plan
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Adjust the data transfer quota for your Lightsail distribution
<a name="amazon-lighstail-changing-distribution-plan"></a>

When you create a Amazon Lightsail distribution, you choose a distribution plan that specifies the monthly data transfer quota and cost of your distribution. If your distribution transfers more data than your plan's monthly data transfer quota, you are charged an overage. For more information about overage pricing, see the [Lightsail pricing page](https://aws.amazon.com/lightsail/pricing/).

To avoid an overage fee, change your distribution's current plan to a different plan that offers a greater amount of monthly data transfer before your distribution exceeds its monthly quota. You can change your distribution's plan only one time during each AWS billing cycle. In this guide, we show you how to change your distribution's plan.

For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

## Change your distribution plan
<a name="changing-distribution-plan"></a>

Complete the following procedure to change your distribution's plan.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to view the current monthly data transfer.

1. Choose the **Details** tab on your distribution's management page.

1. In the **Data transfer** section of the page, choose **Change distribution plan**.

1. At the confirmation prompt, choose **Yes, change** to confirm that you want to change your distribution's plan.

1. On the next prompt, choose the new plan for your distribution, and choose **Select plan**.

1. On the next prompt, choose **Yes, apply** to confirm that you want to apply the new plan to your distribution. Or choose **No, go back** to not apply the new plan to your distribution.