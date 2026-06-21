---
id: "@specs/aws/cloudtrail/docs/API_ImportStatistics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportStatistics"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ImportStatistics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ImportStatistics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportStatistics
<a name="API_ImportStatistics"></a>

 Provides statistics for the specified `ImportID`. CloudTrail does not update import statistics in real-time. Returned values for parameters such as `EventsCompleted` may be lower than the actual value, because CloudTrail updates statistics incrementally over the course of the import. 

## Contents
<a name="API_ImportStatistics_Contents"></a>

 ** EventsCompleted **   <a name="awscloudtrail-Type-ImportStatistics-EventsCompleted"></a>
 The number of trail events imported into the event data store.   
Type: Long  
Required: No

 ** FailedEntries **   <a name="awscloudtrail-Type-ImportStatistics-FailedEntries"></a>
 The number of failed entries.   
Type: Long  
Required: No

 ** FilesCompleted **   <a name="awscloudtrail-Type-ImportStatistics-FilesCompleted"></a>
The number of log files that completed import.  
Type: Long  
Required: No

 ** PrefixesCompleted **   <a name="awscloudtrail-Type-ImportStatistics-PrefixesCompleted"></a>
 The number of S3 prefixes that completed import.   
Type: Long  
Required: No

 ** PrefixesFound **   <a name="awscloudtrail-Type-ImportStatistics-PrefixesFound"></a>
 The number of S3 prefixes found for the import.   
Type: Long  
Required: No

## See Also
<a name="API_ImportStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportStatistics) 