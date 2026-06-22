---
id: "@specs/aws/appconfig/docs/appconfig-creating-feature-flag-configuration-commandline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a feature flag configuration profile (command line)"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a feature flag configuration profile (command line)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-feature-flag-configuration-commandline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a feature flag configuration profile (command line)
<a name="appconfig-creating-feature-flag-configuration-commandline"></a>

The following procedure describes how to use the AWS Command Line Interface (on Linux or Windows) or Tools for Windows PowerShell to create an AWS AppConfig feature flag configuration profile. At the time you create the configuration profile, you can also create a basic feature flag.

**To create a feature flag configuration**

1. Open the AWS CLI.

1. Create a feature flag configuration profile specifying its **Type** as `AWS.AppConfig.FeatureFlags`. The configuration profile must use `hosted` for the location URI.

------
#### [ Linux ]

   ```
   aws appconfig create-configuration-profile \
     --application-id {{APPLICATION_ID}} \
     --name {{CONFIGURATION_PROFILE_NAME}} \
     --location-uri hosted \
     --type AWS.AppConfig.FeatureFlags
   ```

------
#### [ Windows ]

   ```
   aws appconfig create-configuration-profile ^
     --application-id {{APPLICATION_ID}} ^
     --name {{CONFIGURATION_PROFILE_NAME}} ^
     --location-uri hosted ^
     --type AWS.AppConfig.FeatureFlags
   ```

------
#### [ PowerShell ]

   ```
   New-APPCConfigurationProfile `
     -Name {{CONFIGURATION_PROFILE_NAME}} `
     -ApplicationId {{APPLICATION_ID}} `
     -LocationUri hosted `
     -Type AWS.AppConfig.FeatureFlags
   ```

------

1. Create your feature flag configuration data. Your data must be in a JSON format and conform to the `AWS.AppConfig.FeatureFlags` JSON schema. For more information about the schema, see [Understanding the type reference for AWS.AppConfig.FeatureFlags](appconfig-type-reference-feature-flags.md).

1. Use the `CreateHostedConfigurationVersion` API to save your feature flag configuration data to AWS AppConfig.

------
#### [ Linux ]

   ```
   aws appconfig create-hosted-configuration-version \
     --application-id {{APPLICATION_ID}} \
     --configuration-profile-id {{CONFIGURATION_PROFILE_ID}} \
     --content-type "application/json" \
     --content {{file://path/to/feature_flag_configuration_data.json}} \
     --cli-binary-format raw-in-base64-out
   ```

------
#### [ Windows ]

   ```
   aws appconfig create-hosted-configuration-version ^
     --application-id {{APPLICATION_ID}} ^
     --configuration-profile-id {{CONFIGURATION_PROFILE_ID}} ^
     --content-type "application/json" ^
     --content {{file://path/to/feature_flag_configuration_data.json}} ^
     --cli-binary-format raw-in-base64-out
   ```

------
#### [ PowerShell ]

   ```
   New-APPCHostedConfigurationVersion `
     -ApplicationId {{APPLICATION_ID}} `
     -ConfigurationProfileId {{CONFIGURATION_PROFILE_ID}} `
     -ContentType "application/json" `
     -Content {{file://path/to/feature_flag_configuration_data.json}}
   ```

------

   The command loads the content specified for the `Content` parameter from disk. The content must be similar to the following example.

   ```
   {
       "flags": {
           "ui_refresh": {
               "name": "UI Refresh"
           }
       },
       "values": {
           "ui_refresh": {
               "enabled": false,
               "attributeValues": {
                   "dark_mode_support": true
               }
           }
       },
       "version": "1"
   }
   ```

   The system returns information like the following.

------
#### [ Linux ]

   ```
   {
      "ApplicationId"          : "ui_refresh",
      "ConfigurationProfileId" : "UI Refresh",
      "VersionNumber"          : "1",
      "ContentType"            : "application/json"
   }
   ```

------
#### [ Windows ]

   ```
   {
      "ApplicationId"          : "ui_refresh",
      "ConfigurationProfileId" : "UI Refresh",
      "VersionNumber"          : "1",
      "ContentType"            : "application/json"
   }
   ```

------
#### [ PowerShell ]

   ```
   ApplicationId          : ui_refresh
   ConfigurationProfileId : UI Refresh
   VersionNumber          : 1
   ContentType            : application/json
   ```

------

   The `service_returned_content_file` contains your configuration data that includes some AWS AppConfig generated metadata.
**Note**  
When you create the hosted configuration version, AWS AppConfig verifies that your data conforms to the `AWS.AppConfig.FeatureFlags` JSON schema. AWS AppConfig additionally validates that each feature flag attribute in your data satisfies the constraints you defined for those attributes.