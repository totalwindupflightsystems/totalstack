---
id: "@specs/aws/polly/docs/API_StartSpeechSynthesisStreamActionStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartSpeechSynthesisStreamActionStream"
status: active
depends_on:
  - "@specs/aws/polly/meta"
---

# StartSpeechSynthesisStreamActionStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/polly/docs/API_StartSpeechSynthesisStreamActionStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartSpeechSynthesisStreamActionStream
<a name="API_StartSpeechSynthesisStreamActionStream"></a>

Inbound event stream for sending input and control events to manage bidirectional speech synthesis.

## Contents
<a name="API_StartSpeechSynthesisStreamActionStream_Contents"></a>

 ** CloseStreamEvent **   <a name="polly-Type-StartSpeechSynthesisStreamActionStream-CloseStreamEvent"></a>
An event indicating the end of the input stream.  
Type: [CloseStreamEvent](API_CloseStreamEvent.md) object  
Required: No

 ** TextEvent **   <a name="polly-Type-StartSpeechSynthesisStreamActionStream-TextEvent"></a>
A text event containing content to be synthesized.  
Type: [TextEvent](API_TextEvent.md) object  
Required: No

## See Also
<a name="API_StartSpeechSynthesisStreamActionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStreamActionStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStreamActionStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStreamActionStream) 