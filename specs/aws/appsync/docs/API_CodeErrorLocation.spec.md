---
id: "@specs/aws/appsync/docs/API_CodeErrorLocation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CodeErrorLocation"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CodeErrorLocation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CodeErrorLocation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CodeErrorLocation
<a name="API_CodeErrorLocation"></a>

Describes the location of the error in a code sample.

## Contents
<a name="API_CodeErrorLocation_Contents"></a>

 ** column **   <a name="appsync-Type-CodeErrorLocation-column"></a>
The column number in the code. Defaults to `0` if unknown.  
Type: Integer  
Required: No

 ** line **   <a name="appsync-Type-CodeErrorLocation-line"></a>
The line number in the code. Defaults to `0` if unknown.  
Type: Integer  
Required: No

 ** span **   <a name="appsync-Type-CodeErrorLocation-span"></a>
The span/length of the error. Defaults to `-1` if unknown.  
Type: Integer  
Required: No

## See Also
<a name="API_CodeErrorLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CodeErrorLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CodeErrorLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CodeErrorLocation) 