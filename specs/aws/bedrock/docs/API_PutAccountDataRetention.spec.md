---
id: "@specs/aws/bedrock/docs/API_PutAccountDataRetention"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAccountDataRetention"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PutAccountDataRetention

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_PutAccountDataRetention
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAccountDataRetention
<a name="API_PutAccountDataRetention"></a>

Sets the account-wide data retention mode for Amazon Bedrock.

## Request Syntax
<a name="API_PutAccountDataRetention_RequestSyntax"></a>

```
PUT /data-retention HTTP/1.1
Content-type: application/json

{
   "mode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAccountDataRetention_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountDataRetention_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [mode](#API_PutAccountDataRetention_RequestSyntax) **   <a name="bedrock-PutAccountDataRetention-request-mode"></a>
The data retention mode to set for the account.  
Type: String  
Valid Values: `default | none | provider_data_share | inherit`   
Required: Yes

## Response Syntax
<a name="API_PutAccountDataRetention_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mode": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_PutAccountDataRetention_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mode](#API_PutAccountDataRetention_ResponseSyntax) **   <a name="bedrock-PutAccountDataRetention-response-mode"></a>
The data retention mode set for the account.  
Type: String  
Valid Values: `default | none | provider_data_share | inherit` 

 ** [updatedAt](#API_PutAccountDataRetention_ResponseSyntax) **   <a name="bedrock-PutAccountDataRetention-response-updatedAt"></a>
The time at which the data retention mode was last updated.  
Type: Timestamp

## Errors
<a name="API_PutAccountDataRetention_Errors"></a>

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
<a name="API_PutAccountDataRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutAccountDataRetention) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutAccountDataRetention) 