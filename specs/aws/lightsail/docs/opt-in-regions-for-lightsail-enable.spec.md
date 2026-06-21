---
id: "@specs/aws/lightsail/docs/opt-in-regions-for-lightsail-enable"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable Regions"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Enable Regions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/opt-in-regions-for-lightsail-enable
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable opt-in Regions for Lightsail
<a name="opt-in-regions-for-lightsail-enable"></a>

You can enable the supported opt-in Region for Lightsail for no additional charge. You're charged only for resources that you create in the newly enabled Region. This process takes a few minutes for most accounts. For additional information about working with Regions, see [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html).

**Note**  
Before you can use the opt-in Region with Lightsail, the **Opt-in status** must be **Enabled** on the Lightsail console.

This procedure details how to enable an opt-in Region starting from the Lightsail console.

**To enable an opt-in Region for Lightsail**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the Lightsail home page, choose your user or role on the top navigation menu.

1. Choose **Account** in the dropdown menu.  
![Lightsail account tab](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-console-account-menu.png)

1. On the account page, choose the **Profile** tab.

1. In the **Supported opt-in Regions** section, choose **Start opt-in** for the Region that you want to enable.  
![Displays an opt-in Region in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/opt-in-regions-region-is-disabled.png)

1. Review the opt-in information and choose **Start Opt-in**.

1. Review the required steps and choose **Manage AWS profile** to proceed. The [AWS Account Management](https://console.aws.amazon.com/billing/home#/account) console page should open. Leave the Lightsail console open for later steps.

1. In the AWS Regions section, select the Region that you want to enable, then choose **Enable**.
**Note**  
The Region names in Lightsail vary slightly as compared to the Region names in other AWS services. For example, *Jakarta (ap-southeast-3)* in the Lightsail console is the same as *Asia Pacific (Jakarta)* in the AWS Account Management console.  
![Displays how to start enabling an opt-in Region from your AWS profile.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/opt-in-regions-enable-region.png)

1. Review any additional information that is displayed, then choose **Enable Region** to proceed with the operation.

1. Return to your account page in the Lightsail console to periodically check the **Opt-in status** value for the Region. The **Opt-in status** should show as **Enabling** until the process completes and updates to **Enabled**. You can now provision resources in the new Region.  
![Displays how to start enabling an opt-in Region from your AWS profile.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/opt-in-regions-region-is-enabled.png)