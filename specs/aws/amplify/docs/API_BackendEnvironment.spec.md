---
id: "@specs/aws/amplify/docs/API_BackendEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BackendEnvironment"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# BackendEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_BackendEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BackendEnvironment
<a name="API_BackendEnvironment"></a>

Describes the backend environment associated with a `Branch` of a Gen 1 Amplify app. Amplify Gen 1 applications are created using Amplify Studio or the Amplify command line interface (CLI).

## Contents
<a name="API_BackendEnvironment_Contents"></a>

 ** backendEnvironmentArn **   <a name="amplify-Type-BackendEnvironment-backendEnvironmentArn"></a>
The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `(?s).*`   
Required: Yes

 ** createTime **   <a name="amplify-Type-BackendEnvironment-createTime"></a>
The creation date and time for a backend environment that is part of an Amplify app.   
Type: Timestamp  
Required: Yes

 ** environmentName **   <a name="amplify-Type-BackendEnvironment-environmentName"></a>
The name for a backend environment that is part of an Amplify app.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** updateTime **   <a name="amplify-Type-BackendEnvironment-updateTime"></a>
The last updated date and time for a backend environment that is part of an Amplify app.   
Type: Timestamp  
Required: Yes

 ** deploymentArtifacts **   <a name="amplify-Type-BackendEnvironment-deploymentArtifacts"></a>
The name of deployment artifacts.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `(?s).+`   
Required: No

 ** stackName **   <a name="amplify-Type-BackendEnvironment-stackName"></a>
The AWS CloudFormation stack name of a backend environment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

## See Also
<a name="API_BackendEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/BackendEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/BackendEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/BackendEnvironment) 