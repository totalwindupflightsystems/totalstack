---
id: "@specs/aws/appsync/docs/API_CodeError"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CodeError"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CodeError

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CodeError
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CodeError
<a name="API_CodeError"></a>

Describes an AppSync error.

## Contents
<a name="API_CodeError_Contents"></a>

 ** errorType **   <a name="appsync-Type-CodeError-errorType"></a>
The type of code error.   
Examples include, but aren't limited to: `LINT_ERROR`, `PARSER_ERROR`.  
Type: String  
Required: No

 ** location **   <a name="appsync-Type-CodeError-location"></a>
The line, column, and span location of the error in the code.  
Type: [CodeErrorLocation](API_CodeErrorLocation.md) object  
Required: No

 ** value **   <a name="appsync-Type-CodeError-value"></a>
A user presentable error.  
Examples include, but aren't limited to: `Parsing error: Unterminated string literal`.  
Type: String  
Required: No

## See Also
<a name="API_CodeError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CodeError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CodeError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CodeError) 