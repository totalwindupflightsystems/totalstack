---
id: "@specs/aws/amplify/docs/API_Step"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# Step

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_Step
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step
<a name="API_Step"></a>

 Describes an execution step, for an execution job, for an Amplify app. 

## Contents
<a name="API_Step_Contents"></a>

 ** endTime **   <a name="amplify-Type-Step-endTime"></a>
 The end date and time of the execution step.   
Type: Timestamp  
Required: Yes

 ** startTime **   <a name="amplify-Type-Step-startTime"></a>
 The start date and time of the execution step.   
Type: Timestamp  
Required: Yes

 ** status **   <a name="amplify-Type-Step-status"></a>
 The status of the execution step.   
Type: String  
Valid Values: `CREATED | PENDING | PROVISIONING | RUNNING | FAILED | SUCCEED | CANCELLING | CANCELLED`   
Required: Yes

 ** stepName **   <a name="amplify-Type-Step-stepName"></a>
 The name of the execution step.   
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** artifactsUrl **   <a name="amplify-Type-Step-artifactsUrl"></a>
 The URL to the build artifact for the execution step.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** context **   <a name="amplify-Type-Step-context"></a>
 The context for the current step. Includes a build image if the step is build.   
Type: String  
Required: No

 ** logUrl **   <a name="amplify-Type-Step-logUrl"></a>
 The URL to the logs for the execution step.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** screenshots **   <a name="amplify-Type-Step-screenshots"></a>
 The list of screenshot URLs for the execution step, if relevant.   
Type: String to string map  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** statusReason **   <a name="amplify-Type-Step-statusReason"></a>
 The reason for the current step status.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** testArtifactsUrl **   <a name="amplify-Type-Step-testArtifactsUrl"></a>
 The URL to the test artifact for the execution step.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** testConfigUrl **   <a name="amplify-Type-Step-testConfigUrl"></a>
 The URL to the test configuration for the execution step.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/Step) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/Step) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/Step) 