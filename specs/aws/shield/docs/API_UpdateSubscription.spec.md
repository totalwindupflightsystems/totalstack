---
id: "@specs/aws/shield/docs/API_UpdateSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSubscription"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# UpdateSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_UpdateSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSubscription
<a name="API_UpdateSubscription"></a>

Updates the details of an existing subscription. Only enter values for parameters you want to change. Empty parameters are not updated.

**Note**  
For accounts that are members of an AWS Organizations organization, Shield Advanced subscriptions are billed against the organization's payer account, regardless of whether the payer account itself is subscribed. 

## Request Syntax
<a name="API_UpdateSubscription_RequestSyntax"></a>

```
{
   "AutoRenew": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoRenew](#API_UpdateSubscription_RequestSyntax) **   <a name="AWSShield-UpdateSubscription-request-AutoRenew"></a>
When you initally create a subscription, `AutoRenew` is set to `ENABLED`. If `ENABLED`, the subscription will be automatically renewed at the end of the existing subscription period. You can change this by submitting an `UpdateSubscription` request. If the `UpdateSubscription` request does not included a value for `AutoRenew`, the existing value for `AutoRenew` remains unchanged.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Elements
<a name="API_UpdateSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** LockedSubscriptionException **   
You are trying to update a subscription that has not yet completed the 1-year commitment. You can change the `AutoRenew` parameter during the last 30 days of your subscription. This exception indicates that you are attempting to change `AutoRenew` prior to that period.  
HTTP Status Code: 400

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/UpdateSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/UpdateSubscription) 