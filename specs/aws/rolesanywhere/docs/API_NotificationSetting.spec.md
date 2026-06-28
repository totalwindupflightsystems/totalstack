---
id: "@specs/aws/rolesanywhere/docs/API_NotificationSetting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NotificationSetting"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# NotificationSetting

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_NotificationSetting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NotificationSetting
<a name="API_NotificationSetting"></a>

 Customizable notification settings that will be applied to notification events. IAM Roles Anywhere consumes these settings while notifying across multiple channels - CloudWatch metrics, EventBridge, and Health Dashboard. 

## Contents
<a name="API_NotificationSetting_Contents"></a>

 ** enabled **   <a name="rolesanywhere-Type-NotificationSetting-enabled"></a>
Indicates whether the notification setting is enabled.  
Type: Boolean  
Required: Yes

 ** event **   <a name="rolesanywhere-Type-NotificationSetting-event"></a>
The event to which this notification setting is applied.  
Type: String  
Valid Values: `CA_CERTIFICATE_EXPIRY | END_ENTITY_CERTIFICATE_EXPIRY`   
Required: Yes

 ** channel **   <a name="rolesanywhere-Type-NotificationSetting-channel"></a>
The specified channel of notification. IAM Roles Anywhere uses CloudWatch metrics, EventBridge, and Health Dashboard to notify for an event.  
In the absence of a specific channel, IAM Roles Anywhere applies this setting to 'ALL' channels.
Type: String  
Valid Values: `ALL`   
Required: No

 ** threshold **   <a name="rolesanywhere-Type-NotificationSetting-threshold"></a>
The number of days before a notification event. This value is required for a notification setting that is enabled.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 360.  
Required: No

## See Also
<a name="API_NotificationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/NotificationSetting) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/NotificationSetting) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/NotificationSetting) 