---
id: "@specs/aws/bedrock/docs/API_GetAccountDataRetention"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAccountDataRetention"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAccountDataRetention

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetAccountDataRetention
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAccountDataRetention
<a name="API_GetAccountDataRetention"></a>

Returns the account-wide data retention mode for Amazon Bedrock.

## Request Syntax
<a name="API_GetAccountDataRetention_RequestSyntax"></a>

```
GET /data-retention HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountDataRetention_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountDataRetention_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountDataRetention_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mode": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetAccountDataRetention_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mode](#API_GetAccountDataRetention_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetention-response-mode"></a>
The data retention mode configured for the account.  
Type: String  
Valid Values: `default | none | provider_data_share | inherit` 

 ** [updatedAt](#API_GetAccountDataRetention_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetention-response-updatedAt"></a>
The time at which the data retention mode was last updated.  
Type: Timestamp

## Errors
<a name="API_GetAccountDataRetention_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_GetAccountDataRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAccountDataRetention) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAccountDataRetention) 