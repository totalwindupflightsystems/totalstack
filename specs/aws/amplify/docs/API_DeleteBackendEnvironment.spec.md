---
id: "@specs/aws/amplify/docs/API_DeleteBackendEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteBackendEnvironment"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# DeleteBackendEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_DeleteBackendEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteBackendEnvironment
<a name="API_DeleteBackendEnvironment"></a>

Deletes a backend environment for an Amplify app. 

This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## Request Syntax
<a name="API_DeleteBackendEnvironment_RequestSyntax"></a>

```
DELETE /apps/{{appId}}/backendenvironments/{{environmentName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBackendEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_DeleteBackendEnvironment_RequestSyntax) **   <a name="amplify-DeleteBackendEnvironment-request-uri-appId"></a>
The unique ID of an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [environmentName](#API_DeleteBackendEnvironment_RequestSyntax) **   <a name="amplify-DeleteBackendEnvironment-request-uri-environmentName"></a>
The name of a backend environment of an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

## Request Body
<a name="API_DeleteBackendEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBackendEnvironment_ResponseSyntax"></a>

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
<a name="API_DeleteBackendEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [backendEnvironment](#API_DeleteBackendEnvironment_ResponseSyntax) **   <a name="amplify-DeleteBackendEnvironment-response-backendEnvironment"></a>
Describes the backend environment for an Amplify app.   
Type: [BackendEnvironment](API_BackendEnvironment.md) object

## Errors
<a name="API_DeleteBackendEnvironment_Errors"></a>

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
<a name="API_DeleteBackendEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/DeleteBackendEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/DeleteBackendEnvironment) 