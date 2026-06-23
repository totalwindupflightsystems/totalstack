---
id: "@specs/aws/amplify/docs/API_GenerateAccessLogs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GenerateAccessLogs"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# GenerateAccessLogs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_GenerateAccessLogs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GenerateAccessLogs
<a name="API_GenerateAccessLogs"></a>

Returns the website access logs for a specific time range using a presigned URL. 

## Request Syntax
<a name="API_GenerateAccessLogs_RequestSyntax"></a>

```
POST /apps/{{appId}}/accesslogs HTTP/1.1
Content-type: application/json

{
   "domainName": "{{string}}",
   "endTime": {{number}},
   "startTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GenerateAccessLogs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GenerateAccessLogs_RequestSyntax) **   <a name="amplify-GenerateAccessLogs-request-uri-appId"></a>
The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_GenerateAccessLogs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [domainName](#API_GenerateAccessLogs_RequestSyntax) **   <a name="amplify-GenerateAccessLogs-request-domainName"></a>
The name of the domain.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`   
Required: Yes

 ** [endTime](#API_GenerateAccessLogs_RequestSyntax) **   <a name="amplify-GenerateAccessLogs-request-endTime"></a>
The time at which the logs should end. The time range specified is inclusive of the end time.   
Type: Timestamp  
Required: No

 ** [startTime](#API_GenerateAccessLogs_RequestSyntax) **   <a name="amplify-GenerateAccessLogs-request-startTime"></a>
The time at which the logs should start. The time range specified is inclusive of the start time.   
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_GenerateAccessLogs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "logUrl": "string"
}
```

## Response Elements
<a name="API_GenerateAccessLogs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logUrl](#API_GenerateAccessLogs_ResponseSyntax) **   <a name="amplify-GenerateAccessLogs-response-logUrl"></a>
The pre-signed URL for the requested access logs.   
Type: String  
Length Constraints: Maximum length of 1000.

## Errors
<a name="API_GenerateAccessLogs_Errors"></a>

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
<a name="API_GenerateAccessLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/GenerateAccessLogs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/GenerateAccessLogs) 