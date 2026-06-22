---
id: "@specs/aws/codepipeline/docs/API_ActionTypeProperty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeProperty"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeProperty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeProperty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeProperty
<a name="API_ActionTypeProperty"></a>

Represents information about each property specified in the action configuration, such as the description and key name that display for the customer using the action type.

## Contents
<a name="API_ActionTypeProperty_Contents"></a>

 ** key **   <a name="CodePipeline-Type-ActionTypeProperty-key"></a>
Whether the configuration property is a key.  
Type: Boolean  
Required: Yes

 ** name **   <a name="CodePipeline-Type-ActionTypeProperty-name"></a>
The property name that is displayed to users.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** noEcho **   <a name="CodePipeline-Type-ActionTypeProperty-noEcho"></a>
Whether to omit the field value entered by the customer in the log. If `true`, the value is not saved in CloudTrail logs for the action execution.  
Type: Boolean  
Required: Yes

 ** optional **   <a name="CodePipeline-Type-ActionTypeProperty-optional"></a>
Whether the configuration property is an optional value.  
Type: Boolean  
Required: Yes

 ** description **   <a name="CodePipeline-Type-ActionTypeProperty-description"></a>
The description of the property that is displayed to users.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 250.  
Required: No

 ** queryable **   <a name="CodePipeline-Type-ActionTypeProperty-queryable"></a>
Indicates that the property is used with polling. An action type can have up to one queryable property. If it has one, that property must be both required and not secret.  
Type: Boolean  
Required: No

## See Also
<a name="API_ActionTypeProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeProperty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeProperty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeProperty) 