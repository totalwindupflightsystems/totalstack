---
id: "@specs/aws/transcribe/docs/API_streaming_ConfigurationEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConfigurationEvent"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ConfigurationEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_ConfigurationEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConfigurationEvent
<a name="API_streaming_ConfigurationEvent"></a>

Allows you to set audio channel definitions and post-call analytics settings.

## Contents
<a name="API_streaming_ConfigurationEvent_Contents"></a>

 ** ChannelDefinitions **   <a name="transcribe-Type-streaming_ConfigurationEvent-ChannelDefinitions"></a>
Indicates which speaker is on which audio channel.  
Type: Array of [ChannelDefinition](API_streaming_ChannelDefinition.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

 ** PostCallAnalyticsSettings **   <a name="transcribe-Type-streaming_ConfigurationEvent-PostCallAnalyticsSettings"></a>
Provides additional optional settings for your Call Analytics post-call request, including encryption and output locations for your redacted transcript.  
 `PostCallAnalyticsSettings` provides you with the same insights as a Call Analytics post-call transcription. Refer to [Post-call analytics](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) for more information on this feature.  
Type: [PostCallAnalyticsSettings](API_streaming_PostCallAnalyticsSettings.md) object  
Required: No

## See Also
<a name="API_streaming_ConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/ConfigurationEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/ConfigurationEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/ConfigurationEvent) 