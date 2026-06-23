---
id: "@specs/aws/amplify/docs/API_CustomRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRule"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CustomRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CustomRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRule
<a name="API_CustomRule"></a>

Describes a custom rewrite or redirect rule. 

## Contents
<a name="API_CustomRule_Contents"></a>

 ** source **   <a name="amplify-Type-CustomRule-source"></a>
The source pattern for a URL rewrite or redirect rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: Yes

 ** target **   <a name="amplify-Type-CustomRule-target"></a>
The target pattern for a URL rewrite or redirect rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: Yes

 ** condition **   <a name="amplify-Type-CustomRule-condition"></a>
The condition for a URL rewrite or redirect rule, such as a country code.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(?s).*`   
Required: No

 ** status **   <a name="amplify-Type-CustomRule-status"></a>
The status code for a URL rewrite or redirect rule.     
200  
Represents a 200 rewrite rule.  
301  
Represents a 301 (moved permanently) redirect rule. This and all future requests should be directed to the target URL.   
302  
Represents a 302 temporary redirect rule.  
404  
Represents a 404 redirect rule.  
404-200  
Represents a 404 rewrite rule.
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 7.  
Pattern: `.{3,7}`   
Required: No

## See Also
<a name="API_CustomRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CustomRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CustomRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CustomRule) 