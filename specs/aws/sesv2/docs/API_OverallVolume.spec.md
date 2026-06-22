---
id: "@specs/aws/sesv2/docs/API_OverallVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OverallVolume"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# OverallVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_OverallVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OverallVolume
<a name="API_OverallVolume"></a>

An object that contains information about email that was sent from the selected domain.

## Contents
<a name="API_OverallVolume_Contents"></a>

 ** DomainIspPlacements **   <a name="SES-Type-OverallVolume-DomainIspPlacements"></a>
An object that contains inbox and junk mail placement metrics for individual email providers.  
Type: Array of [DomainIspPlacement](API_DomainIspPlacement.md) objects  
Required: No

 ** ReadRatePercent **   <a name="SES-Type-OverallVolume-ReadRatePercent"></a>
The percentage of emails that were sent from the domain that were read by their recipients.  
Type: Double  
Required: No

 ** VolumeStatistics **   <a name="SES-Type-OverallVolume-VolumeStatistics"></a>
An object that contains information about the numbers of messages that arrived in recipients' inboxes and junk mail folders.  
Type: [VolumeStatistics](API_VolumeStatistics.md) object  
Required: No

## See Also
<a name="API_OverallVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/OverallVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/OverallVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/OverallVolume) 