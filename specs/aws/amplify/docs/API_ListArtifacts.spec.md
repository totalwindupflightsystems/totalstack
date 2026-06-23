---
id: "@specs/aws/amplify/docs/API_ListArtifacts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListArtifacts"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListArtifacts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListArtifacts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListArtifacts
<a name="API_ListArtifacts"></a>

Returns a list of end-to-end testing artifacts for a specified app, branch, and job.

To return the build artifacts, use the [GetJob](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetJob.html) API.

For more information about Amplify testing support, see [Setting up end-to-end Cypress tests for your Amplify application](https://docs.aws.amazon.com/amplify/latest/userguide/running-tests.html) in the *Amplify Hosting User Guide*. 

## Request Syntax
<a name="API_ListArtifacts_RequestSyntax"></a>

```
GET /apps/{{appId}}/branches/{{branchName}}/jobs/{{jobId}}/artifacts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListArtifacts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListArtifacts_RequestSyntax) **   <a name="amplify-ListArtifacts-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_ListArtifacts_RequestSyntax) **   <a name="amplify-ListArtifacts-request-uri-branchName"></a>
The name of a branch that is part of an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [jobId](#API_ListArtifacts_RequestSyntax) **   <a name="amplify-ListArtifacts-request-uri-jobId"></a>
The unique ID for a job.   
Length Constraints: Maximum length of 255.  
Pattern: `[0-9]+`   
Required: Yes

 ** [maxResults](#API_ListArtifacts_RequestSyntax) **   <a name="amplify-ListArtifacts-request-uri-maxResults"></a>
The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListArtifacts_RequestSyntax) **   <a name="amplify-ListArtifacts-request-uri-nextToken"></a>
A pagination token. Set to null to start listing artifacts from start. If a non-null pagination token is returned in a result, pass its value in here to list more artifacts.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListArtifacts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListArtifacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "artifacts": [ 
      { 
         "artifactFileName": "string",
         "artifactId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifacts](#API_ListArtifacts_ResponseSyntax) **   <a name="amplify-ListArtifacts-response-artifacts"></a>
A list of artifacts.   
Type: Array of [Artifact](API_Artifact.md) objects

 ** [nextToken](#API_ListArtifacts_ResponseSyntax) **   <a name="amplify-ListArtifacts-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListArtifacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

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
<a name="API_ListArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListArtifacts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListArtifacts) 