---
id: "@specs/aws/shield/docs/API_ApplicationLayerAutomaticResponseConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApplicationLayerAutomaticResponseConfiguration"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ApplicationLayerAutomaticResponseConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ApplicationLayerAutomaticResponseConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApplicationLayerAutomaticResponseConfiguration
<a name="API_ApplicationLayerAutomaticResponseConfiguration"></a>

The automatic application layer DDoS mitigation settings for a [Protection](API_Protection.md). This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks. 

## Contents
<a name="API_ApplicationLayerAutomaticResponseConfiguration_Contents"></a>

 ** Action **   <a name="AWSShield-Type-ApplicationLayerAutomaticResponseConfiguration-Action"></a>
Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.   
Type: [ResponseAction](API_ResponseAction.md) object  
Required: Yes

 ** Status **   <a name="AWSShield-Type-ApplicationLayerAutomaticResponseConfiguration-Status"></a>
Indicates whether automatic application layer DDoS mitigation is enabled for the protection.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

## See Also
<a name="API_ApplicationLayerAutomaticResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration) 