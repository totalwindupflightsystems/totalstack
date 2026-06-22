---
id: "@specs/aws/sesv2/docs/API_Recommendation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Recommendation"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Recommendation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Recommendation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Recommendation
<a name="API_Recommendation"></a>

A recommendation generated for your account.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** CreatedTimestamp **   <a name="SES-Type-Recommendation-CreatedTimestamp"></a>
The first time this issue was encountered and the recommendation was generated.  
Type: Timestamp  
Required: No

 ** Description **   <a name="SES-Type-Recommendation-Description"></a>
The recommendation description / disambiguator - e.g. `DKIM1` and `DKIM2` are different recommendations about your DKIM setup.  
Type: String  
Required: No

 ** Impact **   <a name="SES-Type-Recommendation-Impact"></a>
The recommendation impact, with values like `HIGH` or `LOW`.  
Type: String  
Valid Values: `LOW | HIGH`   
Required: No

 ** LastUpdatedTimestamp **   <a name="SES-Type-Recommendation-LastUpdatedTimestamp"></a>
The last time the recommendation was updated.  
Type: Timestamp  
Required: No

 ** ResourceArn **   <a name="SES-Type-Recommendation-ResourceArn"></a>
The resource affected by the recommendation, with values like `arn:aws:ses:us-east-1:123456789012:identity/example.com`.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Status **   <a name="SES-Type-Recommendation-Status"></a>
The recommendation status, with values like `OPEN` or `FIXED`.  
Type: String  
Valid Values: `OPEN | FIXED`   
Required: No

 ** Type **   <a name="SES-Type-Recommendation-Type"></a>
The recommendation type, with values like `DKIM`, `SPF`, `DMARC`, `BIMI`, or `COMPLAINT`.  
Type: String  
Valid Values: `DKIM | DMARC | SPF | BIMI | COMPLAINT | BOUNCE | FEEDBACK_3P | IP_LISTING`   
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Recommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Recommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Recommendation) 