---
id: "@specs/aws/sesv2/docs/API_DeliverabilityTestReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeliverabilityTestReport"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeliverabilityTestReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeliverabilityTestReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeliverabilityTestReport
<a name="API_DeliverabilityTestReport"></a>

An object that contains metadata related to a predictive inbox placement test.

## Contents
<a name="API_DeliverabilityTestReport_Contents"></a>

 ** CreateDate **   <a name="SES-Type-DeliverabilityTestReport-CreateDate"></a>
The date and time when the predictive inbox placement test was created.  
Type: Timestamp  
Required: No

 ** DeliverabilityTestStatus **   <a name="SES-Type-DeliverabilityTestReport-DeliverabilityTestStatus"></a>
The status of the predictive inbox placement test. If the status is `IN_PROGRESS`, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is `COMPLETE`, then the test is finished, and you can use the `GetDeliverabilityTestReport` to view the results of the test.  
Type: String  
Valid Values: `IN_PROGRESS | COMPLETED`   
Required: No

 ** FromEmailAddress **   <a name="SES-Type-DeliverabilityTestReport-FromEmailAddress"></a>
The sender address that you specified for the predictive inbox placement test.  
Type: String  
Required: No

 ** ReportId **   <a name="SES-Type-DeliverabilityTestReport-ReportId"></a>
A unique string that identifies the predictive inbox placement test.  
Type: String  
Required: No

 ** ReportName **   <a name="SES-Type-DeliverabilityTestReport-ReportName"></a>
A name that helps you identify a predictive inbox placement test report.  
Type: String  
Required: No

 ** Subject **   <a name="SES-Type-DeliverabilityTestReport-Subject"></a>
The subject line for an email that you submitted in a predictive inbox placement test.  
Type: String  
Required: No

## See Also
<a name="API_DeliverabilityTestReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeliverabilityTestReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeliverabilityTestReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeliverabilityTestReport) 