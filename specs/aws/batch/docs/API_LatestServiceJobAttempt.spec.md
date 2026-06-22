---
id: "@specs/aws/batch/docs/API_LatestServiceJobAttempt"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LatestServiceJobAttempt"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# LatestServiceJobAttempt

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_LatestServiceJobAttempt
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LatestServiceJobAttempt
<a name="API_LatestServiceJobAttempt"></a>

Information about the latest attempt of a service job. A Service job can transition from `SCHEDULED` back to `RUNNABLE` state when they encounter capacity constraints.

## Contents
<a name="API_LatestServiceJobAttempt_Contents"></a>

 ** serviceResourceId **   <a name="Batch-Type-LatestServiceJobAttempt-serviceResourceId"></a>
The service resource identifier associated with the service job attempt.  
Type: [ServiceResourceId](API_ServiceResourceId.md) object  
Required: No

## See Also
<a name="API_LatestServiceJobAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LatestServiceJobAttempt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LatestServiceJobAttempt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LatestServiceJobAttempt) 