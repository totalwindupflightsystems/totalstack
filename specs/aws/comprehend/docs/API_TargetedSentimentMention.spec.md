---
id: "@specs/aws/comprehend/docs/API_TargetedSentimentMention"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TargetedSentimentMention"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# TargetedSentimentMention

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_TargetedSentimentMention
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TargetedSentimentMention
<a name="API_TargetedSentimentMention"></a>

Information about one mention of an entity. The mention information includes the location of the mention in the text and the sentiment of the mention.

For more information about targeted sentiment, see [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html) in the *Amazon Comprehend Developer Guide*.

## Contents
<a name="API_TargetedSentimentMention_Contents"></a>

 ** BeginOffset **   <a name="comprehend-Type-TargetedSentimentMention-BeginOffset"></a>
The offset into the document text where the mention begins.  
Type: Integer  
Required: No

 ** EndOffset **   <a name="comprehend-Type-TargetedSentimentMention-EndOffset"></a>
The offset into the document text where the mention ends.  
Type: Integer  
Required: No

 ** GroupScore **   <a name="comprehend-Type-TargetedSentimentMention-GroupScore"></a>
The confidence that all the entities mentioned in the group relate to the same entity.  
Type: Float  
Required: No

 ** MentionSentiment **   <a name="comprehend-Type-TargetedSentimentMention-MentionSentiment"></a>
Contains the sentiment and sentiment score for the mention.  
Type: [MentionSentiment](API_MentionSentiment.md) object  
Required: No

 ** Score **   <a name="comprehend-Type-TargetedSentimentMention-Score"></a>
Model confidence that the entity is relevant. Value range is zero to one, where one is highest confidence.  
Type: Float  
Required: No

 ** Text **   <a name="comprehend-Type-TargetedSentimentMention-Text"></a>
The text in the document that identifies the entity.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Type **   <a name="comprehend-Type-TargetedSentimentMention-Type"></a>
The type of the entity. Amazon Comprehend supports a variety of [entity types](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html#how-targeted-sentiment-entities).  
Type: String  
Valid Values: `PERSON | LOCATION | ORGANIZATION | FACILITY | BRAND | COMMERCIAL_ITEM | MOVIE | MUSIC | BOOK | SOFTWARE | GAME | PERSONAL_TITLE | EVENT | DATE | QUANTITY | ATTRIBUTE | OTHER`   
Required: No

## See Also
<a name="API_TargetedSentimentMention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/TargetedSentimentMention) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/TargetedSentimentMention) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/TargetedSentimentMention) 