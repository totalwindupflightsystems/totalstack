---
id: "@specs/aws/batch/docs/API_ServiceJobPreemptionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobPreemptionConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobPreemptionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobPreemptionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobPreemptionConfiguration
<a name="API_ServiceJobPreemptionConfiguration"></a>

Specifies the service job behavior when preempted.

## Contents
<a name="API_ServiceJobPreemptionConfiguration_Contents"></a>

 ** preemptionRetriesBeforeTermination **   <a name="Batch-Type-ServiceJobPreemptionConfiguration-preemptionRetriesBeforeTermination"></a>
The number of times a service job can be retried after it is preempted. A job will be terminated when preemption retries have been exhausted. If this field is unset, preempted jobs will be requeued an unlimited number of times.   
Type: Integer  
Required: No

## See Also
<a name="API_ServiceJobPreemptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobPreemptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobPreemptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobPreemptionConfiguration) 