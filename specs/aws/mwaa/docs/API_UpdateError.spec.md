---
id: "@specs/aws/mwaa/docs/API_UpdateError"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateError"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# UpdateError

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_UpdateError
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateError
<a name="API_UpdateError"></a>

Describes the error(s) encountered with the last update of the environment.

## Contents
<a name="API_UpdateError_Contents"></a>

 ** ErrorCode **   <a name="mwaa-Type-UpdateError-ErrorCode"></a>
The error code that corresponds to the error with the last update.  
Type: String  
Required: No

 ** ErrorMessage **   <a name="mwaa-Type-UpdateError-ErrorMessage"></a>
The error message that corresponds to the error code.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.+`   
Required: No

## See Also
<a name="API_UpdateError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/UpdateError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/UpdateError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/UpdateError) 