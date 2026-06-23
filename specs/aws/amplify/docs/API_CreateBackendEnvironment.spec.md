---
id: "@specs/aws/amplify/docs/API_CreateBackendEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateBackendEnvironment"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CreateBackendEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CreateBackendEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateBackendEnvironment
<a name="API_CreateBackendEnvironment"></a>

Creates a new backend environment for an Amplify app. 

This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## Request Syntax
<a name="API_CreateBackendEnvironment_RequestSyntax"></a>

```
POST /apps/{{appId}}/backendenvironments HTTP/1.1
Content-type: application/json

{
   "deploymentArtifacts": "{{string}}",
   "environmentName": "{{string}}",
   "stackName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBackendEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateBackendEnvironment_RequestSyntax) **   <a name="amplify-CreateBackendEnvironment-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_CreateBackendEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentArtifacts](#API_CreateBackendEnvironment_RequestSyntax) **   <a name="amplify-CreateBackendEnvironment-request-deploymentArtifacts"></a>
The name of deployment artifacts.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `(?s).+`   
Required: No

 ** [environmentName](#API_CreateBackendEnvironment_RequestSyntax) **   <a name="amplify-CreateBackendEnvironment-request-environmentName"></a>
The name for the backend environment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [stackName](#API_CreateBackendEnvironment_RequestSyntax) **   <a name="amplify-CreateBackendEnvironment-request-stackName"></a>
The AWS CloudFormation stack name of a backend environment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

## Response Syntax
<a name="API_CreateBackendEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "backendEnvironment": { 
      "backendEnvironmentArn": "string",
      "createTime": number,
      "deploymentArtifacts": "string",
      "environmentName": "string",
      "stackName": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateBackendEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [backendEnvironment](#API_CreateBackendEnvironment_ResponseSyntax) **   <a name="amplify-CreateBackendEnvironment-response-backendEnvironment"></a>
Describes the backend environment for an Amplify app.   
Type: [BackendEnvironment](API_BackendEnvironment.md) object

## Errors
<a name="API_CreateBackendEnvironment_Errors"></a>

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

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_CreateBackendEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/CreateBackendEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CreateBackendEnvironment) 