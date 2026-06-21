---
id: "@specs/aws/shield/docs/API_GetSubscriptionState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSubscriptionState"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# GetSubscriptionState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_GetSubscriptionState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSubscriptionState
<a name="API_GetSubscriptionState"></a>

Returns the `SubscriptionState`, either `Active` or `Inactive`.

## Response Syntax
<a name="API_GetSubscriptionState_ResponseSyntax"></a>

```
{
   "SubscriptionState": "string"
}
```

## Response Elements
<a name="API_GetSubscriptionState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubscriptionState](#API_GetSubscriptionState_ResponseSyntax) **   <a name="AWSShield-GetSubscriptionState-response-SubscriptionState"></a>
The status of the subscription.  
Type: String  
Valid Values: `ACTIVE | INACTIVE` 

## Errors
<a name="API_GetSubscriptionState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

## See Also
<a name="API_GetSubscriptionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/GetSubscriptionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/GetSubscriptionState) 