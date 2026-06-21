---
id: "@specs/aws/shield/docs/API_Protection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Protection"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# Protection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_Protection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Protection
<a name="API_Protection"></a>

An object that represents a resource that is under DDoS protection.

## Contents
<a name="API_Protection_Contents"></a>

 ** ApplicationLayerAutomaticResponseConfiguration **   <a name="AWSShield-Type-Protection-ApplicationLayerAutomaticResponseConfiguration"></a>
The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.   
Type: [ApplicationLayerAutomaticResponseConfiguration](API_ApplicationLayerAutomaticResponseConfiguration.md) object  
Required: No

 ** HealthCheckIds **   <a name="AWSShield-Type-Protection-HealthCheckIds"></a>
The unique identifier (ID) for the Route 53 health check that's associated with the protection.   
Type: Array of strings  
Required: No

 ** Id **   <a name="AWSShield-Type-Protection-Id"></a>
The unique identifier (ID) of the protection.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: No

 ** Name **   <a name="AWSShield-Type-Protection-Name"></a>
The name of the protection. For example, `My CloudFront distributions`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[ a-zA-Z0-9_\\.\\-]*`   
Required: No

 ** ProtectionArn **   <a name="AWSShield-Type-Protection-ProtectionArn"></a>
The ARN (Amazon Resource Name) of the protection.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** ResourceArn **   <a name="AWSShield-Type-Protection-ResourceArn"></a>
The ARN (Amazon Resource Name) of the AWS resource that is protected.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

## See Also
<a name="API_Protection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/Protection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/Protection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/Protection) 