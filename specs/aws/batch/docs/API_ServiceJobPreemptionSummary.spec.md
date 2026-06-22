---
id: "@specs/aws/batch/docs/API_ServiceJobPreemptionSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobPreemptionSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobPreemptionSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobPreemptionSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobPreemptionSummary
<a name="API_ServiceJobPreemptionSummary"></a>

Summarizes the preemptions of the service job. This field appears on a service job when it has been preempted.

## Contents
<a name="API_ServiceJobPreemptionSummary_Contents"></a>

 ** preemptedAttemptCount **   <a name="Batch-Type-ServiceJobPreemptionSummary-preemptedAttemptCount"></a>
The total number of times the service job has been preempted.  
Type: Integer  
Required: No

 ** recentPreemptedAttempts **   <a name="Batch-Type-ServiceJobPreemptionSummary-recentPreemptedAttempts"></a>
A list of the most recent preemption attempts for the service job.  
Type: Array of [ServiceJobPreemptedAttempt](API_ServiceJobPreemptedAttempt.md) objects  
Required: No

## See Also
<a name="API_ServiceJobPreemptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobPreemptionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobPreemptionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobPreemptionSummary) 