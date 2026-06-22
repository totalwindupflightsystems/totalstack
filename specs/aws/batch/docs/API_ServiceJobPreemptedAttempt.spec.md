---
id: "@specs/aws/batch/docs/API_ServiceJobPreemptedAttempt"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobPreemptedAttempt"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobPreemptedAttempt

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobPreemptedAttempt
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobPreemptedAttempt
<a name="API_ServiceJobPreemptedAttempt"></a>

Detailed information about a preempted attempt of a service job.

## Contents
<a name="API_ServiceJobPreemptedAttempt_Contents"></a>

 ** serviceResourceId **   <a name="Batch-Type-ServiceJobPreemptedAttempt-serviceResourceId"></a>
The service resource identifier associated with the service job attempt.  
Type: [ServiceResourceId](API_ServiceResourceId.md) object  
Required: No

 ** startedAt **   <a name="Batch-Type-ServiceJobPreemptedAttempt-startedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt was started.  
Type: Long  
Required: No

 ** statusReason **   <a name="Batch-Type-ServiceJobPreemptedAttempt-statusReason"></a>
A string that provides additional details for the current status of the service job attempt.  
Type: String  
Required: No

 ** stoppedAt **   <a name="Batch-Type-ServiceJobPreemptedAttempt-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt stopped running.  
Type: Long  
Required: No

## See Also
<a name="API_ServiceJobPreemptedAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobPreemptedAttempt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobPreemptedAttempt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobPreemptedAttempt) 