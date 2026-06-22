---
id: "@specs/aws/emr/docs/API_FailureDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailureDetails"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# FailureDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_FailureDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailureDetails
<a name="API_FailureDetails"></a>

The details of the step failure. The service attempts to detect the root cause for many common failures.

## Contents
<a name="API_FailureDetails_Contents"></a>

 ** LogFile **   <a name="EMR-Type-FailureDetails-LogFile"></a>
The path to the log file where the step failure root cause was originally recorded.  
Type: String  
Required: No

 ** Message **   <a name="EMR-Type-FailureDetails-Message"></a>
The descriptive message including the error the Amazon EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.  
Type: String  
Required: No

 ** Reason **   <a name="EMR-Type-FailureDetails-Reason"></a>
The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns "Unknown Error" as a reason.  
Type: String  
Required: No

## See Also
<a name="API_FailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/FailureDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/FailureDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/FailureDetails) 