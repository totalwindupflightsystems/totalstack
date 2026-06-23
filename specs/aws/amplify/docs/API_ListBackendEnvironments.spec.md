---
id: "@specs/aws/amplify/docs/API_ListBackendEnvironments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListBackendEnvironments"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListBackendEnvironments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListBackendEnvironments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListBackendEnvironments
<a name="API_ListBackendEnvironments"></a>

Lists the backend environments for an Amplify app. 

This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## Request Syntax
<a name="API_ListBackendEnvironments_RequestSyntax"></a>

```
GET /apps/{{appId}}/backendenvironments?environmentName={{environmentName}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBackendEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListBackendEnvironments_RequestSyntax) **   <a name="amplify-ListBackendEnvironments-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [environmentName](#API_ListBackendEnvironments_RequestSyntax) **   <a name="amplify-ListBackendEnvironments-request-uri-environmentName"></a>
The name of the backend environment   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+` 

 ** [maxResults](#API_ListBackendEnvironments_RequestSyntax) **   <a name="amplify-ListBackendEnvironments-request-uri-maxResults"></a>
The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListBackendEnvironments_RequestSyntax) **   <a name="amplify-ListBackendEnvironments-request-uri-nextToken"></a>
A pagination token. Set to null to start listing backend environments from the start. If a non-null pagination token is returned in a result, pass its value in here to list more backend environments.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListBackendEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBackendEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "backendEnvironments": [ 
      { 
         "backendEnvironmentArn": "string",
         "createTime": number,
         "deploymentArtifacts": "string",
         "environmentName": "string",
         "stackName": "string",
         "updateTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBackendEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [backendEnvironments](#API_ListBackendEnvironments_ResponseSyntax) **   <a name="amplify-ListBackendEnvironments-response-backendEnvironments"></a>
The list of backend environments for an Amplify app.   
Type: Array of [BackendEnvironment](API_BackendEnvironment.md) objects

 ** [nextToken](#API_ListBackendEnvironments_ResponseSyntax) **   <a name="amplify-ListBackendEnvironments-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListBackendEnvironments_Errors"></a>

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
<a name="API_ListBackendEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListBackendEnvironments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListBackendEnvironments) 