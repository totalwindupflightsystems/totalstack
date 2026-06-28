---
id: "@specs/aws/globalaccelerator/docs/API_ByoipCidrEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ByoipCidrEvent"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ByoipCidrEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ByoipCidrEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ByoipCidrEvent
<a name="API_ByoipCidrEvent"></a>

A complex type that contains a `Message` and a `Timestamp` value for changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).

## Contents
<a name="API_ByoipCidrEvent_Contents"></a>

 ** Message **   <a name="globalaccelerator-Type-ByoipCidrEvent-Message"></a>
A string that contains an `Event` message describing changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Timestamp **   <a name="globalaccelerator-Type-ByoipCidrEvent-Timestamp"></a>
A timestamp for when you make a status change for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).  
Type: Timestamp  
Required: No

## See Also
<a name="API_ByoipCidrEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ByoipCidrEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ByoipCidrEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ByoipCidrEvent) 