---
id: "@specs/aws/sesv2/docs/API_PutConfigurationSetSendingOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutConfigurationSetSendingOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutConfigurationSetSendingOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutConfigurationSetSendingOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutConfigurationSetSendingOptions
<a name="API_PutConfigurationSetSendingOptions"></a>

Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.

## Request Syntax
<a name="API_PutConfigurationSetSendingOptions_RequestSyntax"></a>

```
PUT /v2/email/configuration-sets/{{ConfigurationSetName}}/sending HTTP/1.1
Content-type: application/json

{
   "SendingEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetSendingOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetSendingOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSendingOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set to enable or disable email sending for.  
Required: Yes

## Request Body
<a name="API_PutConfigurationSetSendingOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SendingEnabled](#API_PutConfigurationSetSendingOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetSendingOptions-request-SendingEnabled"></a>
If `true`, email sending is enabled for the configuration set. If `false`, email sending is disabled for the configuration set.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_PutConfigurationSetSendingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetSendingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetSendingOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutConfigurationSetSendingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutConfigurationSetSendingOptions) 