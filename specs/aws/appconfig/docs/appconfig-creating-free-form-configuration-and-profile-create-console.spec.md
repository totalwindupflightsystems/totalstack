---
id: "@specs/aws/appconfig/docs/appconfig-creating-free-form-configuration-and-profile-create-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating an AWS AppConfig freeform configuration profile (console)"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating an AWS AppConfig freeform configuration profile (console)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-free-form-configuration-and-profile-create-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating an AWS AppConfig freeform configuration profile (console)
<a name="appconfig-creating-free-form-configuration-and-profile-create-console"></a>

Use the following procedure to create an AWS AppConfig freeform configuration profile and (optionally) a freeform-configuration by using the AWS Systems Manager console.

**To create a freeform configuration profile**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose an application you created in [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md).

1. Choose the **Configuration profiles and feature flags** tab, and then choose **Create configuration**.

1. In the **Configuration options** section, choose **Freeform configuration**.

1. For **Configuration profile name**, enter a name for the configuration profile.

1. (Optional) Expand **Description** and enter a description.

1. (Optional) Expand **Additional options** and complete the following, as necessary.

   1. In the **Associate extensions** section, choose an extension from the list.

   1. In the **Tags** section, choose **Add new tag**, and then specify a key and optional value. 

1. Choose **Next**.

1. On the **Specify configuration data** page, in the **Configuration definition** section, choose an option.

1. Complete the fields for the option you selected, as described in the following table.  
****    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.html)

1. In the **Service role** section, choose **New service role** to have AWS AppConfig create the IAM role that provides access to the configuration data. AWS AppConfig automatically populates the **Role name** field based on the name you entered earlier. Or, choose **Existing service role**. Choose the role by using the **Role ARN** list.

1. Optionally, on the **Add validators** page, choose either **JSON Schema** or **AWS Lambda**. If you choose **JSON Schema**, enter the JSON Schema in the field. If you choose **AWS Lambda**, choose the function Amazon Resource Name (ARN) and the version from the list. 
**Important**  
Configuration data stored in SSM documents must validate against an associated JSON Schema before you can add the configuration to the system. SSM parameters do not require a validation method, but we recommend that you create a validation check for new or updated SSM parameter configurations by using AWS Lambda.

1. Choose **Next**.

1. On the **Review and save** page, choose **Save and continue to deploy**.

**Important**  
If you created a configuration profile for AWS CodePipeline, then you must create a pipeline in CodePipeline that specifies AWS AppConfig as the *deploy provider*. You don't need to perform [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md). However, you must configure a client to receive application configuration updates as described in [Retrieving configuration data without AWS AppConfig Agent](about-data-plane.md). For information about creating a pipeline that specifies AWS AppConfig as the deploy provider, see [Tutorial: Create a Pipeline that Uses AWS AppConfig as a Deployment Provider](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-AppConfig.html) in the *AWS CodePipeline User Guide*. 

Proceed to [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).