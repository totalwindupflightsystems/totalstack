---
id: "@specs/aws/amplify/docs/API_Branch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Branch"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# Branch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_Branch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Branch
<a name="API_Branch"></a>

 The branch for an Amplify app, which maps to a third-party repository branch. 

## Contents
<a name="API_Branch_Contents"></a>

 ** activeJobId **   <a name="amplify-Type-Branch-activeJobId"></a>
 The ID of the active job for a branch of an Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** branchArn **   <a name="amplify-Type-Branch-branchArn"></a>
 The Amazon Resource Name (ARN) for a branch that is part of an Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** branchName **   <a name="amplify-Type-Branch-branchName"></a>
 The name for the branch that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** createTime **   <a name="amplify-Type-Branch-createTime"></a>
A timestamp of when Amplify created the branch.  
Type: Timestamp  
Required: Yes

 ** customDomains **   <a name="amplify-Type-Branch-customDomains"></a>
 The custom domains for a branch of an Amplify app.   
Type: Array of strings  
Array Members: Maximum number of 255 items.  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** description **   <a name="amplify-Type-Branch-description"></a>
 The description for the branch that is part of an Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** displayName **   <a name="amplify-Type-Branch-displayName"></a>
 The display name for the branch. This is used as the default domain prefix.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

 ** enableAutoBuild **   <a name="amplify-Type-Branch-enableAutoBuild"></a>
 Enables auto-building on push for a branch of an Amplify app.   
Type: Boolean  
Required: Yes

 ** enableBasicAuth **   <a name="amplify-Type-Branch-enableBasicAuth"></a>
 Enables basic authorization for a branch of an Amplify app.   
Type: Boolean  
Required: Yes

 ** enableNotification **   <a name="amplify-Type-Branch-enableNotification"></a>
 Enables notifications for a branch that is part of an Amplify app.   
Type: Boolean  
Required: Yes

 ** enablePullRequestPreview **   <a name="amplify-Type-Branch-enablePullRequestPreview"></a>
 Enables pull request previews for the branch.   
Type: Boolean  
Required: Yes

 ** environmentVariables **   <a name="amplify-Type-Branch-environmentVariables"></a>
 The environment variables specific to a branch of an Amplify app.   
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 5500.  
Value Pattern: `(?s).*`   
Required: Yes

 ** framework **   <a name="amplify-Type-Branch-framework"></a>
 The framework for a branch of an Amplify app.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

 ** stage **   <a name="amplify-Type-Branch-stage"></a>
 The current stage for the branch that is part of an Amplify app.   
Type: String  
Valid Values: `PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST`   
Required: Yes

 ** totalNumberOfJobs **   <a name="amplify-Type-Branch-totalNumberOfJobs"></a>
 The total number of jobs that are part of an Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** ttl **   <a name="amplify-Type-Branch-ttl"></a>
 The content Time to Live (TTL) for the website in seconds.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 32.  
Pattern: `\d*`   
Required: Yes

 ** updateTime **   <a name="amplify-Type-Branch-updateTime"></a>
A timestamp for the last updated time for a branch.  
Type: Timestamp  
Required: Yes

 ** associatedResources **   <a name="amplify-Type-Branch-associatedResources"></a>
 A list of custom resources that are linked to this branch.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** backend **   <a name="amplify-Type-Branch-backend"></a>
Describes the backend associated with an Amplify `Branch`.  
This property is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.  
Type: [Backend](API_Backend.md) object  
Required: No

 ** backendEnvironmentArn **   <a name="amplify-Type-Branch-backendEnvironmentArn"></a>
 The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.   
This property is available to Amplify Gen 1 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** basicAuthCredentials **   <a name="amplify-Type-Branch-basicAuthCredentials"></a>
 The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.  
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*`   
Required: No

 ** buildSpec **   <a name="amplify-Type-Branch-buildSpec"></a>
 The build specification (build spec) content for the branch of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25000.  
Pattern: `(?s).+`   
Required: No

 ** computeRoleArn **   <a name="amplify-Type-Branch-computeRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role for a branch of an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** destinationBranch **   <a name="amplify-Type-Branch-destinationBranch"></a>
 The destination branch if the branch is a pull request branch.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** enablePerformanceMode **   <a name="amplify-Type-Branch-enablePerformanceMode"></a>
Enables performance mode for the branch.  
Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.   
Type: Boolean  
Required: No

 ** enableSkewProtection **   <a name="amplify-Type-Branch-enableSkewProtection"></a>
Specifies whether the skew protection feature is enabled for the branch.  
Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see [Skew protection for Amplify deployments](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html) in the *Amplify User Guide*.  
Type: Boolean  
Required: No

 ** pullRequestEnvironmentName **   <a name="amplify-Type-Branch-pullRequestEnvironmentName"></a>
 The Amplify environment name for the pull request.   
Type: String  
Length Constraints: Maximum length of 20.  
Pattern: `(?s).*`   
Required: No

 ** sourceBranch **   <a name="amplify-Type-Branch-sourceBranch"></a>
 The source branch if the branch is a pull request branch.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** tags **   <a name="amplify-Type-Branch-tags"></a>
 The tag for the branch of an Amplify app.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: No

 ** thumbnailUrl **   <a name="amplify-Type-Branch-thumbnailUrl"></a>
 The thumbnail URL for the branch of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## See Also
<a name="API_Branch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/Branch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/Branch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/Branch) 