---
id: "@specs/aws/mwaa/docs/API_CreateCliToken"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCliToken"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# CreateCliToken

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_CreateCliToken
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCliToken
<a name="API_CreateCliToken"></a>

Creates a CLI token for the Airflow CLI. To learn more, see [Creating an Apache Airflow CLI token](https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html).

## Request Syntax
<a name="API_CreateCliToken_RequestSyntax"></a>

```
POST /clitoken/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateCliToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreateCliToken_RequestSyntax) **   <a name="mwaa-CreateCliToken-request-uri-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_CreateCliToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateCliToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CliToken": "string",
   "WebServerHostname": "string"
}
```

## Response Elements
<a name="API_CreateCliToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CliToken](#API_CreateCliToken_ResponseSyntax) **   <a name="mwaa-CreateCliToken-response-CliToken"></a>
An Airflow CLI login token.  
Type: String

 ** [WebServerHostname](#API_CreateCliToken_ResponseSyntax) **   <a name="mwaa-CreateCliToken-response-WebServerHostname"></a>
The Airflow web server hostname for the environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])` 

## Errors
<a name="API_CreateCliToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **   
ResourceNotFoundException: The resource is not available.  
HTTP Status Code: 404

## See Also
<a name="API_CreateCliToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/CreateCliToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/CreateCliToken) 