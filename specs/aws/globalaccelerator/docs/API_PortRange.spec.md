---
id: "@specs/aws/globalaccelerator/docs/API_PortRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PortRange"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# PortRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_PortRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PortRange
<a name="API_PortRange"></a>

A complex type for a range of ports for a listener.

## Contents
<a name="API_PortRange_Contents"></a>

 ** FromPort **   <a name="globalaccelerator-Type-PortRange-FromPort"></a>
The first port in the range of ports, inclusive.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** ToPort **   <a name="globalaccelerator-Type-PortRange-ToPort"></a>
The last port in the range of ports, inclusive.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_PortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/PortRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/PortRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/PortRange) 