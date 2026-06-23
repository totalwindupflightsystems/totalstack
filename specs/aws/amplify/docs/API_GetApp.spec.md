---
id: "@specs/aws/amplify/docs/API_GetApp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetApp"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# GetApp

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_GetApp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetApp
<a name="API_GetApp"></a>

Returns an existing Amplify app specified by an app ID.

## Request Syntax
<a name="API_GetApp_RequestSyntax"></a>

```
GET /apps/{{appId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GetApp_RequestSyntax) **   <a name="amplify-GetApp-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_GetApp_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApp_ResponseSyntax"></a>

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
<a name="API_GetApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [app](#API_GetApp_ResponseSyntax) **   <a name="amplify-GetApp-response-app"></a>
Represents the different branches of a repository for building, deploying, and hosting an Amplify app.   
Type: [App](API_App.md) object

## Errors
<a name="API_GetApp_Errors"></a>

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
<a name="API_GetApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/GetApp) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/GetApp) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/GetApp) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/GetApp) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/GetApp) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/GetApp) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/GetApp) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/GetApp) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/GetApp) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/GetApp) 