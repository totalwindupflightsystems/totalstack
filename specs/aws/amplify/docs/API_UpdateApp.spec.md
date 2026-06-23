---
id: "@specs/aws/amplify/docs/API_UpdateApp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateApp"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# UpdateApp

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_UpdateApp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateApp
<a name="API_UpdateApp"></a>

Updates an existing Amplify app. 

## Request Syntax
<a name="API_UpdateApp_RequestSyntax"></a>

```
POST /apps/{{appId}} HTTP/1.1
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
   "repository": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_UpdateApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessToken](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-accessToken"></a>
The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.  
Use `accessToken` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use `oauthToken`.  
You must specify either `accessToken` or `oauthToken` when you update an app.  
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** [autoBranchCreationConfig](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-autoBranchCreationConfig"></a>
The automated branch creation configuration for an Amplify app.   
Type: [AutoBranchCreationConfig](API_AutoBranchCreationConfig.md) object  
Required: No

 ** [autoBranchCreationPatterns](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-autoBranchCreationPatterns"></a>
Describes the automated branch creation glob patterns for an Amplify app.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** [basicAuthCredentials](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-basicAuthCredentials"></a>
The basic authorization credentials for an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.  
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*`   
Required: No

 ** [buildSpec](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-buildSpec"></a>
The build specification (build spec) for an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25000.  
Pattern: `(?s).+`   
Required: No

 ** [cacheConfig](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-cacheConfig"></a>
The cache configuration for the Amplify app.  
Type: [CacheConfig](API_CacheConfig.md) object  
Required: No

 ** [computeRoleArn](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-computeRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assign to an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [customHeaders](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-customHeaders"></a>
The custom HTTP headers for an Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000.  
Pattern: `(?s).*`   
Required: No

 ** [customRules](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-customRules"></a>
The custom redirect and rewrite rules for an Amplify app.   
Type: Array of [CustomRule](API_CustomRule.md) objects  
Required: No

 ** [description](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-description"></a>
The description for an Amplify app.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [enableAutoBranchCreation](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-enableAutoBranchCreation"></a>
Enables automated branch creation for an Amplify app.   
Type: Boolean  
Required: No

 ** [enableBasicAuth](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-enableBasicAuth"></a>
Enables basic authorization for an Amplify app.   
Type: Boolean  
Required: No

 ** [enableBranchAutoBuild](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-enableBranchAutoBuild"></a>
Enables branch auto-building for an Amplify app.   
Type: Boolean  
Required: No

 ** [enableBranchAutoDeletion](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-enableBranchAutoDeletion"></a>
Automatically disconnects a branch in the Amplify console when you delete a branch from your Git repository.   
Type: Boolean  
Required: No

 ** [environmentVariables](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-environmentVariables"></a>
The environment variables for an Amplify app.   
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 5500.  
Value Pattern: `(?s).*`   
Required: No

 ** [iamServiceRoleArn](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-iamServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [jobConfig](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-jobConfig"></a>
Describes the configuration details that apply to the jobs for an Amplify app.  
Type: [JobConfig](API_JobConfig.md) object  
Required: No

 ** [name](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-name"></a>
The name for an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** [oauthToken](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-oauthToken"></a>
The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.  
Use `oauthToken` for repository providers other than GitHub, such as Bitbucket or CodeCommit.  
To authorize access to GitHub as your repository provider, use `accessToken`.  
You must specify either `oauthToken` or `accessToken` when you update an app.  
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .  
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [platform](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-platform"></a>
The platform for the Amplify app. For a static app, set the platform type to `WEB`. For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE`. For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC`.  
If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to `WEB_COMPUTE`.  
Type: String  
Valid Values: `WEB | WEB_DYNAMIC | WEB_COMPUTE`   
Required: No

 ** [repository](#API_UpdateApp_RequestSyntax) **   <a name="amplify-UpdateApp-request-repository"></a>
The name of the Git repository for an Amplify app.  
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

## Response Syntax
<a name="API_UpdateApp_ResponseSyntax"></a>

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
<a name="API_UpdateApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [app](#API_UpdateApp_ResponseSyntax) **   <a name="amplify-UpdateApp-response-app"></a>
Represents the updated Amplify app.   
Type: [App](API_App.md) object

## Errors
<a name="API_UpdateApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_UpdateApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/UpdateApp) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/UpdateApp) 