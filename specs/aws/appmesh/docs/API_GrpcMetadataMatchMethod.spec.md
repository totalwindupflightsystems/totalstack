---
id: "@specs/aws/appmesh/docs/API_GrpcMetadataMatchMethod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcMetadataMatchMethod"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcMetadataMatchMethod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcMetadataMatchMethod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcMetadataMatchMethod
<a name="API_GrpcMetadataMatchMethod"></a>

An object representing the method header to be matched.

## Contents
<a name="API_GrpcMetadataMatchMethod_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** exact **   <a name="appmesh-Type-GrpcMetadataMatchMethod-exact"></a>
The exact method header to be matched on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** prefix **   <a name="appmesh-Type-GrpcMetadataMatchMethod-prefix"></a>
The specified beginning characters of the method header to be matched on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** range **   <a name="appmesh-Type-GrpcMetadataMatchMethod-range"></a>
An object that represents the range of values to match on. The first character of the range is included in the range, though the last character is not. For example, if the range specified were 1-100, only values 1-99 would be matched.  
Type: [MatchRange](API_MatchRange.md) object  
Required: No

 ** regex **   <a name="appmesh-Type-GrpcMetadataMatchMethod-regex"></a>
The regex used to match the method header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** suffix **   <a name="appmesh-Type-GrpcMetadataMatchMethod-suffix"></a>
The specified ending characters of the method header to match on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_GrpcMetadataMatchMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcMetadataMatchMethod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcMetadataMatchMethod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcMetadataMatchMethod) 