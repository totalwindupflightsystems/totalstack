---
id: "@specs/aws/kendra/docs/API_Highlight"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Highlight"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Highlight

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Highlight
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Highlight
<a name="API_Highlight"></a>

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

## Contents
<a name="API_Highlight_Contents"></a>

 ** BeginOffset **   <a name="kendra-Type-Highlight-BeginOffset"></a>
The zero-based location in the response string where the highlight starts.  
Type: Integer  
Required: Yes

 ** EndOffset **   <a name="kendra-Type-Highlight-EndOffset"></a>
The zero-based location in the response string where the highlight ends.  
Type: Integer  
Required: Yes

 ** TopAnswer **   <a name="kendra-Type-Highlight-TopAnswer"></a>
Indicates whether the response is the best response. True if this is the best response; otherwise, false.  
Type: Boolean  
Required: No

 ** Type **   <a name="kendra-Type-Highlight-Type"></a>
The highlight type.   
Type: String  
Valid Values: `STANDARD | THESAURUS_SYNONYM`   
Required: No

## See Also
<a name="API_Highlight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Highlight) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Highlight) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Highlight) 