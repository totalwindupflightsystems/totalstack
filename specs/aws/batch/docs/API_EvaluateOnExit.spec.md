---
id: "@specs/aws/batch/docs/API_EvaluateOnExit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EvaluateOnExit"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EvaluateOnExit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EvaluateOnExit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EvaluateOnExit
<a name="API_EvaluateOnExit"></a>

Specifies an array of up to 5 conditions to be met, and an action to take (`RETRY` or `EXIT`) if all conditions are met. If none of the `EvaluateOnExit` conditions in a `RetryStrategy` match, then the job is retried.

## Contents
<a name="API_EvaluateOnExit_Contents"></a>

 ** action **   <a name="Batch-Type-EvaluateOnExit-action"></a>
Specifies the action to take if all of the specified conditions (`onStatusReason`, `onReason`, and `onExitCode`) are met. The values aren't case sensitive.  
Type: String  
Valid Values: `RETRY | EXIT`   
Required: Yes

 ** onExitCode **   <a name="Batch-Type-EvaluateOnExit-onExitCode"></a>
Contains a glob pattern to match against the decimal representation of the `ExitCode` returned for a job. The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (\*) so that only the start of the string needs to be an exact match.  
The string can contain up to 512 characters.  
Type: String  
Required: No

 ** onReason **   <a name="Batch-Type-EvaluateOnExit-onReason"></a>
Contains a glob pattern to match against the `Reason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (\*) so that only the start of the string needs to be an exact match.  
Type: String  
Required: No

 ** onStatusReason **   <a name="Batch-Type-EvaluateOnExit-onStatusReason"></a>
Contains a glob pattern to match against the `StatusReason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (\*) so that only the start of the string needs to be an exact match.  
Type: String  
Required: No

## See Also
<a name="API_EvaluateOnExit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EvaluateOnExit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EvaluateOnExit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EvaluateOnExit) 