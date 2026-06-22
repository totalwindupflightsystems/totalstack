---
id: "@specs/aws/sesv2/docs/API_MetricDataError"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MetricDataError"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MetricDataError

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MetricDataError
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MetricDataError
<a name="API_MetricDataError"></a>

An error corresponding to the unsuccessful processing of a single metric data query.

## Contents
<a name="API_MetricDataError_Contents"></a>

 ** Code **   <a name="SES-Type-MetricDataError-Code"></a>
The query error code. Can be one of:  
+  `INTERNAL_FAILURE` – Amazon SES has failed to process one of the queries.
+  `ACCESS_DENIED` – You have insufficient access to retrieve metrics based on the given query.
Type: String  
Valid Values: `INTERNAL_FAILURE | ACCESS_DENIED`   
Required: No

 ** Id **   <a name="SES-Type-MetricDataError-Id"></a>
The query identifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** Message **   <a name="SES-Type-MetricDataError-Message"></a>
The error message associated with the current query error.  
Type: String  
Required: No

## See Also
<a name="API_MetricDataError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MetricDataError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MetricDataError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MetricDataError) 