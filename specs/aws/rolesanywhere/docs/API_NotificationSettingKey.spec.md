---
id: "@specs/aws/rolesanywhere/docs/API_NotificationSettingKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NotificationSettingKey"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# NotificationSettingKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_NotificationSettingKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NotificationSettingKey
<a name="API_NotificationSettingKey"></a>

A notification setting key to reset. A notification setting key includes the event and the channel. 

## Contents
<a name="API_NotificationSettingKey_Contents"></a>

 ** event **   <a name="rolesanywhere-Type-NotificationSettingKey-event"></a>
The notification setting event to reset.  
Type: String  
Valid Values: `CA_CERTIFICATE_EXPIRY | END_ENTITY_CERTIFICATE_EXPIRY`   
Required: Yes

 ** channel **   <a name="rolesanywhere-Type-NotificationSettingKey-channel"></a>
The specified channel of notification.  
Type: String  
Valid Values: `ALL`   
Required: No

## See Also
<a name="API_NotificationSettingKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/NotificationSettingKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/NotificationSettingKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/NotificationSettingKey) 