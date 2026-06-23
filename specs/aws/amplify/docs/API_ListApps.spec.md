---
id: "@specs/aws/amplify/docs/API_ListApps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListApps"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListApps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListApps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListApps
<a name="API_ListApps"></a>

Returns a list of the existing Amplify apps. 

## Request Syntax
<a name="API_ListApps_RequestSyntax"></a>

```
GET /apps?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApps_RequestSyntax) **   <a name="amplify-ListApps-request-uri-maxResults"></a>
The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [nextToken](#API_ListApps_RequestSyntax) **   <a name="amplify-ListApps-request-uri-nextToken"></a>
A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListApps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apps": [ 
      { 
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apps](#API_ListApps_ResponseSyntax) **   <a name="amplify-ListApps-response-apps"></a>
A list of Amplify apps.   
Type: Array of [App](API_App.md) objects

 ** [nextToken](#API_ListApps_ResponseSyntax) **   <a name="amplify-ListApps-response-nextToken"></a>
A pagination token. Set to null to start listing apps from start. If non-null, the pagination token is returned in a result. Pass its value in here to list more projects.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_ListApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListApps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListApps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListApps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListApps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListApps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListApps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListApps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListApps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListApps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListApps) 