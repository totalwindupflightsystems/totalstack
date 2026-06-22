---
id: "@specs/aws/eks/docs/API_ElasticLoadBalancing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ElasticLoadBalancing"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ElasticLoadBalancing

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ElasticLoadBalancing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ElasticLoadBalancing
<a name="API_ElasticLoadBalancing"></a>

Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide*.

## Contents
<a name="API_ElasticLoadBalancing_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-ElasticLoadBalancing-enabled"></a>
Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your AWS account.  
Type: Boolean  
Required: No

## See Also
<a name="API_ElasticLoadBalancing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ElasticLoadBalancing) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ElasticLoadBalancing) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ElasticLoadBalancing) 