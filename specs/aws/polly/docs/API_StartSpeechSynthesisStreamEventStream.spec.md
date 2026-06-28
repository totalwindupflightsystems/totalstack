---
id: "@specs/aws/polly/docs/API_StartSpeechSynthesisStreamEventStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartSpeechSynthesisStreamEventStream"
status: active
depends_on:
  - "@specs/aws/polly/meta"
---

# StartSpeechSynthesisStreamEventStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/polly/docs/API_StartSpeechSynthesisStreamEventStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartSpeechSynthesisStreamEventStream
<a name="API_StartSpeechSynthesisStreamEventStream"></a>

Outbound event stream that contains synthesized audio data and stream status events.

## Contents
<a name="API_StartSpeechSynthesisStreamEventStream_Contents"></a>

 ** AudioEvent **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-AudioEvent"></a>
An audio event containing synthesized speech.  
Type: [AudioEvent](API_AudioEvent.md) object  
Required: No

 ** ServiceFailureException **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-ServiceFailureException"></a>
An unknown condition has caused a service failure.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** ServiceQuotaExceededException **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-ServiceQuotaExceededException"></a>
An exception indicating a service quota would be exceeded.  
Type: Exception  
HTTP Status Code: 402  
Required: No

 ** StreamClosedEvent **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-StreamClosedEvent"></a>
An event, with summary information, indicating the stream has closed.  
Type: [StreamClosedEvent](API_StreamClosedEvent.md) object  
Required: No

 ** ThrottlingException **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-ThrottlingException"></a>
An exception indicating the request was throttled.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** ValidationException **   <a name="polly-Type-StartSpeechSynthesisStreamEventStream-ValidationException"></a>
An exception indicating the input failed validation.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_StartSpeechSynthesisStreamEventStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStreamEventStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStreamEventStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStreamEventStream) 