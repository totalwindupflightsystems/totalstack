---
id: "@specs/aws/appconfig/docs/appconfig-creating-configuration-profile-feature-flags-editing-version"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Saving a previous feature flag version to a new version"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Saving a previous feature flag version to a new version

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-configuration-profile-feature-flags-editing-version
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Saving a previous feature flag version to a new version
<a name="appconfig-creating-configuration-profile-feature-flags-editing-version"></a>

When you update a feature flag, AWS AppConfig automatically saves your changes to a new version. If you want to use a previous feature flag version, you must copy it to a draft version and then save it. You can't edit and save changes to a previous flag version without saving it to a new version. 

**To edit a previous feature flag version and save it to a new version**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose the application with the feature flag you want to edit and save to a new version.

1. On the **Configuration profiles and feature flags** tab, choose the configuration profile with the feature flag you want to edit and save to a new version.

1. On the **Feature flags** tab, use the **Version** list to choose the version you want to edit and save to a new version.

1. Choose **Copy to draft version**.

1. In the **Version label** field, enter a new label (optional, but recommended).

1. In the **Version description** field, enter a new description (optional, but recommended).

1. Choose **Save version**.

1. Choose **Start deployment** to deploy the new version.