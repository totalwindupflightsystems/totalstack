---
id: "@specs/aws/sesv2/docs/API_FailureInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailureInfo"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# FailureInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_FailureInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailureInfo
<a name="API_FailureInfo"></a>

An object that contains the failure details about a job.

## Contents
<a name="API_FailureInfo_Contents"></a>

 ** ErrorMessage **   <a name="SES-Type-FailureInfo-ErrorMessage"></a>
A message about why the job failed.  
Type: String  
Required: No

 ** FailedRecordsS3Url **   <a name="SES-Type-FailureInfo-FailedRecordsS3Url"></a>
An Amazon S3 pre-signed URL that contains all the failed records and related information.  
Type: String  
Required: No

## See Also
<a name="API_FailureInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/FailureInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/FailureInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/FailureInfo) 