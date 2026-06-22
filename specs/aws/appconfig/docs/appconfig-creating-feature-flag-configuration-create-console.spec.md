---
id: "@specs/aws/appconfig/docs/appconfig-creating-feature-flag-configuration-create-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a feature flag configuration profile (console)"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a feature flag configuration profile (console)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-feature-flag-configuration-create-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a feature flag configuration profile (console)
<a name="appconfig-creating-feature-flag-configuration-create-console"></a>

Use the following procedure to create an AWS AppConfig feature flag configuration profile by using the AWS AppConfig console. At the time you create the configuration profile, you can also create a basic feature flag. 

**To create a configuration profile**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose an application you created in [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md).

1. On the **Configuration profiles and feature flags** tab, choose **Create configuration**.

1. In the **Configuration options** section, choose **Feature flag**.

1. In the **Configuration profile** section, for **Configuration profile name**, enter a name.

1. (Optional) Expand **Description** and enter a description.

1. (Optional) Expand **Additional options** and complete the following, as necessary.

   1. In the **Encryption** list, choose an AWS Key Management Service (AWS KMS) key from the list. This customer managed key enables you to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. For more information about this key, see **AWS AppConfig supports customer manager keys** in [Security in AWS AppConfig](appconfig-security.md).

   1. In the **Tags** section, choose **Add new tag**, and then specify a key and optional value. 

1. Choose **Next**.

1. In the **Feature flag definition** section, for **Flag name**, enter a name.

1. For **Flag key** enter a flag identifier to distinguish flags within the same configuration profile. Flags within the same configuration profile can't have the same key. After the flag is created, you can edit the flag name, but not the flag key. 

1. (Optional) Expand **Description** and enter information about this flag.

1. Select **This is a short-term flag** and optionally choose a date for when the flag should be disabled or deleted. AWS AppConfig does *not* disable the flag on the deprecation date. 

1. (Optional) In the **Feature flag attributes** section, choose **Define attribute**. Attributes enable you to provide additional values within your flag. For more information about attributes and constraints, see [Understanding feature flag attributes](appconfig-creating-configuration-and-profile-feature-flags.md#appconfig-creating-configuration-profile-feature-flag-attributes).

   1. For **Key**, specify a flag key and choose its type from the **Type** list. For information about the supported options for the **Value** and **Constraints** fields, see the previously referenced section about attributes.

   1. Select **Required value** to specify whether an attribute value is required.

   1. Choose **Define attribute** to add additional attributes.

1. In the **Feature flag value** section, choose **Enabled** to enable the flag. Use this same toggle to disable a flag when it reaches a specified deprecation date, if applicable.

1. Choose **Next**.

1. On the **Review and save** page, verify the details of the flag and then **Save and continue to deploy**.

Proceed to [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).