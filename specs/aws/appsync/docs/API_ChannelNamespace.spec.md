---
id: "@specs/aws/appsync/docs/API_ChannelNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ChannelNamespace"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# ChannelNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_ChannelNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ChannelNamespace
<a name="API_ChannelNamespace"></a>

Describes a channel namespace associated with an `Api`. The `ChannelNamespace` contains the definitions for code handlers for the `Api`.

## Contents
<a name="API_ChannelNamespace_Contents"></a>

 ** apiId **   <a name="appsync-Type-ChannelNamespace-apiId"></a>
The `Api` ID.  
Type: String  
Required: No

 ** channelNamespaceArn **   <a name="appsync-Type-ChannelNamespace-channelNamespaceArn"></a>
The Amazon Resource Name (ARN) for the `ChannelNamespace`.  
Type: String  
Required: No

 ** codeHandlers **   <a name="appsync-Type-ChannelNamespace-codeHandlers"></a>
The event handler functions that run custom business logic to process published events and subscribe requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: No

 ** created **   <a name="appsync-Type-ChannelNamespace-created"></a>
The date and time that the `ChannelNamespace` was created.  
Type: Timestamp  
Required: No

 ** handlerConfigs **   <a name="appsync-Type-ChannelNamespace-handlerConfigs"></a>
The configuration for the `OnPublish` and `OnSubscribe` handlers.  
Type: [HandlerConfigs](API_HandlerConfigs.md) object  
Required: No

 ** lastModified **   <a name="appsync-Type-ChannelNamespace-lastModified"></a>
The date and time that the `ChannelNamespace` was last changed.  
Type: Timestamp  
Required: No

 ** name **   <a name="appsync-Type-ChannelNamespace-name"></a>
The name of the channel namespace. This name must be unique within the `Api`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([A-Za-z0-9](?:[A-Za-z0-9\-]{0,48}[A-Za-z0-9])?)`   
Required: No

 ** publishAuthModes **   <a name="appsync-Type-ChannelNamespace-publishAuthModes"></a>
The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default `Api`authorization configuration.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: No

 ** subscribeAuthModes **   <a name="appsync-Type-ChannelNamespace-subscribeAuthModes"></a>
The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default `Api`authorization configuration.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: No

 ** tags **   <a name="appsync-Type-ChannelNamespace-tags"></a>
A map with keys of `TagKey` objects and values of `TagValue` objects.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

## See Also
<a name="API_ChannelNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ChannelNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ChannelNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ChannelNamespace) 