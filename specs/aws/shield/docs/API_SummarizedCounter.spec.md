---
id: "@specs/aws/shield/docs/API_SummarizedCounter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SummarizedCounter"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# SummarizedCounter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_SummarizedCounter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SummarizedCounter
<a name="API_SummarizedCounter"></a>

The counter that describes a DDoS attack.

## Contents
<a name="API_SummarizedCounter_Contents"></a>

 ** Average **   <a name="AWSShield-Type-SummarizedCounter-Average"></a>
The average value of the counter for a specified time period.  
Type: Double  
Required: No

 ** Max **   <a name="AWSShield-Type-SummarizedCounter-Max"></a>
The maximum value of the counter for a specified time period.  
Type: Double  
Required: No

 ** N **   <a name="AWSShield-Type-SummarizedCounter-N"></a>
The number of counters for a specified time period.  
Type: Integer  
Required: No

 ** Name **   <a name="AWSShield-Type-SummarizedCounter-Name"></a>
The counter name.  
Type: String  
Required: No

 ** Sum **   <a name="AWSShield-Type-SummarizedCounter-Sum"></a>
The total of counter values for a specified time period.  
Type: Double  
Required: No

 ** Unit **   <a name="AWSShield-Type-SummarizedCounter-Unit"></a>
The unit of the counters.  
Type: String  
Required: No

## See Also
<a name="API_SummarizedCounter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/SummarizedCounter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/SummarizedCounter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/SummarizedCounter) 