---
id: "@specs/aws/emr/docs/API_CancelStepsInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelStepsInfo"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CancelStepsInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CancelStepsInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelStepsInfo
<a name="API_CancelStepsInfo"></a>

Specification of the status of a CancelSteps request. Available only in Amazon EMR version 4.8.0 and later, excluding version 5.0.0.

## Contents
<a name="API_CancelStepsInfo_Contents"></a>

 ** Reason **   <a name="EMR-Type-CancelStepsInfo-Reason"></a>
The reason for the failure if the CancelSteps request fails.  
Type: String  
Required: No

 ** Status **   <a name="EMR-Type-CancelStepsInfo-Status"></a>
The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.  
Type: String  
Valid Values: `SUBMITTED | FAILED`   
Required: No

 ** StepId **   <a name="EMR-Type-CancelStepsInfo-StepId"></a>
The encrypted StepId of a step.  
Type: String  
Required: No

## See Also
<a name="API_CancelStepsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CancelStepsInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CancelStepsInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CancelStepsInfo) 