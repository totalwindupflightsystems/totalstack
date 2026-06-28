---
id: "@specs/aws/network-firewall/docs/API_AvailabilityZoneMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AvailabilityZoneMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AvailabilityZoneMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AvailabilityZoneMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AvailabilityZoneMetadata
<a name="API_AvailabilityZoneMetadata"></a>

High-level information about an Availability Zone where the firewall has an endpoint defined. 

## Contents
<a name="API_AvailabilityZoneMetadata_Contents"></a>

 ** IPAddressType **   <a name="networkfirewall-Type-AvailabilityZoneMetadata-IPAddressType"></a>
The IP address type of the Firewall subnet in the Availability Zone. You can't change the IP address type after you create the subnet.  
Type: String  
Valid Values: `DUALSTACK | IPV4 | IPV6`   
Required: No

## See Also
<a name="API_AvailabilityZoneMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AvailabilityZoneMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AvailabilityZoneMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AvailabilityZoneMetadata) 