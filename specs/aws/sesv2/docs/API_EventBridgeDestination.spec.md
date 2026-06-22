---
id: "@specs/aws/sesv2/docs/API_EventBridgeDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventBridgeDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EventBridgeDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EventBridgeDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventBridgeDestination
<a name="API_EventBridgeDestination"></a>

An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.

## Contents
<a name="API_EventBridgeDestination_Contents"></a>

 ** EventBusArn **   <a name="SES-Type-EventBridgeDestination-EventBusArn"></a>
The Amazon Resource Name (ARN) of the Amazon EventBridge bus to publish email events to. Only the default bus is supported.   
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## See Also
<a name="API_EventBridgeDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EventBridgeDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EventBridgeDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EventBridgeDestination) 