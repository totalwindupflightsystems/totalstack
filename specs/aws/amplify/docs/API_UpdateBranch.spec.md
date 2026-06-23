---
id: "@specs/aws/amplify/docs/API_UpdateBranch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateBranch"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# UpdateBranch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_UpdateBranch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateBranch
<a name="API_UpdateBranch"></a>

 Updates a branch for an Amplify app. 

## Request Syntax
<a name="API_UpdateBranch_RequestSyntax"></a>

```
POST /apps/{{appId}}/branches/{{branchName}} HTTP/1.1
Content-type: application/json

{
   "backend": { 
      "stackArn": "{{string}}"
   },
   "backendEnvironmentArn": "{{string}}",
   "basicAuthCredentials": "{{string}}",
   "buildSpec": "{{string}}",
   "computeRoleArn": "{{string}}",
   "description": "{{string}}",
   "displayName": "{{string}}",
   "enableAutoBuild": {{boolean}},
   "enableBasicAuth": {{boolean}},
   "enableNotification": {{boolean}},
   "enablePerformanceMode": {{boolean}},
   "enablePullRequestPreview": {{boolean}},
   "enableSkewProtection": {{boolean}},
   "environmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "framework": "{{string}}",
   "pullRequestEnvironmentName": "{{string}}",
   "stage": "{{string}}",
   "ttl": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBranch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-uri-branchName"></a>
The name of the branch.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

## Request Body
<a name="API_UpdateBranch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [backend](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-backend"></a>
The backend for a `Branch` of an Amplify app. Use for a backend created from an CloudFormation stack.  
This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.  
Type: [Backend](API_Backend.md) object  
Required: No

 ** [backendEnvironmentArn](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-backendEnvironmentArn"></a>
The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app.   
This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [basicAuthCredentials](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-basicAuthCredentials"></a>
 The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format `user:password`.  
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*`   
Required: No

 ** [buildSpec](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-buildSpec"></a>
 The build specification (build spec) for the branch.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25000.  
Pattern: `(?s).+`   
Required: No

 ** [computeRoleArn](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-computeRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [description](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-description"></a>
 The description for the branch.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `(?s).*`   
Required: No

 ** [displayName](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-displayName"></a>
 The display name for a branch. This is used as the default domain prefix.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: No

 ** [enableAutoBuild](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enableAutoBuild"></a>
 Enables auto building for the branch.   
Type: Boolean  
Required: No

 ** [enableBasicAuth](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enableBasicAuth"></a>
 Enables basic authorization for the branch.   
Type: Boolean  
Required: No

 ** [enableNotification](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enableNotification"></a>
 Enables notifications for the branch.   
Type: Boolean  
Required: No

 ** [enablePerformanceMode](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enablePerformanceMode"></a>
Enables performance mode for the branch.  
Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.   
Type: Boolean  
Required: No

 ** [enablePullRequestPreview](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enablePullRequestPreview"></a>
 Enables pull request previews for this branch.   
Type: Boolean  
Required: No

 ** [enableSkewProtection](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-enableSkewProtection"></a>
Specifies whether the skew protection feature is enabled for the branch.  
Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see [Skew protection for Amplify deployments](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html) in the *Amplify User Guide*.  
Type: Boolean  
Required: No

 ** [environmentVariables](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-environmentVariables"></a>
 The environment variables for the branch.   
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 5500.  
Value Pattern: `(?s).*`   
Required: No

 ** [framework](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-framework"></a>
 The framework for the branch.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: No

 ** [pullRequestEnvironmentName](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-pullRequestEnvironmentName"></a>
 The Amplify environment name for the pull request.   
Type: String  
Length Constraints: Maximum length of 20.  
Pattern: `(?s).*`   
Required: No

 ** [stage](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-stage"></a>
 Describes the current stage for the branch.   
Type: String  
Valid Values: `PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST`   
Required: No

 ** [ttl](#API_UpdateBranch_RequestSyntax) **   <a name="amplify-UpdateBranch-request-ttl"></a>
 The content Time to Live (TTL) for the website in seconds.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 32.  
Pattern: `\d*`   
Required: No

## Response Syntax
<a name="API_UpdateBranch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "branch": { 
      "activeJobId": "string",
      "associatedResources": [ "string" ],
      "backend": { 
         "stackArn": "string"
      },
      "backendEnvironmentArn": "string",
      "basicAuthCredentials": "string",
      "branchArn": "string",
      "branchName": "string",
      "buildSpec": "string",
      "computeRoleArn": "string",
      "createTime": number,
      "customDomains": [ "string" ],
      "description": "string",
      "destinationBranch": "string",
      "displayName": "string",
      "enableAutoBuild": boolean,
      "enableBasicAuth": boolean,
      "enableNotification": boolean,
      "enablePerformanceMode": boolean,
      "enablePullRequestPreview": boolean,
      "enableSkewProtection": boolean,
      "environmentVariables": { 
         "string" : "string" 
      },
      "framework": "string",
      "pullRequestEnvironmentName": "string",
      "sourceBranch": "string",
      "stage": "string",
      "tags": { 
         "string" : "string" 
      },
      "thumbnailUrl": "string",
      "totalNumberOfJobs": "string",
      "ttl": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [branch](#API_UpdateBranch_ResponseSyntax) **   <a name="amplify-UpdateBranch-response-branch"></a>
 The branch for an Amplify app, which maps to a third-party repository branch.   
Type: [Branch](API_Branch.md) object

## Errors
<a name="API_UpdateBranch_Errors"></a>

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

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_UpdateBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/UpdateBranch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/UpdateBranch) 