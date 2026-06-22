---
id: "@specs/aws/sesv2/docs/API_ExportStatistics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportStatistics"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ExportStatistics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ExportStatistics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportStatistics
<a name="API_ExportStatistics"></a>

Statistics about the execution of an export job.

## Contents
<a name="API_ExportStatistics_Contents"></a>

 ** ExportedRecordsCount **   <a name="SES-Type-ExportStatistics-ExportedRecordsCount"></a>
The number of records that were exported to the final export file.  
This value might not be available for all export source types  
Type: Integer  
Required: No

 ** ProcessedRecordsCount **   <a name="SES-Type-ExportStatistics-ProcessedRecordsCount"></a>
The number of records that were processed to generate the final export file.  
Type: Integer  
Required: No

## See Also
<a name="API_ExportStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ExportStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ExportStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ExportStatistics) 