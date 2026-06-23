---
id: "@specs/aws/comprehend/docs/API_TargetedSentimentEntity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TargetedSentimentEntity"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# TargetedSentimentEntity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_TargetedSentimentEntity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TargetedSentimentEntity
<a name="API_TargetedSentimentEntity"></a>

Information about one of the entities found by targeted sentiment analysis.

For more information about targeted sentiment, see [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html) in the *Amazon Comprehend Developer Guide*.

## Contents
<a name="API_TargetedSentimentEntity_Contents"></a>

 ** DescriptiveMentionIndex **   <a name="comprehend-Type-TargetedSentimentEntity-DescriptiveMentionIndex"></a>
One or more index into the Mentions array that provides the best name for the entity group.  
Type: Array of integers  
Required: No

 ** Mentions **   <a name="comprehend-Type-TargetedSentimentEntity-Mentions"></a>
An array of mentions of the entity in the document. The array represents a co-reference group. See [ Co-reference group](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html#how-targeted-sentiment-values) for an example.   
Type: Array of [TargetedSentimentMention](API_TargetedSentimentMention.md) objects  
Required: No

## See Also
<a name="API_TargetedSentimentEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/TargetedSentimentEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/TargetedSentimentEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/TargetedSentimentEntity) 