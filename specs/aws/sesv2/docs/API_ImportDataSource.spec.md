---
id: "@specs/aws/sesv2/docs/API_ImportDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportDataSource"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ImportDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ImportDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportDataSource
<a name="API_ImportDataSource"></a>

An object that contains details about the data source of the import job.

## Contents
<a name="API_ImportDataSource_Contents"></a>

 ** DataFormat **   <a name="SES-Type-ImportDataSource-DataFormat"></a>
The data format of the import job's data source.  
Type: String  
Valid Values: `CSV | JSON`   
Required: Yes

 ** S3Url **   <a name="SES-Type-ImportDataSource-S3Url"></a>
An Amazon S3 URL in the format s3://*<bucket\_name>*/*<object>*.  
Type: String  
Pattern: `^s3:\/\/([^\/]+)\/(.*?([^\/]+)\/?)$`   
Required: Yes

## See Also
<a name="API_ImportDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ImportDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ImportDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ImportDataSource) 