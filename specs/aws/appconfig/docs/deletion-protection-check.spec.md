---
id: "@specs/aws/appconfig/docs/deletion-protection-check"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bypassing or forcing a deletion protection check"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Bypassing or forcing a deletion protection check

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/deletion-protection-check
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Bypassing or forcing a deletion protection check
<a name="deletion-protection-check"></a>

To help you manage deletion protection, the [DeleteEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteEnvironment.html) and [DeleteConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteConfigurationProfile.html) APIs include a parameter called `DeletionProtectionCheck`. This parameter supports the following values:
+ `BYPASS`: Instructs AWS AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it. 
+ `APPLY`: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. `APPLY` also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks. 
+ `ACCOUNT_DEFAULT`: The default setting, which instructs AWS AppConfig to implement the deletion protection value specified in the `UpdateAccountSettings` API.

**Note**  
By default, `DeletionProtectionCheck` skips configuration profiles and environments created in the past hour. The default configuration is intended to prevent deletion protection from interferring with tests and demos that create short-lived resources. You can override this behavior by passing `DeletionProtectionCheck=APPLY` when calling `DeleteEnvironment` or `DeleteConfigurationProfile`.

The following CLI walkthrough uses sample commands to illustrate how to use the `DeletionProtectionCheck` parameter. Replace {{ID}} in the following commands with the ID for your AWS AppConfig artifacts.

1. Call [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) on a deployed configuration.

   ```
   aws appconfigdata get-latest-configuration --configuration-token $(aws appconfigdata start-configuration-session --application-identifier {{ID}} --environment-identifier {{ID}} --configuration-profile-identifier {{ID}} --query InitialConfigurationToken) outfile.txt 
   ```

1. Wait 60 seconds for AWS AppConfig to register that the configuration is active.

1. Run the following command to call [DeleteEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteEnvironment.html) and apply deletion protection on the environment.

   ```
   aws appconfig delete-environment --environment-id {{ID}} --application-id {{ID}} --deletion-protection-check APPLY
   ```

   The command should return the following error.

   ```
   An error occurred (BadRequestException) when calling the DeleteEnvironment operation: Environment Beta is actively being used in your application and cannot be deleted.
   ```

1. Run the following command to bypass deletion protection and delete the environment.

   ```
   aws appconfig delete-environment --environment-id {{ID}} --application-id {{ID}} --deletion-protection-check BYPASS
   ```