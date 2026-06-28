---
id: "@specs/aws/transcribe/docs/API_streaming_MedicalScribeSessionControlEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MedicalScribeSessionControlEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# MedicalScribeSessionControlEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_MedicalScribeSessionControlEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MedicalScribeSessionControlEvent
<a name="API_streaming_MedicalScribeSessionControlEvent"></a>

Specify the lifecycle of your streaming session.

## Contents
<a name="API_streaming_MedicalScribeSessionControlEvent_Contents"></a>

 ** Type **   <a name="transcribe-Type-streaming_MedicalScribeSessionControlEvent-Type"></a>
The type of `MedicalScribeSessionControlEvent`.   
Possible Values:  
+  `END_OF_SESSION` - Indicates the audio streaming is complete. After you send an END\_OF\_SESSION event, AWS HealthScribe starts the post-stream analytics. The session can't be resumed after this event is sent. After AWS HealthScribe processes the event, the real-time `StreamStatus` is `COMPLETED`. You get the `StreamStatus` and other stream details with the [GetMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_GetMedicalScribeStream.html) API operation. For more information about different streaming statuses, see the `StreamStatus` description in the [MedicalScribeStreamDetails](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeStreamDetails.html). 
Type: String  
Valid Values: `END_OF_SESSION`   
Required: Yes

## See Also
<a name="API_streaming_MedicalScribeSessionControlEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeSessionControlEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeSessionControlEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeSessionControlEvent) 