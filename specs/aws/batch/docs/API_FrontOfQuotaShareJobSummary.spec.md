---
id: "@specs/aws/batch/docs/API_FrontOfQuotaShareJobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FrontOfQuotaShareJobSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FrontOfQuotaShareJobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FrontOfQuotaShareJobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FrontOfQuotaShareJobSummary
<a name="API_FrontOfQuotaShareJobSummary"></a>

An object that represents summary details for the first `RUNNABLE` job in a quota share.

## Contents
<a name="API_FrontOfQuotaShareJobSummary_Contents"></a>

 ** earliestTimeAtPosition **   <a name="Batch-Type-FrontOfQuotaShareJobSummary-earliestTimeAtPosition"></a>
The Unix timestamp (in milliseconds) for when the job transitioned to its current position in the quota share.  
Type: Long  
Required: No

 ** jobArn **   <a name="Batch-Type-FrontOfQuotaShareJobSummary-jobArn"></a>
The ARN for a job in a named quota share.  
Type: String  
Required: No

## See Also
<a name="API_FrontOfQuotaShareJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQuotaShareJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQuotaShareJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQuotaShareJobSummary) 