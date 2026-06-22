---
id: "@specs/aws/codepipeline/docs/API_EnvironmentVariable"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnvironmentVariable"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# EnvironmentVariable

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_EnvironmentVariable
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnvironmentVariable
<a name="API_EnvironmentVariable"></a>

The environment variables for the action.

## Contents
<a name="API_EnvironmentVariable_Contents"></a>

 ** name **   <a name="CodePipeline-Type-EnvironmentVariable-name"></a>
The environment variable name in the key-value pair.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]+`   
Required: Yes

 ** value **   <a name="CodePipeline-Type-EnvironmentVariable-value"></a>
The environment variable value in the key-value pair.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `.*`   
Required: Yes

 ** type **   <a name="CodePipeline-Type-EnvironmentVariable-type"></a>
Specifies the type of use for the environment variable value. The value can be either `PLAINTEXT` or `SECRETS_MANAGER`. If the value is `SECRETS_MANAGER`, provide the Secrets reference in the EnvironmentVariable value.  
Type: String  
Valid Values: `PLAINTEXT | SECRETS_MANAGER`   
Required: No

## See Also
<a name="API_EnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/EnvironmentVariable) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/EnvironmentVariable) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/EnvironmentVariable) 