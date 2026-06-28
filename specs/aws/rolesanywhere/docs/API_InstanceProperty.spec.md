---
id: "@specs/aws/rolesanywhere/docs/API_InstanceProperty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceProperty"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# InstanceProperty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_InstanceProperty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceProperty
<a name="API_InstanceProperty"></a>

A key-value pair you set that identifies a property of the authenticating instance.

## Contents
<a name="API_InstanceProperty_Contents"></a>

 ** failed **   <a name="rolesanywhere-Type-InstanceProperty-failed"></a>
Indicates whether the temporary credential request was successful.   
Type: Boolean  
Required: No

 ** properties **   <a name="rolesanywhere-Type-InstanceProperty-properties"></a>
A list of instanceProperty objects.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 200.  
Value Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** seenAt **   <a name="rolesanywhere-Type-InstanceProperty-seenAt"></a>
The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InstanceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/InstanceProperty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/InstanceProperty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/InstanceProperty) 