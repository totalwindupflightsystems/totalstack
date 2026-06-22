---
id: "@specs/aws/eks/docs/API_InsightStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InsightStatus"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# InsightStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_InsightStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InsightStatus
<a name="API_InsightStatus"></a>

The status of the insight.

## Contents
<a name="API_InsightStatus_Contents"></a>

 ** reason **   <a name="AmazonEKS-Type-InsightStatus-reason"></a>
Explanation on the reasoning for the status of the resource.   
Type: String  
Required: No

 ** status **   <a name="AmazonEKS-Type-InsightStatus-status"></a>
The status of the resource.  
Type: String  
Valid Values: `PASSING | WARNING | ERROR | UNKNOWN`   
Required: No

## See Also
<a name="API_InsightStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/InsightStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/InsightStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/InsightStatus) 