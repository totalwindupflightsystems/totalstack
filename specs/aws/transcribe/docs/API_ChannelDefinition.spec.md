---
id: "@specs/aws/transcribe/docs/API_ChannelDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ChannelDefinition"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ChannelDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ChannelDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ChannelDefinition
<a name="API_ChannelDefinition"></a>

Makes it possible to specify which speaker is on which channel. For example, if your agent is the first participant to speak, you would set `ChannelId` to `0` (to indicate the first channel) and `ParticipantRole` to `AGENT` (to indicate that it's the agent speaking).

## Contents
<a name="API_ChannelDefinition_Contents"></a>

 ** ChannelId **   <a name="transcribe-Type-ChannelDefinition-ChannelId"></a>
Specify the audio channel you want to define.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** ParticipantRole **   <a name="transcribe-Type-ChannelDefinition-ParticipantRole"></a>
Specify the speaker you want to define. Omitting this parameter is equivalent to specifying both participants.  
Type: String  
Valid Values: `AGENT | CUSTOMER`   
Required: No

## See Also
<a name="API_ChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ChannelDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ChannelDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ChannelDefinition) 