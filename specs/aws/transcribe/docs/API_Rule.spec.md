---
id: "@specs/aws/transcribe/docs/API_Rule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Rule"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Rule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_Rule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Rule
<a name="API_Rule"></a>

A rule is a set of criteria that you can specify to flag an attribute in your Call Analytics output. Rules define a Call Analytics category.

Rules can include these parameters: [InterruptionFilter](API_InterruptionFilter.md), [NonTalkTimeFilter](API_NonTalkTimeFilter.md), [SentimentFilter](API_SentimentFilter.md), and [TranscriptFilter](API_TranscriptFilter.md).

To learn more about Call Analytics rules and categories, see [Creating categories for post-call transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html) and [Creating categories for real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html).

To learn more about Call Analytics, see [Analyzing call center audio with Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html).

## Contents
<a name="API_Rule_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** InterruptionFilter **   <a name="transcribe-Type-Rule-InterruptionFilter"></a>
Flag the presence or absence of interruptions in your Call Analytics transcription output. Refer to [InterruptionFilter](API_InterruptionFilter.md) for more detail.  
Type: [InterruptionFilter](API_InterruptionFilter.md) object  
Required: No

 ** NonTalkTimeFilter **   <a name="transcribe-Type-Rule-NonTalkTimeFilter"></a>
Flag the presence or absence of periods of silence in your Call Analytics transcription output. Refer to [NonTalkTimeFilter](API_NonTalkTimeFilter.md) for more detail.  
Type: [NonTalkTimeFilter](API_NonTalkTimeFilter.md) object  
Required: No

 ** SentimentFilter **   <a name="transcribe-Type-Rule-SentimentFilter"></a>
Flag the presence or absence of specific sentiments in your Call Analytics transcription output. Refer to [SentimentFilter](API_SentimentFilter.md) for more detail.  
Type: [SentimentFilter](API_SentimentFilter.md) object  
Required: No

 ** TranscriptFilter **   <a name="transcribe-Type-Rule-TranscriptFilter"></a>
Flag the presence or absence of specific words or phrases in your Call Analytics transcription output. Refer to [TranscriptFilter](API_TranscriptFilter.md) for more detail.  
Type: [TranscriptFilter](API_TranscriptFilter.md) object  
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/Rule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/Rule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/Rule) 