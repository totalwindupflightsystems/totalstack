---
id: "@specs/aws/emr/docs/API_PortRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PortRange"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PortRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PortRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PortRange
<a name="API_PortRange"></a>

A list of port ranges that are permitted to allow inbound traffic from all public IP addresses. To specify a single port, use the same value for `MinRange` and `MaxRange`.

## Contents
<a name="API_PortRange_Contents"></a>

 ** MinRange **   <a name="EMR-Type-PortRange-MinRange"></a>
The smallest port number in a specified range of port numbers.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 65535.  
Required: Yes

 ** MaxRange **   <a name="EMR-Type-PortRange-MaxRange"></a>
The smallest port number in a specified range of port numbers.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_PortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PortRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PortRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PortRange) 