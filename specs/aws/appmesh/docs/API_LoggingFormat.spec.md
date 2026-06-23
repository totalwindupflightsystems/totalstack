---
id: "@specs/aws/appmesh/docs/API_LoggingFormat"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingFormat"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# LoggingFormat

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_LoggingFormat
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingFormat
<a name="API_LoggingFormat"></a>

An object that represents the format for the logs.

## Contents
<a name="API_LoggingFormat_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="appmesh-Type-LoggingFormat-json"></a>
The logging format for JSON.  
Type: Array of [JsonFormatRef](API_JsonFormatRef.md) objects  
Required: No

 ** text **   <a name="appmesh-Type-LoggingFormat-text"></a>
The logging format for text.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

## See Also
<a name="API_LoggingFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/LoggingFormat) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/LoggingFormat) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/LoggingFormat) 