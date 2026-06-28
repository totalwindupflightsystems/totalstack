---
id: "@specs/aws/storagegateway/docs/API_SoftwareUpdatePreferences"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SoftwareUpdatePreferences"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# SoftwareUpdatePreferences

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_SoftwareUpdatePreferences
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SoftwareUpdatePreferences
<a name="API_SoftwareUpdatePreferences"></a>

A set of variables indicating the software update preferences for the gateway.

## Contents
<a name="API_SoftwareUpdatePreferences_Contents"></a>

 ** AutomaticUpdatePolicy **   <a name="StorageGateway-Type-SoftwareUpdatePreferences-AutomaticUpdatePolicy"></a>
Indicates the automatic update policy for a gateway.  
 `ALL_VERSIONS` - Enables regular gateway maintenance updates.  
 `EMERGENCY_VERSIONS_ONLY` - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.  
Type: String  
Valid Values: `ALL_VERSIONS | EMERGENCY_VERSIONS_ONLY`   
Required: No

## See Also
<a name="API_SoftwareUpdatePreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SoftwareUpdatePreferences) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SoftwareUpdatePreferences) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SoftwareUpdatePreferences) 