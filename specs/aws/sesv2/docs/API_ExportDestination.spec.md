---
id: "@specs/aws/sesv2/docs/API_ExportDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ExportDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ExportDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportDestination
<a name="API_ExportDestination"></a>

An object that contains details about the destination of the export job.

## Contents
<a name="API_ExportDestination_Contents"></a>

 ** DataFormat **   <a name="SES-Type-ExportDestination-DataFormat"></a>
The data format of the final export job file, can be one of the following:  
+  `CSV` - A comma-separated values file.
+  `JSON` - A Json file.
Type: String  
Valid Values: `CSV | JSON`   
Required: Yes

 ** S3Url **   <a name="SES-Type-ExportDestination-S3Url"></a>
An Amazon S3 pre-signed URL that points to the generated export file.  
Type: String  
Pattern: `^s3:\/\/([^\/]+)\/(.*?([^\/]+)\/?)$`   
Required: No

## See Also
<a name="API_ExportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ExportDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ExportDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ExportDestination) 