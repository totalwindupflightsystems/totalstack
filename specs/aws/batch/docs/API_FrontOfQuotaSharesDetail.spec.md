---
id: "@specs/aws/batch/docs/API_FrontOfQuotaSharesDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FrontOfQuotaSharesDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FrontOfQuotaSharesDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FrontOfQuotaSharesDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FrontOfQuotaSharesDetail
<a name="API_FrontOfQuotaSharesDetail"></a>

An object that represents the details of the first `RUNNABLE` job in each named quota share associated with a single job queue.

## Contents
<a name="API_FrontOfQuotaSharesDetail_Contents"></a>

 ** lastUpdatedAt **   <a name="Batch-Type-FrontOfQuotaSharesDetail-lastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when the first `RUNNABLE` job per quota share were all last updated.  
Type: Long  
Required: No

 ** quotaShares **   <a name="Batch-Type-FrontOfQuotaSharesDetail-quotaShares"></a>
Contains a list of the first `RUNNABLE` job in each named quota share.  
Type: String to array of [FrontOfQuotaShareJobSummary](API_FrontOfQuotaShareJobSummary.md) objects map  
Required: No

## See Also
<a name="API_FrontOfQuotaSharesDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQuotaSharesDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQuotaSharesDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQuotaSharesDetail) 