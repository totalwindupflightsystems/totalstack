---
id: "@specs/aws/mwaa/docs/API_InvokeRestApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InvokeRestApi"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# InvokeRestApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_InvokeRestApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InvokeRestApi
<a name="API_InvokeRestApi"></a>

Invokes the Apache Airflow REST API on the webserver with the specified inputs. To learn more, see [Using the Apache Airflow REST API](https://docs.aws.amazon.com/mwaa/latest/userguide/access-mwaa-apache-airflow-rest-api.html) 

## Request Syntax
<a name="API_InvokeRestApi_RequestSyntax"></a>

```
POST /restapi/{{Name}} HTTP/1.1
Content-type: application/json

{
   "Body": {{JSON value}},
   "Method": "{{string}}",
   "Path": "{{string}}",
   "QueryParameters": {{JSON value}}
}
```

## URI Request Parameters
<a name="API_InvokeRestApi_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_InvokeRestApi_RequestSyntax) **   <a name="mwaa-InvokeRestApi-request-uri-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_InvokeRestApi_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Body](#API_InvokeRestApi_RequestSyntax) **   <a name="mwaa-InvokeRestApi-request-Body"></a>
The request body for the Apache Airflow REST API call, provided as a JSON object.  
Type: JSON value  
Required: No

 ** [Method](#API_InvokeRestApi_RequestSyntax) **   <a name="mwaa-InvokeRestApi-request-Method"></a>
The HTTP method used for making Airflow REST API calls. For example, `POST`.   
Type: String  
Valid Values: `GET | PUT | POST | PATCH | DELETE`   
Required: Yes

 ** [Path](#API_InvokeRestApi_RequestSyntax) **   <a name="mwaa-InvokeRestApi-request-Path"></a>
The Apache Airflow REST API endpoint path to be called. For example, `/dags/123456/clearTaskInstances`. For more information, see [Apache Airflow API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [QueryParameters](#API_InvokeRestApi_RequestSyntax) **   <a name="mwaa-InvokeRestApi-request-QueryParameters"></a>
Query parameters to be included in the Apache Airflow REST API call, provided as a JSON object.   
Type: JSON value  
Required: No

## Response Syntax
<a name="API_InvokeRestApi_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RestApiResponse": JSON value,
   "RestApiStatusCode": number
}
```

## Response Elements
<a name="API_InvokeRestApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RestApiResponse](#API_InvokeRestApi_ResponseSyntax) **   <a name="mwaa-InvokeRestApi-response-RestApiResponse"></a>
The response data from the Apache Airflow REST API call, provided as a JSON object.  
Type: JSON value

 ** [RestApiStatusCode](#API_InvokeRestApi_ResponseSyntax) **   <a name="mwaa-InvokeRestApi-response-RestApiStatusCode"></a>
The HTTP status code returned by the Apache Airflow REST API call.  
Type: Integer

## Errors
<a name="API_InvokeRestApi_Errors"></a>

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

 ** RestApiClientException **   
An exception indicating that a client-side error occurred during the Apache Airflow REST API call.    
 ** RestApiResponse **   
The error response data from the Apache Airflow REST API call, provided as a JSON object.  
 ** RestApiStatusCode **   
The HTTP status code returned by the Apache Airflow REST API call.
HTTP Status Code: 400

 ** RestApiServerException **   
An exception indicating that a server-side error occurred during the Apache Airflow REST API call.    
 ** RestApiResponse **   
The error response data from the Apache Airflow REST API call, provided as a JSON object.  
 ** RestApiStatusCode **   
The HTTP status code returned by the Apache Airflow REST API call.
HTTP Status Code: 400

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## Examples
<a name="API_InvokeRestApi_Examples"></a>

### Example
<a name="API_InvokeRestApi_Example_1"></a>

This example illustrates one usage of InvokeRestApi.

#### Sample Request
<a name="API_InvokeRestApi_Example_1_Request"></a>

```
{
      "name": "MyEnvironment",
      "path": "/dags",
      "method": "GET"
}
```

### Example
<a name="API_InvokeRestApi_Example_2"></a>

This example illustrates one usage of InvokeRestApi.

#### Sample Response
<a name="API_InvokeRestApi_Example_2_Response"></a>

```
{
      "restApiResponse": {"dags":[],"total_entries":0},
      "restApiStatusCode": 200,
}
```

## See Also
<a name="API_InvokeRestApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/InvokeRestApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/InvokeRestApi) 