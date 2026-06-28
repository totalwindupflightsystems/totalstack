---
id: "@specs/aws/storagegateway/docs/API_BandwidthRateLimitInterval"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BandwidthRateLimitInterval"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# BandwidthRateLimitInterval

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_BandwidthRateLimitInterval
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BandwidthRateLimitInterval
<a name="API_BandwidthRateLimitInterval"></a>

Describes a bandwidth rate limit interval for a gateway. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both.

**Note**  
FSx File Gateway does not support this feature.

## Contents
<a name="API_BandwidthRateLimitInterval_Contents"></a>

 ** DaysOfWeek **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-DaysOfWeek"></a>
 The days of the week component of the bandwidth rate limit interval, represented as ordinal numbers from 0 to 6, where 0 represents Sunday and 6 represents Saturday.   
Type: Array of integers  
Array Members: Minimum number of 1 item. Maximum number of 7 items.  
Valid Range: Minimum value of 0. Maximum value of 6.  
Required: Yes

 ** EndHourOfDay **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-EndHourOfDay"></a>
 The hour of the day to end the bandwidth rate limit interval.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.  
Required: Yes

 ** EndMinuteOfHour **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-EndMinuteOfHour"></a>
 The minute of the hour to end the bandwidth rate limit interval.   
 The bandwidth rate limit interval ends at the end of the minute. To end an interval at the end of an hour, use the value `59`. 
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 59.  
Required: Yes

 ** StartHourOfDay **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-StartHourOfDay"></a>
 The hour of the day to start the bandwidth rate limit interval.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.  
Required: Yes

 ** StartMinuteOfHour **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-StartMinuteOfHour"></a>
 The minute of the hour to start the bandwidth rate limit interval. The interval begins at the start of that minute. To begin an interval exactly at the start of the hour, use the value `0`.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 59.  
Required: Yes

 ** AverageDownloadRateLimitInBitsPerSec **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-AverageDownloadRateLimitInBitsPerSec"></a>
 The average download rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the download rate limit is not set.   
S3 File Gateway does not support this feature.
Type: Long  
Valid Range: Minimum value of 102400.  
Required: No

 ** AverageUploadRateLimitInBitsPerSec **   <a name="StorageGateway-Type-BandwidthRateLimitInterval-AverageUploadRateLimitInBitsPerSec"></a>
 The average upload rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the upload rate limit is not set.   
For Tape Gateway and Volume Gateway, the minimum value is `51200`.  
This field is required for S3 File Gateway, and the minimum value is `104857600`.
Type: Long  
Valid Range: Minimum value of 51200.  
Required: No

## See Also
<a name="API_BandwidthRateLimitInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/BandwidthRateLimitInterval) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/BandwidthRateLimitInterval) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/BandwidthRateLimitInterval) 