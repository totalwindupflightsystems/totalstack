---
id: "@specs/aws/storagegateway/docs/API_CacheReportInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheReportInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CacheReportInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CacheReportInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheReportInfo
<a name="API_CacheReportInfo"></a>

Contains all informational fields associated with a cache report. Includes name, ARN, tags, status, progress, filters, start time, and end time.

## Contents
<a name="API_CacheReportInfo_Contents"></a>

 ** CacheReportARN **   <a name="StorageGateway-Type-CacheReportInfo-CacheReportARN"></a>
The Amazon Resource Name (ARN) of the cache report you want to describe.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** CacheReportStatus **   <a name="StorageGateway-Type-CacheReportInfo-CacheReportStatus"></a>
The status of the specified cache report.  
Type: String  
Valid Values: `IN_PROGRESS | COMPLETED | CANCELED | FAILED | ERROR`   
Required: No

 ** EndTime **   <a name="StorageGateway-Type-CacheReportInfo-EndTime"></a>
The time at which the gateway stopped generating the cache report.  
Type: Timestamp  
Required: No

 ** ExclusionFilters **   <a name="StorageGateway-Type-CacheReportInfo-ExclusionFilters"></a>
The list of filters and parameters that determine which files are excluded from the report.  
Type: Array of [CacheReportFilter](API_CacheReportFilter.md) objects  
Required: No

 ** FileShareARN **   <a name="StorageGateway-Type-CacheReportInfo-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** InclusionFilters **   <a name="StorageGateway-Type-CacheReportInfo-InclusionFilters"></a>
The list of filters and parameters that determine which files are included in the report.  
Type: Array of [CacheReportFilter](API_CacheReportFilter.md) objects  
Required: No

 ** LocationARN **   <a name="StorageGateway-Type-CacheReportInfo-LocationARN"></a>
The ARN of the Amazon S3 bucket location where the cache report is saved.  
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 1400.  
Required: No

 ** ReportCompletionPercent **   <a name="StorageGateway-Type-CacheReportInfo-ReportCompletionPercent"></a>
The percentage of the report generation process that has been completed at time of inquiry.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** ReportName **   <a name="StorageGateway-Type-CacheReportInfo-ReportName"></a>
The file name of the completed cache report object stored in Amazon S3.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** Role **   <a name="StorageGateway-Type-CacheReportInfo-Role"></a>
The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`   
Required: No

 ** StartTime **   <a name="StorageGateway-Type-CacheReportInfo-StartTime"></a>
The time at which the gateway started generating the cache report.  
Type: Timestamp  
Required: No

 ** Tags **   <a name="StorageGateway-Type-CacheReportInfo-Tags"></a>
The list of key/value tags associated with the report.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_CacheReportInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CacheReportInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CacheReportInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CacheReportInfo) 