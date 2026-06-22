---
id: "@specs/aws/mwaa/docs/API_DeleteEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEnvironment"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# DeleteEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_DeleteEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEnvironment
<a name="API_DeleteEnvironment"></a>

Deletes an Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment.

## Request Syntax
<a name="API_DeleteEnvironment_RequestSyntax"></a>

```
DELETE /environments/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DeleteEnvironment_RequestSyntax) **   <a name="mwaa-DeleteEnvironment-request-uri-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_DeleteEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
ResourceNotFoundException: The resource is not available.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
ServiceUnavailableException: The service is currently unavailable.  
HTTP Status Code: 503

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/DeleteEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/DeleteEnvironment) 