---
id: "@specs/aws/amplify/docs/API_ListBranches"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListBranches"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListBranches

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListBranches
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListBranches
<a name="API_ListBranches"></a>

 Lists the branches of an Amplify app. 

## Request Syntax
<a name="API_ListBranches_RequestSyntax"></a>

```
GET /apps/{{appId}}/branches?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBranches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListBranches_RequestSyntax) **   <a name="amplify-ListBranches-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [maxResults](#API_ListBranches_RequestSyntax) **   <a name="amplify-ListBranches-request-uri-maxResults"></a>
 The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListBranches_RequestSyntax) **   <a name="amplify-ListBranches-request-uri-nextToken"></a>
A pagination token. Set to null to start listing branches from the start. If a non-null pagination token is returned in a result, pass its value in here to list more branches.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListBranches_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBranches_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "branches": [ 
      { 
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBranches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [branches](#API_ListBranches_ResponseSyntax) **   <a name="amplify-ListBranches-response-branches"></a>
 A list of branches for an Amplify app.   
Type: Array of [Branch](API_Branch.md) objects  
Array Members: Maximum number of 255 items.

 ** [nextToken](#API_ListBranches_ResponseSyntax) **   <a name="amplify-ListBranches-response-nextToken"></a>
 A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListBranches_Errors"></a>

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
<a name="API_ListBranches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListBranches) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListBranches) 