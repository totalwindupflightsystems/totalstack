---
id: "@specs/aws/comprehend/docs/API_MentionSentiment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MentionSentiment"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# MentionSentiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_MentionSentiment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MentionSentiment
<a name="API_MentionSentiment"></a>

Contains the sentiment and sentiment score for one mention of an entity.

For more information about targeted sentiment, see [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html) in the *Amazon Comprehend Developer Guide*.

## Contents
<a name="API_MentionSentiment_Contents"></a>

 ** Sentiment **   <a name="comprehend-Type-MentionSentiment-Sentiment"></a>
The sentiment of the mention.   
Type: String  
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL | MIXED`   
Required: No

 ** SentimentScore **   <a name="comprehend-Type-MentionSentiment-SentimentScore"></a>
Describes the level of confidence that Amazon Comprehend has in the accuracy of its detection of sentiments.  
Type: [SentimentScore](API_SentimentScore.md) object  
Required: No

## See Also
<a name="API_MentionSentiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/MentionSentiment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/MentionSentiment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/MentionSentiment) 