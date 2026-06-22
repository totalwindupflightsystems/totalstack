---
id: "@specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-procedures"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a multi-variant feature flag"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a multi-variant feature flag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-procedures
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a multi-variant feature flag
<a name="appconfig-creating-multi-variant-feature-flags-procedures"></a>

Use the procedures in this section to create variants of a feature flag.

**Before you begin**  
Note the following important information.
+ You can create variants of existing feature flags by editing them. You can't create variants of a new feature flag *when you create a new configuration profile*. You must complete the workflow of creating the new configuration profile first. After you create the configuration profile, you can add variants to any flag within the configuration profile. For information about how to create a new configuration profile, see [Creating a feature flag configuration profile in AWS AppConfig](appconfig-creating-configuration-and-profile-feature-flags.md).
+ To retrieve feature flag variant data for Amazon EC2, Amazon ECS, and Amazon EKS compute platforms, you must use AWS AppConfig Agent version 2.0.4416 or later.
+ For performance reasons, AWS CLI and SDK calls to AWS AppConfig don't retrieve variant data. For more information about AWS AppConfig Agent, see [How to use AWS AppConfig Agent to retrieve configuration data](appconfig-agent-how-to-use.md).
+ When you create a feature flag variant, you specify a rule for it. Rules are expressions that take request context as input and produce a boolean result as output. Before you create variants, review the supported operands and operators for flag variant rules. You can create rules before you create variants. For more information, see [Understanding multi-variant feature flag rules](appconfig-creating-multi-variant-feature-flags-rules.md).

**Topics**
+ [Creating a multi-variant feature flag (console)](#appconfig-creating-multi-variant-feature-flags-procedures-console)
+ [Creating a multi-variant feature flag (command line)](#appconfig-creating-multi-variant-feature-flags-procedures-commandline)

## Creating a multi-variant feature flag (console)
<a name="appconfig-creating-multi-variant-feature-flags-procedures-console"></a>

The following procedure describes how to create a multi-variant feature flag for an existing configuration profile by using the AWS AppConfig console. You can also edit existing feature flags to create variants.

**To create a multi-variant feature flag**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose an application.

1. On the **Configuration profiles and feature flags** tab, choose an existing feature flag configuration profile.

1. In the **Flags** section, choose **Add new flag**.

1. In the **Feature flag definition** section, for **Flag name**, enter a name.

1. For **Flag key** enter a flag identifier to distinguish flags within the same configuration profile. Flags within the same configuration profile can't have the same key. After the flag is created, you can edit the flag name, but not the flag key. 

1. (Optional) In the **Description** field, enter information about this flag.

1. In the **Variants** section, choose **Multi-variant flag**.

1. (Optional) In the **Feature flag attributes** section, choose **Define attribute**. Attributes enable you to provide additional values within your flag. For more information about attributes and constraints, see [Understanding feature flag attributes](appconfig-creating-configuration-and-profile-feature-flags.md#appconfig-creating-configuration-profile-feature-flag-attributes).

   1. For **Key**, specify a flag key and choose its type from the **Type** list. For information about the supported options for the **Value** and **Constraints** fields, see the previously referenced section about attributes.

   1. Select **Required value** to specify whether an attribute value is required.

   1. Choose **Define attribute** to add additional attributes.

   1. Choose **Apply** to save attribute changes.

1. In the **Feature flag variants** section, choose **Create variant**.

   1. For **Variant name**, enter a name.

   1. Use the **Enabled value** toggle to enable the variant.

   1. In the **Rule** text box, enter a rule.

   1. Use the **Create variant** > **Create variant above** or **Create variant below** options to create additional variants for this flag. 

   1. In the **Default variant** section, use the **Enabled value** toggle to enable the default variant. Optionally, provide values for attributes defined in step 10.

   1. Choose **Apply**.

1. Verify the details of the flag and its variants and choose **Create flag**.

For information about deploying your new feature flag with variants, see [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).

## Creating a multi-variant feature flag (command line)
<a name="appconfig-creating-multi-variant-feature-flags-procedures-commandline"></a>

The following procedure describes how to use the AWS Command Line Interface (on Linux or Windows) or Tools for Windows PowerShell to create a multi-variant feature flag for an existing configuration profile. You can also edit existing feature flags to create variants.

**Before you begin**  
Complete the following tasks before you create a multi-variant feature flag by using the AWS CLI.
+ Create a feature flag configuration profile. For more information, see [Creating a feature flag configuration profile in AWS AppConfig](appconfig-creating-configuration-and-profile-feature-flags.md).
+ Update to the latest version of the AWS CLI. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

**To create a multi-variant feature flag**

1. Create a configuration file on your local machine that specifies the details of the multi-variant flag you want to create. Save the file with a `.json` file extension. The file must adhere to the [https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html) JSON schema. The schema contents of your configuration file will be similar to the following.

   ```
   {
     "flags": {
       "{{FLAG_NAME}}": {
         "attributes": {
             "{{ATTRIBUTE_NAME}}": {
             "constraints": {
               "type": "{{CONSTRAINT_TYPE}}"
             }
           }
         },
         "description": "{{FLAG_DESCRIPTION}}",
         "name": "{{VARIANT_NAME}}"
       }
     },
     "values": {
       "{{VARIANT_VALUE_NAME}}": {
         "_variants": [
           {
             "attributeValues": {
               "{{ATTRIBUTE_NAME}}": {{BOOLEAN}}
             },
             "enabled": {{BOOLEAN}},
             "name": "{{VARIANT_NAME}}",
             "rule": "{{VARIANT_RULE}}"
           },
           {
             "attributeValues": {
               "{{ATTRIBUTE_NAME}}": {{BOOLEAN}}
             },
             "enabled": {{BOOLEAN}},
             "name": "{{VARIANT_NAME}}",
             "rule": "{{VARIANT_RULE}}"
           },
           {
             "attributeValues": {
               "{{ATTRIBUTE_NAME}}": {{BOOLEAN}}
             },
             "enabled": {{BOOLEAN}},
             "name": "{{VARIANT_NAME}}",
             "rule": "{{VARIANT_RULE}}"
           },
           {
             "attributeValues": {
               "{{ATTRIBUTE_NAME}}": {{BOOLEAN}}
             },
             "enabled": {{BOOLEAN}},
             "name": "{{VARIANT_NAME}}",
             "rule": "{{VARIANT_RULE}}"
           }
         ]
       }
     },
     "version": "{{VERSION_NUMBER}}"
   }
   ```

   Here is an example with three variants and the default variant.

   ```
   {
     "flags": {
       "ui_refresh": {
         "attributes": {
           "dark_mode_support": {
             "constraints": {
               "type": "boolean"
             }
           }
         },
         "description": "A release flag used to release a new UI",
         "name": "UI Refresh"
       }
     },
     "values": {
       "ui_refresh": {
         "_variants": [
           {
             "attributeValues": {
               "dark_mode_support": true
             },
             "enabled": true,
             "name": "QA",
             "rule": "(ends_with $email \"qa-testers.mycompany.com\")"
           },
           {
             "attributeValues": {
               "dark_mode_support": true
             },
             "enabled": true,
             "name": "Beta Testers",
             "rule": "(exists key::\"opted_in_to_beta\")"
           },
           {
             "attributeValues": {
               "dark_mode_support": false
             },
             "enabled": true,
             "name": "Sample Population",
             "rule": "(split pct::10 by::$email)"
           },
           {
             "attributeValues": {
               "dark_mode_support": false
             },
             "enabled": false,
             "name": "Default Variant"
           }
         ]
       }
     },
     "version": "1"
   }
   ```

1. Use the `CreateHostedConfigurationVersion` API to save your feature flag configuration data to AWS AppConfig.

------
#### [ Linux ]

   ```
   aws appconfig create-hosted-configuration-version \
     --application-id {{APPLICATION_ID}} \
     --configuration-profile-id {{CONFIGURATION_PROFILE_ID}} \
     --content-type "application/json" \
     --content {{file://path/to/feature_flag_configuration_data.json \}}
     --cli-binary-format raw-in-base64-out \
     outfile
   ```

------
#### [ Windows ]

   ```
   aws appconfig create-hosted-configuration-version ^
     --application-id {{APPLICATION_ID}} ^
     --configuration-profile-id {{CONFIGURATION_PROFILE_ID}} ^
     --content-type "application/json" ^
     --content {{file://path/to/feature_flag_configuration_data.json}} ^
     --cli-binary-format raw-in-base64-out ^
     outfile
   ```

------
#### [ PowerShell ]

   ```
   New-APPCHostedConfigurationVersion `
     -ApplicationId {{APPLICATION_ID}} `
     -ConfigurationProfileId {{CONFIGURATION_PROFILE_ID}} `
     -ContentType "application/json" `
     -Content {{file://path/to/feature_flag_configuration_data.json}} `
     -Raw
   ```

------

   The `service_returned_content_file` contains your configuration data that includes some AWS AppConfig generated metadata.
**Note**  
When you create the hosted configuration version, AWS AppConfig verifies that your data conforms to the [https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html) JSON schema. AWS AppConfig additionally validates that each feature flag attribute in your data satisfies the constraints you defined for those attributes.