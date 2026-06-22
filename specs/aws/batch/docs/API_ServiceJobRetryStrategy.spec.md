---
id: "@specs/aws/batch/docs/API_ServiceJobRetryStrategy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobRetryStrategy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobRetryStrategy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobRetryStrategy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobRetryStrategy
<a name="API_ServiceJobRetryStrategy"></a>

The retry strategy for service jobs. This defines how many times to retry a failed service job and under what conditions. For more information, see [Service job retry strategies](https://docs.aws.amazon.com/batch/latest/userguide/service-job-retries.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_ServiceJobRetryStrategy_Contents"></a>

 ** attempts **   <a name="Batch-Type-ServiceJobRetryStrategy-attempts"></a>
The number of times to move a service job to `RUNNABLE` status. You can specify between 1 and 10 attempts.  
Type: Integer  
Required: Yes

 ** evaluateOnExit **   <a name="Batch-Type-ServiceJobRetryStrategy-evaluateOnExit"></a>
Array of `ServiceJobEvaluateOnExit` objects that specify conditions under which the service job should be retried or failed.  
Type: Array of [ServiceJobEvaluateOnExit](API_ServiceJobEvaluateOnExit.md) objects  
Required: No

## See Also
<a name="API_ServiceJobRetryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobRetryStrategy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobRetryStrategy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobRetryStrategy) 