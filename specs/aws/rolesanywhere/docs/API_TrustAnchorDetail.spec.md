---
id: "@specs/aws/rolesanywhere/docs/API_TrustAnchorDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TrustAnchorDetail"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# TrustAnchorDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_TrustAnchorDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TrustAnchorDetail
<a name="API_TrustAnchorDetail"></a>

The state of the trust anchor after a read or write operation. 

## Contents
<a name="API_TrustAnchorDetail_Contents"></a>

 ** createdAt **   <a name="rolesanywhere-Type-TrustAnchorDetail-createdAt"></a>
The ISO-8601 timestamp when the trust anchor was created.   
Type: Timestamp  
Required: No

 ** enabled **   <a name="rolesanywhere-Type-TrustAnchorDetail-enabled"></a>
Indicates whether the trust anchor is enabled.  
Type: Boolean  
Required: No

 ** name **   <a name="rolesanywhere-Type-TrustAnchorDetail-name"></a>
The name of the trust anchor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: No

 ** notificationSettings **   <a name="rolesanywhere-Type-TrustAnchorDetail-notificationSettings"></a>
A list of notification settings to be associated to the trust anchor.  
Type: Array of [NotificationSettingDetail](API_NotificationSettingDetail.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** source **   <a name="rolesanywhere-Type-TrustAnchorDetail-source"></a>
The trust anchor type and its related certificate data.  
Type: [Source](API_Source.md) object  
Required: No

 ** trustAnchorArn **   <a name="rolesanywhere-Type-TrustAnchorDetail-trustAnchorArn"></a>
The ARN of the trust anchor.  
Type: String  
Required: No

 ** trustAnchorId **   <a name="rolesanywhere-Type-TrustAnchorDetail-trustAnchorId"></a>
The unique identifier of the trust anchor.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-TrustAnchorDetail-updatedAt"></a>
The ISO-8601 timestamp when the trust anchor was last updated.   
Type: Timestamp  
Required: No

## See Also
<a name="API_TrustAnchorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/TrustAnchorDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/TrustAnchorDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/TrustAnchorDetail) 