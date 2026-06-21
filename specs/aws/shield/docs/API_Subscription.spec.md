---
id: "@specs/aws/shield/docs/API_Subscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Subscription"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# Subscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_Subscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Subscription
<a name="API_Subscription"></a>

Information about the AWS Shield Advanced subscription for an account.

## Contents
<a name="API_Subscription_Contents"></a>

 ** SubscriptionLimits **   <a name="AWSShield-Type-Subscription-SubscriptionLimits"></a>
Limits settings for your subscription.   
Type: [SubscriptionLimits](API_SubscriptionLimits.md) object  
Required: Yes

 ** AutoRenew **   <a name="AWSShield-Type-Subscription-AutoRenew"></a>
If `ENABLED`, the subscription will be automatically renewed at the end of the existing subscription period.  
When you initally create a subscription, `AutoRenew` is set to `ENABLED`. You can change this by submitting an `UpdateSubscription` request. If the `UpdateSubscription` request does not included a value for `AutoRenew`, the existing value for `AutoRenew` remains unchanged.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** EndTime **   <a name="AWSShield-Type-Subscription-EndTime"></a>
The date and time your subscription will end.  
Type: Timestamp  
Required: No

 ** Limits **   <a name="AWSShield-Type-Subscription-Limits"></a>
Specifies how many protections of a given type you can create.  
Type: Array of [Limit](API_Limit.md) objects  
Required: No

 ** ProactiveEngagementStatus **   <a name="AWSShield-Type-Subscription-ProactiveEngagementStatus"></a>
If `ENABLED`, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.  
If `PENDING`, you have requested proactive engagement and the request is pending. The status changes to `ENABLED` when your request is fully processed.  
If `DISABLED`, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.   
Type: String  
Valid Values: `ENABLED | DISABLED | PENDING`   
Required: No

 ** StartTime **   <a name="AWSShield-Type-Subscription-StartTime"></a>
The start time of the subscription, in Unix time in seconds.   
Type: Timestamp  
Required: No

 ** SubscriptionArn **   <a name="AWSShield-Type-Subscription-SubscriptionArn"></a>
The ARN (Amazon Resource Name) of the subscription.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** TimeCommitmentInSeconds **   <a name="AWSShield-Type-Subscription-TimeCommitmentInSeconds"></a>
The length, in seconds, of the AWS Shield Advanced subscription for the account.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/Subscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/Subscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/Subscription) 