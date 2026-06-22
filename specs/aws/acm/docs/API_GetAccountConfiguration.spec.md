---
id: "@specs/aws/acm/docs/API_GetAccountConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAccountConfiguration"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# GetAccountConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_GetAccountConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAccountConfiguration
<a name="API_GetAccountConfiguration"></a>

Returns the account configuration options associated with an AWS account.

## Response Syntax
<a name="API_GetAccountConfiguration_ResponseSyntax"></a>

```
{
   "ExpiryEvents": { 
      "DaysBeforeExpiry": number
   }
}
```

## Response Elements
<a name="API_GetAccountConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExpiryEvents](#API_GetAccountConfiguration_ResponseSyntax) **   <a name="ACM-GetAccountConfiguration-response-ExpiryEvents"></a>
Expiration events configuration options associated with the AWS account.  
Type: [ExpiryEventsConfiguration](API_ExpiryEventsConfiguration.md) object

## Errors
<a name="API_GetAccountConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have access required to perform this action.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied because it exceeded a quota.    
 ** throttlingReasons **   
One or more reasons why the request was throttled.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/GetAccountConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/GetAccountConfiguration) 