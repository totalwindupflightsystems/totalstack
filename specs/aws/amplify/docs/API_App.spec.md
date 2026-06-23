---
id: "@specs/aws/amplify/docs/API_App"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS App"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# App

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_App
> **target_lang:** meta — documentation tier. ALL sections preserved.



# App
<a name="API_App"></a>

Represents the different branches of a repository for building, deploying, and hosting an Amplify app. 

## Contents
<a name="API_App_Contents"></a>

 ** appArn **   <a name="amplify-Type-App-appArn"></a>
The Amazon Resource Name (ARN) of the Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** appId **   <a name="amplify-Type-App-appId"></a>
The unique ID of the Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** createTime **   <a name="amplify-Type-App-createTime"></a>
A timestamp of when Amplify created the application.  
Type: Timestamp  
Required: Yes

 ** defaultDomain **   <a name="amplify-Type-App-defaultDomain"></a>
The default domain for the Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

 ** description **   <a name="amplify-Type-App-description"></a>
The description for the Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** enableBasicAuth **   <a name="amplify-Type-App-enableBasicAuth"></a>
Enables basic authorization for the Amplify app's branches.   
Type: Boolean  
Required: Yes

 ** enableBranchAutoBuild **   <a name="amplify-Type-App-enableBranchAutoBuild"></a>
Enables the auto-building of branches for the Amplify app.   
Type: Boolean  
Required: Yes

 ** environmentVariables **   <a name="amplify-Type-App-environmentVariables"></a>
The environment variables for the Amplify app.   
For a list of the environment variables that are accessible to Amplify by default, see [Amplify Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html) in the *Amplify Hosting User Guide*.  
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 5500.  
Value Pattern: `(?s).*`   
Required: Yes

 ** name **   <a name="amplify-Type-App-name"></a>
The name for the Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** platform **   <a name="amplify-Type-App-platform"></a>
The platform for the Amplify app. For a static app, set the platform type to `WEB`. For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE`. For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC`.  
If you are deploying an SSG only app with Next.js 14 or later, you must use the platform type `WEB_COMPUTE`.  
Type: String  
Valid Values: `WEB | WEB_DYNAMIC | WEB_COMPUTE`   
Required: Yes

 ** repository **   <a name="amplify-Type-App-repository"></a>
The Git repository for the Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** updateTime **   <a name="amplify-Type-App-updateTime"></a>
A timestamp of when Amplify updated the application.  
Type: Timestamp  
Required: Yes

 ** autoBranchCreationConfig **   <a name="amplify-Type-App-autoBranchCreationConfig"></a>
Describes the automated branch creation configuration for the Amplify app.   
Type: [AutoBranchCreationConfig](API_AutoBranchCreationConfig.md) object  
Required: No

 ** autoBranchCreationPatterns **   <a name="amplify-Type-App-autoBranchCreationPatterns"></a>
Describes the automated branch creation glob patterns for the Amplify app.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** basicAuthCredentials **   <a name="amplify-Type-App-basicAuthCredentials"></a>
The basic authorization credentials for branches for the Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.  
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*`   
Required: No

 ** buildSpec **   <a name="amplify-Type-App-buildSpec"></a>
Describes the content of the build specification (build spec) for the Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25000.  
Pattern: `(?s).+`   
Required: No

 ** cacheConfig **   <a name="amplify-Type-App-cacheConfig"></a>
The cache configuration for the Amplify app. If you don't specify the cache configuration `type`, Amplify uses the default `AMPLIFY_MANAGED` setting.  
Type: [CacheConfig](API_CacheConfig.md) object  
Required: No

 ** computeRoleArn **   <a name="amplify-Type-App-computeRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** customHeaders **   <a name="amplify-Type-App-customHeaders"></a>
Describes the custom HTTP headers for the Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000.  
Pattern: `(?s).*`   
Required: No

 ** customRules **   <a name="amplify-Type-App-customRules"></a>
Describes the custom redirect and rewrite rules for the Amplify app.   
Type: Array of [CustomRule](API_CustomRule.md) objects  
Required: No

 ** enableAutoBranchCreation **   <a name="amplify-Type-App-enableAutoBranchCreation"></a>
Enables automated branch creation for the Amplify app.   
Type: Boolean  
Required: No

 ** enableBranchAutoDeletion **   <a name="amplify-Type-App-enableBranchAutoDeletion"></a>
Automatically disconnect a branch in the Amplify console when you delete a branch from your Git repository.  
Type: Boolean  
Required: No

 ** iamServiceRoleArn **   <a name="amplify-Type-App-iamServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** jobConfig **   <a name="amplify-Type-App-jobConfig"></a>
The configuration details that apply to the jobs for an Amplify app.  
Type: [JobConfig](API_JobConfig.md) object  
Required: No

 ** productionBranch **   <a name="amplify-Type-App-productionBranch"></a>
Describes the information about a production branch of the Amplify app.   
Type: [ProductionBranch](API_ProductionBranch.md) object  
Required: No

 ** repositoryCloneMethod **   <a name="amplify-Type-App-repositoryCloneMethod"></a>
This is for internal use.
The Amplify service uses this parameter to specify the authentication protocol to use to access the Git repository for an Amplify app. Amplify specifies `TOKEN` for a GitHub repository, `SIGV4` for an AWS CodeCommit repository, and `SSH` for GitLab and Bitbucket repositories.  
Type: String  
Valid Values: `SSH | TOKEN | SIGV4`   
Required: No

 ** tags **   <a name="amplify-Type-App-tags"></a>
The tag for the Amplify app.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: No

 ** wafConfiguration **   <a name="amplify-Type-App-wafConfiguration"></a>
Describes the Firewall configuration for the Amplify app. Firewall support enables you to protect your hosted applications with a direct integration with AWS WAF.  
Type: [WafConfiguration](API_WafConfiguration.md) object  
Required: No

 ** webhookCreateTime **   <a name="amplify-Type-App-webhookCreateTime"></a>
A timestamp of when Amplify created the webhook in your Git repository.  
Type: Timestamp  
Required: No

## See Also
<a name="API_App_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/App) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/App) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/App) 