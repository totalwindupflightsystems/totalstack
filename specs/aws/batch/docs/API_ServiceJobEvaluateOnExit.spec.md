---
id: "@specs/aws/batch/docs/API_ServiceJobEvaluateOnExit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobEvaluateOnExit"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobEvaluateOnExit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobEvaluateOnExit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobEvaluateOnExit
<a name="API_ServiceJobEvaluateOnExit"></a>

Specifies conditions for when to exit or retry a service job based on the exit status or status reason.

## Contents
<a name="API_ServiceJobEvaluateOnExit_Contents"></a>

 ** action **   <a name="Batch-Type-ServiceJobEvaluateOnExit-action"></a>
The action to take if the service job exits with the specified condition. Valid values are `RETRY` and `EXIT`.  
Type: String  
Valid Values: `RETRY | EXIT`   
Required: No

 ** onStatusReason **   <a name="Batch-Type-ServiceJobEvaluateOnExit-onStatusReason"></a>
Contains a glob pattern to match against the StatusReason returned for a job. The pattern can contain up to 512 characters and can contain all printable characters. It can optionally end with an asterisk (\*) so that only the start of the string needs to be an exact match.  
Type: String  
Required: No

## See Also
<a name="API_ServiceJobEvaluateOnExit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobEvaluateOnExit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobEvaluateOnExit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobEvaluateOnExit) 