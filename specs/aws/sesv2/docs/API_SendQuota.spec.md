---
id: "@specs/aws/sesv2/docs/API_SendQuota"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SendQuota"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# SendQuota

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_SendQuota
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SendQuota
<a name="API_SendQuota"></a>

An object that contains information about the per-day and per-second sending limits for your Amazon SES account in the current AWS Region.

## Contents
<a name="API_SendQuota_Contents"></a>

 ** Max24HourSend **   <a name="SES-Type-SendQuota-Max24HourSend"></a>
The maximum number of emails that you can send in the current AWS Region over a 24-hour period. A value of -1 signifies an unlimited quota. (This value is also referred to as your *sending quota*.)  
Type: Double  
Required: No

 ** MaxSendRate **   <a name="SES-Type-SendQuota-MaxSendRate"></a>
The maximum number of emails that you can send per second in the current AWS Region. This value is also called your *maximum sending rate* or your *maximum TPS (transactions per second) rate*.  
Type: Double  
Required: No

 ** SentLast24Hours **   <a name="SES-Type-SendQuota-SentLast24Hours"></a>
The number of emails sent from your Amazon SES account in the current AWS Region over the past 24 hours.  
Type: Double  
Required: No

## See Also
<a name="API_SendQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SendQuota) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SendQuota) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SendQuota) 