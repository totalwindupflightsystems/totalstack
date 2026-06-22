---
id: "@specs/aws/appconfig/docs/appconfig-creating-namespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a namespace"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a namespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-namespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a namespace for your application in AWS AppConfig
<a name="appconfig-creating-namespace"></a>

The procedures in this section help you create an AWS AppConfig artifact called an application. An application is simply an organizational construct like a folder that identifies the namespace of your application. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users. You must create these artifacts before you can use AWS AppConfig to deploy and retrieve feature flags or free form configuration data. 

The following procedure gives you the option to associate an extension with a feature flag configuration profile. An *extension* augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration. For more information, see [Understanding AWS AppConfig extensions](working-with-appconfig-extensions-about.md).

**Note**  
You can use AWS CloudFormation to create AWS AppConfig artifacts, including applications, environments, configuration profiles, deployments, deployment strategies, and hosted configuration versions. For more information, see [AWS AppConfig resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppConfig.html) in the *AWS CloudFormation User Guide*.

**Topics**
+ [Creating an AWS AppConfig application (console)](#appconfig-creating-application-console)
+ [Creating an AWS AppConfig application (command line)](#appconfig-creating-application-commandline)

## Creating an AWS AppConfig application (console)
<a name="appconfig-creating-application-console"></a>

Use the following procedure to create an AWS AppConfig application by using the AWS Systems Manager console.

**To create an application**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose **Create application**.

1. For **Name**, enter a name for the application.

1. For **Description**, enter information about the application.

1. (Optional) In the **Extensions** section, choose an extension from the list. For more information, see [Understanding AWS AppConfig extensions](working-with-appconfig-extensions-about.md).

1. (Optional) In the **Tags** section, enter a key and an optional value. You can specify a maximum of 50 tags for a resource. 

1. Choose **Create application**.

AWS AppConfig creates the application and then displays the **Environments** tab. Proceed to [Creating environments for your application in AWS AppConfig](appconfig-creating-environment.md).

## Creating an AWS AppConfig application (command line)
<a name="appconfig-creating-application-commandline"></a>

The following procedure describes how to use the AWS CLI (on Linux or Windows) or AWS Tools for PowerShell to create an AWS AppConfig application.

**To create an application step by step**

1. Open the AWS CLI.

1. Run the following command to create an application. 

------
#### [ Linux ]

   ```
   aws appconfig create-application \
     --name {{A_name_for_the_application}} \
     --description {{A_description_of_the_application}} \  
     --tags {{User_defined_key_value_pair_metadata_for_the_application}}
   ```

------
#### [ Windows ]

   ```
   aws appconfig create-application ^
     --name {{A_name_for_the_application}} ^
     --description {{A_description_of_the_application}} ^
     --tags {{User_defined_key_value_pair_metadata_for_the_application}}
   ```

------
#### [ PowerShell ]

   ```
   New-APPCApplication `
     -Name {{Name_for_the_application}} `
     -Description {{Description_of_the_application}} `
     -Tag {{Hashtable_type_user_defined_key_value_pair_metadata_for_the_application}}
   ```

------

   The system returns information like the following.

------
#### [ Linux ]

   ```
   {
      "Id": "Application ID",
      "Name": "Application name",
      "Description": "Description of the application"
   }
   ```

------
#### [ Windows ]

   ```
   {
      "Id": "Application ID",
      "Name": "Application name",
      "Description": "Description of the application"
   }
   ```

------
#### [ PowerShell ]

   ```
   ContentLength    : Runtime of the command
   Description      : Description of the application
   HttpStatusCode   : HTTP Status of the runtime
   Id               : Application ID
   Name             : Application name
   ResponseMetadata : Runtime Metadata
   ```

------