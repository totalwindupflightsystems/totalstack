---
id: "@specs/aws/fsx/docs/API_CompletionReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CompletionReport"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CompletionReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CompletionReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CompletionReport
<a name="API_CompletionReport"></a>

Provides a report detailing the data repository task results of the files processed that match the criteria specified in the report `Scope` parameter. FSx delivers the report to the file system's linked data repository in Amazon S3, using the path specified in the report `Path` parameter. You can specify whether or not a report gets generated for a task using the `Enabled` parameter.

## Contents
<a name="API_CompletionReport_Contents"></a>

 ** Enabled **   <a name="FSx-Type-CompletionReport-Enabled"></a>
Set `Enabled` to `True` to generate a `CompletionReport` when the task completes. If set to `true`, then you need to provide a report `Scope`, `Path`, and `Format`. Set `Enabled` to `False` if you do not want a `CompletionReport` generated when the task completes.  
Type: Boolean  
Required: Yes

 ** Format **   <a name="FSx-Type-CompletionReport-Format"></a>
Required if `Enabled` is set to `true`. Specifies the format of the `CompletionReport`. `REPORT_CSV_20191124` is the only format currently supported. When `Format` is set to `REPORT_CSV_20191124`, the `CompletionReport` is provided in CSV format, and is delivered to `{path}/task-{id}/failures.csv`.   
Type: String  
Valid Values: `REPORT_CSV_20191124`   
Required: No

 ** Path **   <a name="FSx-Type-CompletionReport-Path"></a>
Required if `Enabled` is set to `true`. Specifies the location of the report on the file system's linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The `Path` you provide must be located within the file system’s ExportPath. An example `Path` value is "s3://amzn-s3-demo-bucket/myExportPath/optionalPrefix". The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** Scope **   <a name="FSx-Type-CompletionReport-Scope"></a>
Required if `Enabled` is set to `true`. Specifies the scope of the `CompletionReport`; `FAILED_FILES_ONLY` is the only scope currently supported. When `Scope` is set to `FAILED_FILES_ONLY`, the `CompletionReport` only contains information about files that the data repository task failed to process.  
Type: String  
Valid Values: `FAILED_FILES_ONLY`   
Required: No

## See Also
<a name="API_CompletionReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CompletionReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CompletionReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CompletionReport) 