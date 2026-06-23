---
id: "@specs/aws/appmesh/docs/API_HeaderMatchMethod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HeaderMatchMethod"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HeaderMatchMethod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HeaderMatchMethod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HeaderMatchMethod
<a name="API_HeaderMatchMethod"></a>

An object that represents the method and value to match with the header value sent in a request. Specify one match method.

## Contents
<a name="API_HeaderMatchMethod_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** exact **   <a name="appmesh-Type-HeaderMatchMethod-exact"></a>
The value sent by the client must match the specified value exactly.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** prefix **   <a name="appmesh-Type-HeaderMatchMethod-prefix"></a>
The value sent by the client must begin with the specified characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** range **   <a name="appmesh-Type-HeaderMatchMethod-range"></a>
An object that represents the range of values to match on.  
Type: [MatchRange](API_MatchRange.md) object  
Required: No

 ** regex **   <a name="appmesh-Type-HeaderMatchMethod-regex"></a>
The value sent by the client must include the specified characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** suffix **   <a name="appmesh-Type-HeaderMatchMethod-suffix"></a>
The value sent by the client must end with the specified characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_HeaderMatchMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HeaderMatchMethod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HeaderMatchMethod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HeaderMatchMethod) 