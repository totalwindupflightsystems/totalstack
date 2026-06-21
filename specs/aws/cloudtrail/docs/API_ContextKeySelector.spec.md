---
id: "@specs/aws/cloudtrail/docs/API_ContextKeySelector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContextKeySelector"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ContextKeySelector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ContextKeySelector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContextKeySelector
<a name="API_ContextKeySelector"></a>

An object that contains information types to be included in CloudTrail enriched events.

## Contents
<a name="API_ContextKeySelector_Contents"></a>

 ** Equals **   <a name="awscloudtrail-Type-ContextKeySelector-Equals"></a>
A list of keys defined by Type to be included in CloudTrail enriched events.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** Type **   <a name="awscloudtrail-Type-ContextKeySelector-Type"></a>
Specifies the type of the event record field in ContextKeySelector. Valid values include RequestContext, TagContext.  
Type: String  
Valid Values: `TagContext | RequestContext`   
Required: Yes

## See Also
<a name="API_ContextKeySelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ContextKeySelector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ContextKeySelector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ContextKeySelector) 