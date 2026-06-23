---
id: "@specs/aws/amplify/docs/API_CreateApp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateApp"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CreateApp

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CreateApp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateApp
<a name="API_CreateApp"></a>

Creates a new Amplify app. 

## Request Syntax
<a name="API_CreateApp_RequestSyntax"></a>

```
POST /apps HTTP/1.1
Content-type: application/json

{
   "accessToken": "{{string}}",
   "autoBranchCreationConfig": { 
      "basicAuthCredentials": "{{string}}",
      "buildSpec": "{{string}}",
      "enableAutoBuild": {{boolean}},
      "enableBasicAuth": {{boolean}},
      "enablePerformanceMode": {{boolean}},
      "enablePullRequestPreview": {{boolean}},
      "environmentVariables": { 
         "{{string}}" : "{{string}}" 
      },
      "framework": "{{string}}",
      "pullRequestEnvironmentName": "{{string}}",
      "stage": "{{string}}"
   },
   "autoBranchCreationPatterns": [ "{{string}}" ],
   "basicAuthCredentials": "{{string}}",
   "buildSpec": "{{string}}",
   "cacheConfig": { 
      "type": "{{string}}"
   },
   "computeRoleArn": "{{string}}",
   "customHeaders": "{{string}}",
   "customRules": [ 
      { 
         "condition": "{{string}}",
         "source": "{{string}}",
         "status": "{{string}}",
         "target": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "enableAutoBranchCreation": {{boolean}},
   "enableBasicAuth": {{boolean}},
   "enableBranchAutoBuild": {{boolean}},
   "enableBranchAutoDeletion": {{boolean}},
   "environmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "iamServiceRoleArn": "{{string}}",
   "jobConfig": { 
      "buildComputeType": "{{string}}"
   },
   "name": "{{string}}",
   "oauthToken": "{{string}}",
   "platform": "{{string}}",
   "repository": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateApp_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessToken](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-accessToken"></a>
The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.  
Use `accessToken` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use `oauthToken`.  
You must specify either `accessToken` or `oauthToken` when you create a new app.  
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** [autoBranchCreationConfig](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-autoBranchCreationConfig"></a>
The automated branch creation configuration for an Amplify app.   
Type: [AutoBranchCreationConfig](API_AutoBranchCreationConfig.md) object  
Required: No

 ** [autoBranchCreationPatterns](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-autoBranchCreationPatterns"></a>
The automated branch creation glob patterns for an Amplify app.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** [basicAuthCredentials](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-basicAuthCredentials"></a>
The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.  
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*`   
Required: No

 ** [buildSpec](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-buildSpec"></a>
The build specification (build spec) for an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25000.  
Pattern: `(?s).+`   
Required: No

 ** [cacheConfig](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-cacheConfig"></a>
The cache configuration for the Amplify app.  
Type: [CacheConfig](API_CacheConfig.md) object  
Required: No

 ** [computeRoleArn](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-computeRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assign to an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [customHeaders](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-customHeaders"></a>
The custom HTTP headers for an Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000.  
Pattern: `(?s).*`   
Required: No

 ** [customRules](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-customRules"></a>
The custom rewrite and redirect rules for an Amplify app.   
Type: Array of [CustomRule](API_CustomRule.md) objects  
Required: No

 ** [description](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-description"></a>
The description of the Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [enableAutoBranchCreation](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-enableAutoBranchCreation"></a>
Enables automated branch creation for an Amplify app.   
Type: Boolean  
Required: No

 ** [enableBasicAuth](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-enableBasicAuth"></a>
Enables basic authorization for an Amplify app. This will apply to all branches that are part of this app.   
Type: Boolean  
Required: No

 ** [enableBranchAutoBuild](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-enableBranchAutoBuild"></a>
Enables the auto building of branches for an Amplify app.   
Type: Boolean  
Required: No

 ** [enableBranchAutoDeletion](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-enableBranchAutoDeletion"></a>
Automatically disconnects a branch in the Amplify console when you delete a branch from your Git repository.   
Type: Boolean  
Required: No

 ** [environmentVariables](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-environmentVariables"></a>
The environment variables map for an Amplify app.   
For a list of the environment variables that are accessible to Amplify by default, see [Amplify Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html) in the *Amplify Hosting User Guide*.  
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 5500.  
Value Pattern: `(?s).*`   
Required: No

 ** [iamServiceRoleArn](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-iamServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [jobConfig](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-jobConfig"></a>
Describes the configuration details that apply to the jobs for an Amplify app.  
Type: [JobConfig](API_JobConfig.md) object  
Required: No

 ** [name](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-name"></a>
The name of the Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [oauthToken](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-oauthToken"></a>
The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.  
Use `oauthToken` for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use `accessToken`.  
You must specify either `oauthToken` or `accessToken` when you create a new app.  
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .  
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [platform](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-platform"></a>
The platform for the Amplify app. For a static app, set the platform type to `WEB`. For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE`. For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC`.  
If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to `WEB_COMPUTE` and set the artifacts `baseDirectory` to `.next` in the application's build settings. For an example of the build specification settings, see [Amplify build settings for a Next.js 14 SSG application](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-app.html#build-setting-detection-ssg-14) in the *Amplify Hosting User Guide*.  
Type: String  
Valid Values: `WEB | WEB_DYNAMIC | WEB_COMPUTE`   
Required: No

 ** [repository](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-repository"></a>
The Git repository for the Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [tags](#API_CreateApp_RequestSyntax) **   <a name="amplify-CreateApp-request-tags"></a>
The tag for an Amplify app.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: No

## Response Syntax
<a name="API_CreateApp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "app": { 
      "appArn": "string",
      "appId": "string",
      "autoBranchCreationConfig": { 
         "basicAuthCredentials": "string",
         "buildSpec": "string",
         "enableAutoBuild": boolean,
         "enableBasicAuth": boolean,
         "enablePerformanceMode": boolean,
         "enablePullRequestPreview": boolean,
         "environmentVariables": { 
            "string" : "string" 
         },
         "framework": "string",
         "pullRequestEnvironmentName": "string",
         "stage": "string"
      },
      "autoBranchCreationPatterns": [ "string" ],
      "basicAuthCredentials": "string",
      "buildSpec": "string",
      "cacheConfig": { 
         "type": "string"
      },
      "computeRoleArn": "string",
      "createTime": number,
      "customHeaders": "string",
      "customRules": [ 
         { 
            "condition": "string",
            "source": "string",
            "status": "string",
            "target": "string"
         }
      ],
      "defaultDomain": "string",
      "description": "string",
      "enableAutoBranchCreation": boolean,
      "enableBasicAuth": boolean,
      "enableBranchAutoBuild": boolean,
      "enableBranchAutoDeletion": boolean,
      "environmentVariables": { 
         "string" : "string" 
      },
      "iamServiceRoleArn": "string",
      "jobConfig": { 
         "buildComputeType": "string"
      },
      "name": "string",
      "platform": "string",
      "productionBranch": { 
         "branchName": "string",
         "lastDeployTime": number,
         "status": "string",
         "thumbnailUrl": "string"
      },
      "repository": "string",
      "repositoryCloneMethod": "string",
      "tags": { 
         "string" : "string" 
      },
      "updateTime": number,
      "wafConfiguration": { 
         "statusReason": "string",
         "wafStatus": "string",
         "webAclArn": "string"
      },
      "webhookCreateTime": number
   }
}
```

## Response Elements
<a name="API_CreateApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [app](#API_CreateApp_ResponseSyntax) **   <a name="amplify-CreateApp-response-app"></a>
Represents the different branches of a repository for building, deploying, and hosting an Amplify app.   
Type: [App](API_App.md) object

## Errors
<a name="API_CreateApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** DependentServiceFailureException **   
An operation failed because a dependent service threw an exception.   
HTTP Status Code: 503

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** LimitExceededException **   
A resource could not be created because service quotas were exceeded.   
HTTP Status Code: 429

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_CreateApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/CreateApp) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CreateApp) 