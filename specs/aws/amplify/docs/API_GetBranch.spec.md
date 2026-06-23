---
id: "@specs/aws/amplify/docs/API_GetBranch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetBranch"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# GetBranch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_GetBranch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetBranch
<a name="API_GetBranch"></a>

 Returns a branch for an Amplify app. 

## Request Syntax
<a name="API_GetBranch_RequestSyntax"></a>

```
GET /apps/{{appId}}/branches/{{branchName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBranch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GetBranch_RequestSyntax) **   <a name="amplify-GetBranch-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_GetBranch_RequestSyntax) **   <a name="amplify-GetBranch-request-uri-branchName"></a>
The name of the branch.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

## Request Body
<a name="API_GetBranch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBranch_ResponseSyntax"></a>

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
<a name="API_GetBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [branch](#API_GetBranch_ResponseSyntax) **   <a name="amplify-GetBranch-response-branch"></a>
 The branch for an Amplify app, which maps to a third-party repository branch.   
Type: [Branch](API_Branch.md) object

## Errors
<a name="API_GetBranch_Errors"></a>

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
<a name="API_GetBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/GetBranch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/GetBranch) 