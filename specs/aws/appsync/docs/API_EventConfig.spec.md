---
id: "@specs/aws/appsync/docs/API_EventConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# EventConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_EventConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventConfig
<a name="API_EventConfig"></a>

Describes the authorization configuration for connections, message publishing, message subscriptions, and logging for an Event API.

## Contents
<a name="API_EventConfig_Contents"></a>

 ** authProviders **   <a name="appsync-Type-EventConfig-authProviders"></a>
A list of authorization providers.  
Type: Array of [AuthProvider](API_AuthProvider.md) objects  
Required: Yes

 ** connectionAuthModes **   <a name="appsync-Type-EventConfig-connectionAuthModes"></a>
A list of valid authorization modes for the Event API connections.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: Yes

 ** defaultPublishAuthModes **   <a name="appsync-Type-EventConfig-defaultPublishAuthModes"></a>
A list of valid authorization modes for the Event API publishing.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: Yes

 ** defaultSubscribeAuthModes **   <a name="appsync-Type-EventConfig-defaultSubscribeAuthModes"></a>
A list of valid authorization modes for the Event API subscriptions.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: Yes

 ** logConfig **   <a name="appsync-Type-EventConfig-logConfig"></a>
The CloudWatch Logs configuration for the Event API.  
Type: [EventLogConfig](API_EventLogConfig.md) object  
Required: No

## See Also
<a name="API_EventConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/EventConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/EventConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/EventConfig) 