---
id: "@specs/aws/amplify/docs/API_Backend"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Backend"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# Backend

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_Backend
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Backend
<a name="API_Backend"></a>

Describes the backend associated with an Amplify `Branch`.

This property is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## Contents
<a name="API_Backend_Contents"></a>

 ** stackArn **   <a name="amplify-Type-Backend-stackArn"></a>
The Amazon Resource Name (ARN) for the CloudFormation stack.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws:cloudformation:[a-z0-9-]+:\d{12}:stack/.+/.+$`   
Required: No

## See Also
<a name="API_Backend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/Backend) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/Backend) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/Backend) 