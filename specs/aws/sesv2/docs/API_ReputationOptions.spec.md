---
id: "@specs/aws/sesv2/docs/API_ReputationOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ReputationOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ReputationOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ReputationOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ReputationOptions
<a name="API_ReputationOptions"></a>

Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region. 

## Contents
<a name="API_ReputationOptions_Contents"></a>

 ** LastFreshStart **   <a name="SES-Type-ReputationOptions-LastFreshStart"></a>
The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.  
Type: Timestamp  
Required: No

 ** ReputationMetricsEnabled **   <a name="SES-Type-ReputationOptions-ReputationMetricsEnabled"></a>
If `true`, tracking of reputation metrics is enabled for the configuration set. If `false`, tracking of reputation metrics is disabled for the configuration set.  
Type: Boolean  
Required: No

## See Also
<a name="API_ReputationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ReputationOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ReputationOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ReputationOptions) 