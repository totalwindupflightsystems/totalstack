---
id: "@specs/aws/shield/docs/API_AttackSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackSummary"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackSummary
<a name="API_AttackSummary"></a>

Summarizes all DDoS attacks for a specified time period.

## Contents
<a name="API_AttackSummary_Contents"></a>

 ** AttackId **   <a name="AWSShield-Type-AttackSummary-AttackId"></a>
The unique identifier (ID) of the attack.  
Type: String  
Required: No

 ** AttackVectors **   <a name="AWSShield-Type-AttackSummary-AttackVectors"></a>
The list of attacks for a specified time period.  
Type: Array of [AttackVectorDescription](API_AttackVectorDescription.md) objects  
Required: No

 ** EndTime **   <a name="AWSShield-Type-AttackSummary-EndTime"></a>
The end time of the attack, in Unix time in seconds.   
Type: Timestamp  
Required: No

 ** ResourceArn **   <a name="AWSShield-Type-AttackSummary-ResourceArn"></a>
The ARN (Amazon Resource Name) of the resource that was attacked.  
Type: String  
Required: No

 ** StartTime **   <a name="AWSShield-Type-AttackSummary-StartTime"></a>
The start time of the attack, in Unix time in seconds.   
Type: Timestamp  
Required: No

## See Also
<a name="API_AttackSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackSummary) 