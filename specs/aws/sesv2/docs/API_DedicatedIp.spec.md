---
id: "@specs/aws/sesv2/docs/API_DedicatedIp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DedicatedIp"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DedicatedIp

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DedicatedIp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DedicatedIp
<a name="API_DedicatedIp"></a>

Contains information about a dedicated IP address that is associated with your Amazon SES account.

To learn more about requesting dedicated IP addresses, see [Requesting and Relinquishing Dedicated IP Addresses](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/dedicated-ip-case.html) in the *Amazon SES Developer Guide*.

## Contents
<a name="API_DedicatedIp_Contents"></a>

 ** Ip **   <a name="SES-Type-DedicatedIp-Ip"></a>
An IPv4 address.  
Type: String  
Required: Yes

 ** WarmupPercentage **   <a name="SES-Type-DedicatedIp-WarmupPercentage"></a>
Indicates the progress of your dedicated IP warm-up:  
+  `0-100` – For standard dedicated IP addresses, this shows the warm-up completion percentage. A value of 100 means the IP address is fully warmed up and ready for use.
+  `-1` – Appears for IP addresses in managed dedicated pools where Amazon SES automatically handles the warm-up process, making the percentage not applicable.
Type: Integer  
Required: Yes

 ** WarmupStatus **   <a name="SES-Type-DedicatedIp-WarmupStatus"></a>
The warm-up status of a dedicated IP address. The status can have one of the following values:  
+  `IN_PROGRESS` – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing.
+  `DONE` – The dedicated IP warm-up process is complete, and the IP address is ready to use.
+  `NOT_APPLICABLE` – The warm-up status doesn't apply to this IP address. This status is used for IP addresses in managed dedicated IP pools, where Amazon SES automatically handles the warm-up process.
Type: String  
Valid Values: `IN_PROGRESS | DONE | NOT_APPLICABLE`   
Required: Yes

 ** PoolName **   <a name="SES-Type-DedicatedIp-PoolName"></a>
The name of the dedicated IP pool that the IP address is associated with.  
Type: String  
Required: No

## See Also
<a name="API_DedicatedIp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DedicatedIp) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DedicatedIp) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DedicatedIp) 