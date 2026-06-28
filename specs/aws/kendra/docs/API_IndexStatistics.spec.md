---
id: "@specs/aws/kendra/docs/API_IndexStatistics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IndexStatistics"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# IndexStatistics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_IndexStatistics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IndexStatistics
<a name="API_IndexStatistics"></a>

Provides information about the number of documents and the number of questions and answers in an index.

## Contents
<a name="API_IndexStatistics_Contents"></a>

 ** FaqStatistics **   <a name="kendra-Type-IndexStatistics-FaqStatistics"></a>
The number of question and answer topics in the index.  
Type: [FaqStatistics](API_FaqStatistics.md) object  
Required: Yes

 ** TextDocumentStatistics **   <a name="kendra-Type-IndexStatistics-TextDocumentStatistics"></a>
The number of text documents indexed.  
Type: [TextDocumentStatistics](API_TextDocumentStatistics.md) object  
Required: Yes

## See Also
<a name="API_IndexStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/IndexStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/IndexStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/IndexStatistics) 