---
id: "@specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-versions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding available versions of the AWS AppConfig Agent Lambda extension"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding available versions of the AWS AppConfig Agent Lambda extension

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-versions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding available versions of the AWS AppConfig Agent Lambda extension
<a name="appconfig-integration-lambda-extensions-versions"></a>

This topic includes information about AWS AppConfig Agent Lambda extension versions. The AWS AppConfig Agent Lambda extension supports Lambda functions developed for the x86-64 and ARM64 (Graviton2) platforms. To work properly, your Lambda function must be configured to use the specific Amazon Resource Name (ARN) for the AWS Region where it is currently hosted. You can view AWS Region and ARN details later in this section.

**Important**  
Note the following important details about the AWS AppConfig Agent Lambda extension.  
The `GetConfiguration` API action was deprecated on January 28, 2022. Calls to receive configuration data should use the `StartConfigurationSession` and `GetLatestConfiguration` APIs instead. If you are using a version of the AWS AppConfig Agent Lambda extension created after January 28, 2022, you need to configure permissions to the new APIs. For more information, see [Retrieving configuration data without AWS AppConfig Agent](about-data-plane.md).
AWS AppConfig supports all of the versions listed in [Older extension versions](#appconfig-integration-lambda-extensions-enabling-older-versions). We recommend that you periodically update to the latest version to take advantage of extension enhancements.

**Topics**
+ [AWS AppConfig Agent Lambda Extension release notes](#appconfig-integration-lambda-extensions-versions-release-notes)
+ [Finding your Lambda extension version number](#appconfig-integration-lambda-extensions-versions-find)
+ [x86-64 platform](#appconfig-integration-lambda-extensions-enabling-x86-64)
+ [ARM64 platform](#appconfig-integration-lambda-extensions-enabling-ARM64)
+ [Older extension versions](#appconfig-integration-lambda-extensions-enabling-older-versions)

## AWS AppConfig Agent Lambda Extension release notes
<a name="appconfig-integration-lambda-extensions-versions-release-notes"></a>

The following table describes changes made to recent versions of the AWS AppConfig Lambda extension.


****  

| Version | Launch date | Notes | 
| --- | --- | --- | 
| 2.0.17054.0 | 05/14/2026 | Minor enhancements and bug fixes.  | 
| 2.0.14126.0 | 03/25/2026 | Minor enhancements and bug fixes.  | 
| 2.0.11962.0 | 02/20/2026 | Improved environment support, minor enhancements, and bug fixes.  | 
| 2.0.8693 | 11/20/2025 | Improved environment support, minor enhancements, and bug fixes. Added support for the following AWS Regions[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html) | 
| 2.0.2037 | 05/12/2025 | Added `/ping` path, which exposes a simple health check that returns that agent's version. Also includes minor enhancements and bug fixes.  | 
| 2.0.1079 | 12/12/2024 | Minor enhancements and bug fixes. | 
| 2.0.719 | 08/08/2024 | Minor enhancements and bug fixes. | 
| 2.0.678 | 07/23/2024 | Enhancements to support feature flag targets, variants, and splits. For more information, see [Creating multi-variant feature flags](appconfig-creating-multi-variant-feature-flags.md).  | 
| 2.0.501 | 07/01/2024 | Minor enhancements and bug fixes. | 
| 2.0.358 | 12/01/2023 | Added support for the following [retrieval features:](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-additional-features.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html) | 
| 2.0.181 | 08/14/2023 | Added support for the Israel (Tel Aviv) il-central-1 AWS Region. | 
| 2.0.165 | 02/21/2023 | Minor bug fixes. No longer restricting extension use to specific runtime versions via the AWS Lambda console. Added support for the following AWS Regions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html) | 
| 2.0.122 | 08/23/2022 | Added support for a tunneling proxy, which can be configured with the `AWS_APPCONFIG_EXTENSION_PROXY_URL` and `AWS_APPCONFIG_EXTENSION_PROXY_HEADERS` environment variables. Added .NET 6 as a runtime. For more information about environment variables, see [Configuring the AWS AppConfig Agent Lambda extension](appconfig-integration-lambda-extensions-config.md).  | 
| 2.0.58 | 05/03/2022 | Improved support for Graviton2 (ARM64) processors in Lambda. | 
| 2.0.45 | 03/15/2022 | Added support for calling a single feature flag. Previously, customers called feature flags grouped into a configuration profile and had to parse the response client-side. With this release, customers can use a `flag=<flag-name>` parameter when calling the HTTP localhost endpoint to get the value of a single flag. Also added initial support for Graviton2 (ARM64) processors.  | 

## Finding your Lambda extension version number
<a name="appconfig-integration-lambda-extensions-versions-find"></a>

Use the following procedure to locate the version number of your currently configured AWS AppConfig Agent Lambda extension. To work properly, your Lambda function must be configured to use the specific Amazon Resource Name (ARN) for the AWS Region where it is currently hosted.

1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. Choose the Lambda function where you want to add the `AWS-AppConfig-Extension` layer.

1. In the **Layers** section, choose **Add a layer**.

1. In the **Choose a layer** section, choose **AWS-AppConfig-Extension** from the **AWS layers** list.

1. Use the **Version** list to choose a version number.

1. Choose **Add**.

1. Use the **Test** tab to test the function.

1. After the test completes, view the log output. Locate the AWS AppConfig Agent Lambda extension version in the **Details of the Execution** section. This version must match the required URLs for that version. 

## x86-64 platform
<a name="appconfig-integration-lambda-extensions-enabling-x86-64"></a>

When you add the extension as a layer to your Lambda, you must specify an ARN. Choose an ARN from the following table that corresponds with the AWS Region where you created the Lambda. These ARNs are for Lambda functions developed for the x86-64 platform.


**Version 2.0.17054.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:321` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:277` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:395` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:373` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:262` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:172` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:295` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:220` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:303` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:242` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:273` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:367` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:249` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:214` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:243` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:241` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:254` | 
| Asia Pacific (Taipei) | `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension:147` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:272` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:273` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:272` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:258` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:313` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:256` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:188` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:161` | 
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension:97` | 
| Asia Pacific (Thailand) | `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension:134` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:290` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:217` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:327` | 
| Mexico (Central) | `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension:142` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:260` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:188` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:212` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:254` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:219` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:220` | 

## ARM64 platform
<a name="appconfig-integration-lambda-extensions-enabling-ARM64"></a>

When you add the extension as a layer to your Lambda, you must specify an ARN. Choose an ARN from the following table that corresponds with the AWS Region where you created the Lambda. These ARNs are for Lambda functions developed for the ARM64 platform.


**Version 2.0.17054.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:254` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:229` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:272` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:275` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:182` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:162` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:238` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:178` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:241` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:194` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:192` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:226` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:177` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:175` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:182` | 
| Asia Pacific (Taipei) | `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension-Arm64:121` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:225` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:181` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:187` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:210` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:256` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:193` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:173` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:136` | 
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension-Arm64:87` | 
| Asia Pacific (Thailand) | `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension-Arm64:133` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:232` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:175` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:215` | 
| Mexico (Central) | `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension-Arm64:141` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:188` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:168` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:182` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:171` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:165` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:163` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:165` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:166` | 

## Older extension versions
<a name="appconfig-integration-lambda-extensions-enabling-older-versions"></a>

This section lists the ARNs and AWS Regions for older versions of the AWS AppConfig Lambda extension. This list doesn't contain information for all previous versions of the AWS AppConfig Agent Lambda extension, but it will be updated when new versions are released.

**Topics**
+ [Older extension versions (x86-64 platform)](#appconfig-integration-lambda-extensions-enabling-older-versions-x86-64)
+ [Older extension versions (ARM64 platform)](#appconfig-integration-lambda-extensions-enabling-older-versions-ARM64)

### Older extension versions (x86-64 platform)
<a name="appconfig-integration-lambda-extensions-enabling-older-versions-x86-64"></a>

The following tables list ARNs and the AWS Regions for older versions of the AWS AppConfig Agent Lambda extension developed for the x86-64 platform.

Date replaced by newer extension: 05/14/2026


**Version 2.0.14126.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:317` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:273` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:383` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:369` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:258` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:168` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:291` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:216` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:299` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:238` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:269` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:363` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:245` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:210` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:249` | 
| Asia Pacific (Taipei) | `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension:139` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:286` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:213` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:268` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:269` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:268` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:254` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:309` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:252` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:184` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:157` | 
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension:87` | 
| Asia Pacific (Thailand) | `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension:130` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:256` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:184` | 
| Mexico (Central) | `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension:138` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:323` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:236` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:237` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:215` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:214` | 

Date replaced by newer extension: 03/25/2026


**Version 2.0.11962.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:296`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:252`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:359`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:348`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:239`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:147`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:270`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:195`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:278`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:217`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:248`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:342`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:226`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:189`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:219`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:221`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:228`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:245`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:248`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:247`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:233`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:288`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:231`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:163`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:136`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:264`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:192`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension:58`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension:109`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension:118`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:302`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension:115`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:234`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:168`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:206`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:244`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:184`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:182`  | 

Date replaced by newer extension: 02/17/2026


**Version 2.0.8693**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:279`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:235`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:348`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:335`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:228`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:130`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:261`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:178`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:261`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:207`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:235`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:333`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:215`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:176`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:205`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:203`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:217`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:228`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:239`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:234`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:224`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:272`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:222`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:152`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:127`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:248`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:179`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension:41`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension:98`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension:100 `  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:288`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension:98`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:225`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:155`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:195`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:227`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:184`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:182`  | 

Date replaced by newer extension: 11/20/2025


**Version 2.0.2037**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:207` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:162` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:258` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:262` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:152` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:57` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:189` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:106` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:189` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:133` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:162` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:259` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:140` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:102` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:133` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:131` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:142` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:155` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:165` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:159` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:156` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:199` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:150` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:78` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:55` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:175` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:104` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:215` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:152` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:81` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:120` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:154` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:110` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:109` | 

Date replaced by newer extension: 05/20/2025


**Version 2.0.1079**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:174` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:133` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:223` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:230` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:123` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:27` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:159` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:77` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:160` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:121` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:133` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:225` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:111` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:74` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:106` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:104` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:113` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:126` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:136` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:130` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:134` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:165` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:121` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:49` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:26` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:146` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:75` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:179` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:123` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:52` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:91` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:125` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:80` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:80` | 

Date replaced by newer extension: 12/12/2024


**Version 2.0.719**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:173` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:132` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:221` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:229` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:121` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:27` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:158` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:75` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:159` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:120` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:132` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:224` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:110` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:72` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:104` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:102` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:112` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:125` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:135` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:129` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:132` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:164` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:120` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:48` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension:25` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:145` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:74` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:178` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:122` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:50` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:90` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:124` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:79` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:79` | 

Date replaced by newer extension: 08/08/2024


**Version 2.0.678**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:167` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:126` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:213` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:223` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:116` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:21` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:152` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:70` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:153` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:114` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:126` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:218` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:104` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:67` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:99` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:97` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:106` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:119` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:129` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:123` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:127` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:158` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:114` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:42` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:139` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:68` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:172` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:116` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:45` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:84` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:118` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:73` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:73` | 

Date replaced by newer extension: 07/23/2024


**Version 2.0.501**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:153` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:112` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:195` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:210` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:101` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:136` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:53` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:144` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:99` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:111` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:201` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:89` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:50` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:85` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:83` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:91` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:104` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:114` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:107` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:112` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:142` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:98` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:26` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:125` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:53` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:155` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:102` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:28` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:68` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:103` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:59` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:59` | 

Date replaced by newer extension: 07/01/2024


**Version 2.0.358**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:128` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:93` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:141` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:161` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:93` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:106` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:47` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:125` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:93` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:98` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:159` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:83` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:44` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:76` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:76` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:83` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:98` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:108` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:101` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:106` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:106` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:79` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:20` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:107` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:47` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:128` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:83` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:22` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:49` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:85` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:54` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:54` | 

Date replaced by newer extension: 12/01/2023


**Version 2.0.181**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:113` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:81` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:124` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:146` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:81` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:93` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:32` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:110` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:81` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:82` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:142` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:73` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:29` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:68` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:68` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:73` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:84` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:93` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:86` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:91` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:93` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:64` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:5` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:94` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:32` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:113` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:73` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension:7` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:34` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:73` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:46` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:46` | 

Date replaced by newer extension: 08/14/2023


**Version 2.0.165**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:110` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:79` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:121` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:143` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:79` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:91` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension:29` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:108` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:79` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:80` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:139` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:71` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension:26` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:66` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:66` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:71` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:82` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:91` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:84` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:89` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:91` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:60` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension:2` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:92` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension:29` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:110` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:71` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension:31` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:71` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:44` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:44` | 

Date replaced by newer extension: 02/21/2023


**Version 2.0.122**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:82` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:59` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:93` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:114` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:59` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:70` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:82` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:59` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:60` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:111` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:54` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:52` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:52` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:54` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:62` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:70` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:59` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:64` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:70` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:37` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:71` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:82` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:54` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:54` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:29` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:29` | 

Date replaced by newer extension: 08/23/2022


**Version 2.0.58**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:69` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:50` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:78` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:101` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:50` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:59` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:69` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:50` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:51` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:98` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:47` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:46` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:46` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:47` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:49` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:59` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:46` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:51` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:59` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:24` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:60` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:69` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:47` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:47` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:23` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:23` | 

Date replaced by newer extension: 04/21/2022


**Version 2.0.45**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:68` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:49` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:77` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:100` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:49` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:58` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:68` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:49` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:50` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:97` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:46` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:45` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:45` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:46` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:48` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:58` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:45` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:50` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:58` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:23` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:59` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:68` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:46` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:46` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:22` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:22` | 

Date replaced by newer extension: 03/15/2022


**Version 2.0.30**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:61` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:47` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:61` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:89` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:47` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:54` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:59` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:47` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:48` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:86` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:44` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension:43` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension:43` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:44` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:45` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension:42` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:54` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:45` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:54` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension:13` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:55` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:61` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:44` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:44` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension:20` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension:20` | 

### Older extension versions (ARM64 platform)
<a name="appconfig-integration-lambda-extensions-enabling-older-versions-ARM64"></a>

The following tables list ARNs and the AWS Regions for older versions of the AWS AppConfig Agent Lambda extension developed for the ARM64 platform.

Date replaced by newer extension: 05/14/2026


**Version 2.0.14126.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:250` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:225` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:260` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:271` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:178` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:158` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:234` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:174` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:237` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:190` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:188` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:222` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:173` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:171` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:177` | 
| Asia Pacific (Taipei) | `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension-Arm64:113` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:228` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:171` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:221` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:177` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:183` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:206` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:252` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:189` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:169` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:132` | 
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension-Arm64:77` | 
| Asia Pacific (Thailand) | `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension-Arm64:129` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:184` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:167` | 
| Mexico (Central) | `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension-Arm64:137` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:211` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:158` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:159` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:161` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:160` | 

Date replaced by newer extension: 03/25/2026


**Version 2.0.11962.0**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:229`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:204`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:236`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:250`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:159`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:137`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:213`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:153`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:216`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:169`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:167`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:201`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:154`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:150`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:156`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension-Arm64:92`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:198`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:156`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:162`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:185`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:231`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:168`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:148`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:111`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension-Arm64:48`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension-Arm64:108`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:206`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:150`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:190`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension-Arm64:114`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:162`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:162`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:172`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:151`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:141`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:143`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:130`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:128`  | 

Date replaced by newer extension: 02/17/2026


**Version 2.0.8693**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:212 ` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:187 ` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:225 ` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:237 ` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:148 ` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:120 ` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:204 ` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:136 ` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:199 ` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:159` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:154` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:192 ` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:143 ` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:137 ` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:145 ` | 
| Asia Pacific (Taipei) | `arn:aws:lambda:ap-east-2:730335625313:layer:AWS-AppConfig-Extension-Arm64:74 ` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:181 ` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:147 ` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:149 ` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:176 ` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:215 ` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:159 ` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:137 ` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:102 ` | 
| Asia Pacific (New Zealand) | `arn:aws:lambda:ap-southeast-6:381491832265:layer:AWS-AppConfig-Extension-Arm64:31 ` | 
| Asia Pacific (Thailand) | `arn:aws:lambda:ap-southeast-7:851725616657:layer:AWS-AppConfig-Extension-Arm64:97 ` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:190 ` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:137 ` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:176 ` | 
| Mexico (Central) | `arn:aws:lambda:mx-central-1:891376990304:layer:AWS-AppConfig-Extension-Arm64:97 ` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:153 ` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:151 ` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:155 ` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:138 ` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:127 ` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:125 ` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:130 ` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:128 ` | 

Date replaced by newer extension: 11/20/2025


**Version 2.0.2037**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:140` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:114` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:135` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:164` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:72` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:47` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:132` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:64` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:127` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:85` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:81` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:118` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:68` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:63` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:70` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:108` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:73` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:74` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:108` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:142` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:87` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:63` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:30` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:117` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:62` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:103` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:80` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:76` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:82` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:64` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:55` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:53` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:56` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:55` | 

Date replaced by newer extension: 05/20/2025


**Version 2.0.1079**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:107` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:85` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:100` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:132` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:43` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:18` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:102` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:35` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:98` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:73` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:52` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:84` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:39` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:35` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:41` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:79` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:44` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:45` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:86` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:108` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:58` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:34` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:88` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:33` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:67` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:51` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:47` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:53` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:35` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:28` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:26` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:26` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:26` | 

Date replaced by newer extension: 12/12/2024


**Version 2.0.678**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:106` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:84` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:98` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:131` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:41` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension-Arm64:17` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:101` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:33` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:97` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:72` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:51` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:83` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:38` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:33` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:40` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:78` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:43` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:44` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:84` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:107` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:57` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:33` | 
| Asia Pacific (Malaysia) | `arn:aws:lambda:ap-southeast-5:631746059939:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:87` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:32` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:66` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:50` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:46` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:52` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:33` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:26` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:24` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:25` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:25` | 

Date replaced by newer extension: 08/08/2024


**Version 2.0.678**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:100` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:78` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:90` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:125` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:11` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:36` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:95` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:28` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:91` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:66` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:45` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:77` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:32` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:28` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:34` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:72` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:37` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:38` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:79` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:101` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:51` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:27` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:81` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:26` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:60` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:44` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:40` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:46` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:28` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:21` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:19` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:19` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:19` | 

Date replaced by newer extension: 07/23/2024


**Version 2.0.501**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:86` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:64` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:72` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:112` | 
| Canada West (Calgary) | `arn:aws:lambda:ca-west-1:436199621743:layer:AWS-AppConfig-Extension:1` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:21` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:79` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:82` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:51` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:30` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:60` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:17` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:19` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:57` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:22` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:22` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:64` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:85` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:35` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:67` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:11` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:43` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:30` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:24` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:31` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:11` | 
| China (Beijing) | `arn:aws-cn:lambda:cn-north-1:615057806174:layer:AWS-AppConfig-Extension-Arm64:7` | 
| China (Ningxia) | `arn:aws-cn:lambda:cn-northwest-1:615084187847:layer:AWS-AppConfig-Extension-Arm64:5` | 
| AWS GovCloud (US-East) | `arn:aws-us-gov:lambda:us-gov-east-1:946561847325:layer:AWS-AppConfig-Extension-Arm64:5` | 
| AWS GovCloud (US-West) | `arn:aws-us-gov:lambda:us-gov-west-1:946746059096:layer:AWS-AppConfig-Extension-Arm64:5` | 

Date replaced by newer extension: 07/01/2024


**Version 2.0.358**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:61` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:45` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:18` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:63` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:13` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:49` | 
| Europe (Zurich) | `arn:aws:lambda:eu-central-2:758369105281:layer:AWS-AppConfig-Extension-Arm64:5` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:63` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:45` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:17` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:18` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Europe (Spain) | `arn:aws:lambda:eu-south-2:586093569114:layer:AWS-AppConfig-Extension-Arm64:5` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:51` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:58` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:49` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Asia Pacific (Melbourne) | `arn:aws:lambda:ap-southeast-4:307021474294:layer:AWS-AppConfig-Extension-Arm64:5` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:49` | 
| Asia Pacific (Hyderabad) | `arn:aws:lambda:ap-south-2:489524808438:layer:AWS-AppConfig-Extension-Arm64:5` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Middle East (UAE) | `arn:aws:lambda:me-central-1:662846165436:layer:AWS-AppConfig-Extension-Arm64:5` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:13` | 
| Israel (Tel Aviv) | `arn:aws:lambda:il-central-1:895787185223:layer:AWS-AppConfig-Extension-Arm64:5` | 

Date replaced by newer extension: 12/01/2023


**Version 2.0.181**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:46` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:33` | 
| US West (N. California) | `arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension-Arm64:1` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:48` | 
| Canada (Central) | `arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:36` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:48` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:33` | 
| Europe (Paris) | `arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Europe (Stockholm) | `arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Europe (Milan) | `arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Hong Kong) | `arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:37` | 
| Asia Pacific (Seoul) | `arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Osaka) | `arn:aws:lambda:ap-northeast-3:706869817123:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:43` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:36` | 
| Asia Pacific (Jakarta) | `arn:aws:lambda:ap-southeast-3:418787028745:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:36` | 
| South America (São Paulo) | `arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Africa (Cape Town) | `arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Middle East (Bahrain) | `arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension-Arm64:1` | 

Date replaced by newer extension: 03/30/2023


**Version 2.0.165**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:43` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:31` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:45` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:34` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:46` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:31` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:35` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:41` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:34` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:34` | 

Date replaced by newer extension: 02/21/2023


**Version 2.0.122**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:15` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:11` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:13` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:20` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:11` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:15` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:16` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:13` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:13` | 

Date replaced by newer extension: 08/23/2022


**Version 2.0.58**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:2` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:2` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:3` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:7` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:3` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:2` | 

Date replaced by newer extension: 04/21/2022


**Version 2.0.45**  

| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) | `arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension-Arm64:1` | 
| US East (Ohio) | `arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension-Arm64:1` | 
| US West (Oregon) | `arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Europe (Frankfurt) | `arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Europe (Ireland) | `arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension-Arm64:6` | 
| Europe (London) | `arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Tokyo) | `arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Singapore) | `arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension-Arm64:2` | 
| Asia Pacific (Sydney) | `arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension-Arm64:1` | 
| Asia Pacific (Mumbai) | `arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension-Arm64:1` | 