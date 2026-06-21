---
id: "@specs/aws/cloudtrail/docs/API_RefreshScheduleFrequency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RefreshScheduleFrequency"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# RefreshScheduleFrequency

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_RefreshScheduleFrequency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RefreshScheduleFrequency
<a name="API_RefreshScheduleFrequency"></a>

 Specifies the frequency for a dashboard refresh schedule. 

 For a custom dashboard, you can schedule a refresh for every 1, 6, 12, or 24 hours, or every day. 

## Contents
<a name="API_RefreshScheduleFrequency_Contents"></a>

 ** Unit **   <a name="awscloudtrail-Type-RefreshScheduleFrequency-Unit"></a>
 The unit to use for the refresh.   
For custom dashboards, the unit can be `HOURS` or `DAYS`.  
For the Highlights dashboard, the `Unit` must be `HOURS`.  
Type: String  
Valid Values: `HOURS | DAYS`   
Required: No

 ** Value **   <a name="awscloudtrail-Type-RefreshScheduleFrequency-Value"></a>
 The value for the refresh schedule.   
 For custom dashboards, the following values are valid when the unit is `HOURS`: `1`, `6`, `12`, `24`   
For custom dashboards, the only valid value when the unit is `DAYS` is `1`.  
For the Highlights dashboard, the `Value` must be `6`.  
Type: Integer  
Required: No

## See Also
<a name="API_RefreshScheduleFrequency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RefreshScheduleFrequency) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RefreshScheduleFrequency) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RefreshScheduleFrequency) 