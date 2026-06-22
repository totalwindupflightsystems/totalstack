---
id: "@specs/aws/codepipeline/docs/API_ActionConfigurationProperty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionConfigurationProperty"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionConfigurationProperty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionConfigurationProperty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionConfigurationProperty
<a name="API_ActionConfigurationProperty"></a>

Represents information about an action configuration property.

## Contents
<a name="API_ActionConfigurationProperty_Contents"></a>

 ** key **   <a name="CodePipeline-Type-ActionConfigurationProperty-key"></a>
Whether the configuration property is a key.  
Type: Boolean  
Required: Yes

 ** name **   <a name="CodePipeline-Type-ActionConfigurationProperty-name"></a>
The name of the action configuration property.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** required **   <a name="CodePipeline-Type-ActionConfigurationProperty-required"></a>
Whether the configuration property is a required value.  
Type: Boolean  
Required: Yes

 ** secret **   <a name="CodePipeline-Type-ActionConfigurationProperty-secret"></a>
Whether the configuration property is secret. Secrets are hidden from all calls except for `GetJobDetails`, `GetThirdPartyJobDetails`, `PollForJobs`, and `PollForThirdPartyJobs`.  
When updating a pipeline, passing \* \* \* \* \* without changing any other values of the action preserves the previous value of the secret.  
Type: Boolean  
Required: Yes

 ** description **   <a name="CodePipeline-Type-ActionConfigurationProperty-description"></a>
The description of the action configuration property that is displayed to users.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 160.  
Required: No

 ** queryable **   <a name="CodePipeline-Type-ActionConfigurationProperty-queryable"></a>
Indicates that the property is used with `PollForJobs`. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.  
If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.  
Type: Boolean  
Required: No

 ** type **   <a name="CodePipeline-Type-ActionConfigurationProperty-type"></a>
The type of the configuration property.  
Type: String  
Valid Values: `String | Number | Boolean`   
Required: No

## See Also
<a name="API_ActionConfigurationProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionConfigurationProperty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionConfigurationProperty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionConfigurationProperty) 