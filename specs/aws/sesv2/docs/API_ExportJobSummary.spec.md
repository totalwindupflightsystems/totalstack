---
id: "@specs/aws/sesv2/docs/API_ExportJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportJobSummary"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ExportJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ExportJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportJobSummary
<a name="API_ExportJobSummary"></a>

A summary of the export job.

## Contents
<a name="API_ExportJobSummary_Contents"></a>

 ** CompletedTimestamp **   <a name="SES-Type-ExportJobSummary-CompletedTimestamp"></a>
The timestamp of when the export job was completed.  
Type: Timestamp  
Required: No

 ** CreatedTimestamp **   <a name="SES-Type-ExportJobSummary-CreatedTimestamp"></a>
The timestamp of when the export job was created.  
Type: Timestamp  
Required: No

 ** ExportSourceType **   <a name="SES-Type-ExportJobSummary-ExportSourceType"></a>
The source type of the export job.  
Type: String  
Valid Values: `METRICS_DATA | MESSAGE_INSIGHTS`   
Required: No

 ** JobId **   <a name="SES-Type-ExportJobSummary-JobId"></a>
The export job ID.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** JobStatus **   <a name="SES-Type-ExportJobSummary-JobStatus"></a>
The status of the export job.  
Type: String  
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | CANCELLED`   
Required: No

## See Also
<a name="API_ExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ExportJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ExportJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ExportJobSummary) 