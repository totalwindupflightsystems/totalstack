---
id: "@specs/aws/appmesh/docs/API_MatchRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MatchRange"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# MatchRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_MatchRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MatchRange
<a name="API_MatchRange"></a>

An object that represents the range of values to match on. The first character of the range is included in the range, though the last character is not. For example, if the range specified were 1-100, only values 1-99 would be matched.

## Contents
<a name="API_MatchRange_Contents"></a>

 ** end **   <a name="appmesh-Type-MatchRange-end"></a>
The end of the range.  
Type: Long  
Required: Yes

 ** start **   <a name="appmesh-Type-MatchRange-start"></a>
The start of the range.  
Type: Long  
Required: Yes

## See Also
<a name="API_MatchRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/MatchRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/MatchRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/MatchRange) 