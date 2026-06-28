---
id: "@specs/aws/kendra/docs/API_ExperienceEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExperienceEndpoint"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ExperienceEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ExperienceEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExperienceEndpoint
<a name="API_ExperienceEndpoint"></a>

Provides the configuration information for the endpoint for your Amazon Kendra experience.

## Contents
<a name="API_ExperienceEndpoint_Contents"></a>

 ** Endpoint **   <a name="kendra-Type-ExperienceEndpoint-Endpoint"></a>
The endpoint of your Amazon Kendra experience.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*$`   
Required: No

 ** EndpointType **   <a name="kendra-Type-ExperienceEndpoint-EndpointType"></a>
The type of endpoint for your Amazon Kendra experience. The type currently available is `HOME`, which is a unique and fully hosted URL to the home page of your Amazon Kendra experience.  
Type: String  
Valid Values: `HOME`   
Required: No

## See Also
<a name="API_ExperienceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ExperienceEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ExperienceEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ExperienceEndpoint) 