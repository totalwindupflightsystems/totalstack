---
id: "@specs/aws/cloudtrail/docs/API_RefreshSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RefreshSchedule"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# RefreshSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_RefreshSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RefreshSchedule
<a name="API_RefreshSchedule"></a>

 The schedule for a dashboard refresh. 

## Contents
<a name="API_RefreshSchedule_Contents"></a>

 ** Frequency **   <a name="awscloudtrail-Type-RefreshSchedule-Frequency"></a>
 The frequency at which you want the dashboard refreshed.   
Type: [RefreshScheduleFrequency](API_RefreshScheduleFrequency.md) object  
Required: No

 ** Status **   <a name="awscloudtrail-Type-RefreshSchedule-Status"></a>
 Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** TimeOfDay **   <a name="awscloudtrail-Type-RefreshSchedule-TimeOfDay"></a>
 The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.   
Type: String  
Pattern: `^[0-9]{2}:[0-9]{2}`   
Required: No

## See Also
<a name="API_RefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RefreshSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RefreshSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RefreshSchedule) 