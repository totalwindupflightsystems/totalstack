---
id: "@specs/aws/mwaa/docs/API_CreateWebLoginToken"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateWebLoginToken"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# CreateWebLoginToken

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_CreateWebLoginToken
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateWebLoginToken
<a name="API_CreateWebLoginToken"></a>

Creates a web login token for the Airflow Web UI. To learn more, see [Creating an Apache Airflow web login token](https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html).

## Request Syntax
<a name="API_CreateWebLoginToken_RequestSyntax"></a>

```
POST /webtoken/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateWebLoginToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreateWebLoginToken_RequestSyntax) **   <a name="mwaa-CreateWebLoginToken-request-uri-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_CreateWebLoginToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateWebLoginToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AirflowIdentity": "string",
   "IamIdentity": "string",
   "WebServerHostname": "string",
   "WebToken": "string"
}
```

## Response Elements
<a name="API_CreateWebLoginToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AirflowIdentity](#API_CreateWebLoginToken_ResponseSyntax) **   <a name="mwaa-CreateWebLoginToken-response-AirflowIdentity"></a>
The user name of the Apache Airflow identity creating the web login token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [IamIdentity](#API_CreateWebLoginToken_ResponseSyntax) **   <a name="mwaa-CreateWebLoginToken-response-IamIdentity"></a>
The name of the IAM identity creating the web login token. This might be an IAM user, or an assumed or federated identity. For example, `assumed-role/Admin/your-name`.  
Type: String

 ** [WebServerHostname](#API_CreateWebLoginToken_ResponseSyntax) **   <a name="mwaa-CreateWebLoginToken-response-WebServerHostname"></a>
The Airflow web server hostname for the environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])` 

 ** [WebToken](#API_CreateWebLoginToken_ResponseSyntax) **   <a name="mwaa-CreateWebLoginToken-response-WebToken"></a>
An Airflow web server login token.  
Type: String

## Errors
<a name="API_CreateWebLoginToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
Access to the Apache Airflow Web UI or CLI has been denied due to insufficient permissions. To learn more, see [Accessing an Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html).  
HTTP Status Code: 403

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
ResourceNotFoundException: The resource is not available.  
HTTP Status Code: 404

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_CreateWebLoginToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/CreateWebLoginToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/CreateWebLoginToken) 