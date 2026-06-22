---
id: "@specs/aws/appconfig/docs/appconfig-creating-configuration-profile-other-data-sources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a configuration profile for non-native data sources"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a configuration profile for non-native data sources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-configuration-profile-other-data-sources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a configuration profile for non-native data sources
<a name="appconfig-creating-configuration-profile-other-data-sources"></a>

AWS AppConfig supports deploying configuration data from most any data store. Natively, AWS AppConfig supports deploying configuration data stored in the following services:
+ The AWS AppConfig hosted configuration store
+ Amazon S3
+ AWS Secrets Manager
+ AWS Systems Manager Parameter Store
+ Systems Manager Document Store
+ AWS CodePipeline

If your configuration data is stored in a location not natively supported by AWS AppConfig, you can create an [AWS AppConfig extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) to retrieve your data from its source. For example, by using an AWS AppConfig extension, you can retrieve configuration data stored in Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB (DynamoDB), GitHub, GitLab, or a local repo, to name a few. By implementing an extension, you can take advantage of AWS AppConfig security and DevOps enhancements for your applications and computing environment. You can also use this method as you migrate configuration data from legacy systems into AWS AppConfig.

Creating a configuration profile for data sources not natively supported in AWS AppConfig involves the following processes or actions:

1. Create an [AWS Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) that fetches data from your data source. As long as a Lambda function can access the data source, your AWS AppConfig extension will be able to retrieve the data. 

1. Create a custom AWS AppConfig extension that invokes your Lambda function. For more information, see [Walkthrough: Creating custom AWS AppConfig extensions](working-with-appconfig-extensions-creating-custom.md).

1. Create an AWS AppConfig free-form configuration profile. Specifically, create a configuration profile that uses the **AWS AppConfig hosted configuration** definition. The configuration profile functions as a temporary data store after your Lambda function retrieves your configuration from your source. Your application will retrieve the configuration data from the AWS AppConfig hosted configuration store. For more information, see [Creating a free form configuration profile in AWS AppConfig](appconfig-free-form-configurations-creating.md).

1. Create an extension association that triggers using the `PRE_CREATE_HOSTED_CONFIGURATION_VERSION` action point. For more information, see [Step 4: Create an extension association for a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-association.md).

Once configured, when your application requests a new version of the configuration data, the Lambda fetches your configuration data and pulls it into the configuration profile. AWS AppConfig then saves the configuration profile and your third-party data.

When you're ready, you can deploy the configuration profile to your applications, just like any other type of configuration data.

**Note**  
You can choose to insert third-party data in line with existing configuration data, or have the entire contents of the configuration data contain only the third-party data. If you want to have the data in line with other existing data, that logic should be part of the Lambda function that imports the data from the third-party source.

## Migrating to AWS AppConfig from legacy and home-grown configuration services
<a name="appconfig-creating-configuration-profile-other-data-sources-migrating"></a>

If you've started using AWS AppConfig and still have legacy configuration data or feature flags in another system, you can use the process described earlier in this topic to migrate off of your legacy system and onto AWS AppConfig. You can build an extension that pulls data out of your legacy system and deploys it through AWS AppConfig. Using AWS AppConfig in this way provides you with all of the safety guardrail controls and benefits while still using your legacy data stores.