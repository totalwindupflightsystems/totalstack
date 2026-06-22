---
id: "@specs/aws/acm/docs/API_PutAccountConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAccountConfiguration"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# PutAccountConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_PutAccountConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAccountConfiguration
<a name="API_PutAccountConfiguration"></a>

Adds or modifies account-level configurations in ACM. 

The supported configuration option is `DaysBeforeExpiry`. This option specifies the number of days prior to certificate expiration when ACM starts generating `EventBridge` events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.

## Request Syntax
<a name="API_PutAccountConfiguration_RequestSyntax"></a>

```
{
   "ExpiryEvents": { 
      "DaysBeforeExpiry": {{number}}
   },
   "IdempotencyToken": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAccountConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [IdempotencyToken](#API_PutAccountConfiguration_RequestSyntax) **   <a name="ACM-PutAccountConfiguration-request-IdempotencyToken"></a>
Customer-chosen string used to distinguish between calls to `PutAccountConfiguration`. Idempotency tokens time out after one hour. If you call `PutAccountConfiguration` multiple times with the same unexpired idempotency token, ACM treats it as the same request and returns the original result. If you change the idempotency token for each call, ACM treats each call as a new request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `\w+`   
Required: Yes

 ** [ExpiryEvents](#API_PutAccountConfiguration_RequestSyntax) **   <a name="ACM-PutAccountConfiguration-request-ExpiryEvents"></a>
Specifies expiration events associated with an account.  
Type: [ExpiryEventsConfiguration](API_ExpiryEventsConfiguration.md) object  
Required: No

## Response Elements
<a name="API_PutAccountConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have access required to perform this action.  
HTTP Status Code: 400

 ** ConflictException **   
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied because it exceeded a quota.    
 ** throttlingReasons **   
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## See Also
<a name="API_PutAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/PutAccountConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/PutAccountConfiguration) 