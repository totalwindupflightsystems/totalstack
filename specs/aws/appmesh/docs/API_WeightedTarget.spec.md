---
id: "@specs/aws/appmesh/docs/API_WeightedTarget"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WeightedTarget"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# WeightedTarget

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_WeightedTarget
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WeightedTarget
<a name="API_WeightedTarget"></a>

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

## Contents
<a name="API_WeightedTarget_Contents"></a>

 ** virtualNode **   <a name="appmesh-Type-WeightedTarget-virtualNode"></a>
The virtual node to associate with the weighted target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** weight **   <a name="appmesh-Type-WeightedTarget-weight"></a>
The relative weight of the weighted target.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: Yes

 ** port **   <a name="appmesh-Type-WeightedTarget-port"></a>
The targeted port of the weighted object.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_WeightedTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/WeightedTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/WeightedTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/WeightedTarget) 